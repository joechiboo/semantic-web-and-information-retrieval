"""
Batch generate Chinese SRT subtitle files for course videos.
Fetches English transcripts from YouTube, translates to Traditional Chinese,
and outputs SRT files.
"""

import json
import time
import sys
import os
import requests
from youtube_transcript_api import YouTubeTranscriptApi

DOCS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "docs")
SRT_DIR = os.path.join(DOCS_DIR, "srt")
TIMESTAMPS_FILE = os.path.join(DOCS_DIR, "timestamps.json")

# All videos: (video_id, srt_filename)
VIDEOS = [
    ("kNkCfaH2rxc", "01-introduction-to-information-retrieval"),
    ("K-yrnyvqXGo", "02-simple-introduction-to-semantic-networks"),
    ("3PgIC9KcSNE", "03-semantic-networks-additional-info"),
    ("sY0kbo251A4", "04-detailed-introduction-to-semantic-networks"),
    ("e81nC0LO0A8", "05-term-document-matrices"),
    ("Wf6HbY2PQDw", "06-the-inverted-index"),
    ("5KbynCj7yRQ", "07-query-processing-with-inverted-index"),
    ("TIN_02pJU-Y", "08-boolean-retrieval-model"),
    ("QVVvx_Csd2I", "09-phrase-queries-and-positional-indexes"),
    ("ZrNmCtSrL48", "10-introducing-ranked-retrieval"),
    ("MiX8_JVP6PE", "11-scoring-with-jaccard-coefficient"),
    ("9UXM2NXVYY0", "12-term-frequency-weighting"),
    ("7nWlI_TVid0", "13-inverse-document-frequency-weighting"),
    ("4-P3ckZprBk", "14-tf-idf-weighting"),
    ("o5nflzfX5tw", "15-the-vector-space-model"),
    ("k1tD7pYKWuM", "16-calculating-tf-idf-cosine-scores"),
    ("b7pfLpVBN84", "17-evaluating-search-engines"),
]


def seconds_to_srt_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def fetch_transcript(video_id):
    """Fetch English transcript from YouTube."""
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id, languages=["en"])
    snippets = []
    for s in transcript.snippets:
        snippets.append({
            "text": s.text,
            "start": s.start,
            "duration": s.duration,
        })
    return snippets


def deduplicate_snippets(snippets):
    """Remove overlapping time ranges - keep non-overlapping sequential segments."""
    if not snippets:
        return []

    result = []
    for s in snippets:
        text = s["text"].replace("\n", " ").strip()
        start = s["start"]
        end = s["start"] + s["duration"]

        if result and start < result[-1]["end"]:
            # Overlap: adjust start to previous end
            start = result[-1]["end"]

        if start < end and text:
            result.append({"text": text, "start": start, "end": end})

    return result


def merge_snippets_to_sentences(snippets):
    """Merge short snippets into segments suitable for translation (~200 chars max)."""
    deduped = deduplicate_snippets(snippets)
    merged = []
    current_text = ""
    current_start = 0
    current_end = 0

    for s in deduped:
        if not current_text:
            current_text = s["text"]
            current_start = s["start"]
            current_end = s["end"]
        else:
            current_text += " " + s["text"]
            current_end = s["end"]

        # Keep chunks small for subtitle readability (~5-8 seconds)
        text_len = len(current_text)
        duration = current_end - current_start
        ends_with_sentence = current_text.rstrip().endswith(('.', '!', '?'))

        if (text_len >= 80 and ends_with_sentence) or text_len >= 120 or duration >= 8:
            merged.append({
                "text": current_text.strip(),
                "start": current_start,
                "end": current_end,
            })
            current_text = ""

    if current_text:
        merged.append({
            "text": current_text.strip(),
            "start": current_start,
            "end": current_end,
        })

    return merged


def translate_text(text, max_retries=3):
    """Translate English text to Traditional Chinese using Google Translate API."""
    url = "https://translate.googleapis.com/translate_a/single"
    params = {
        "client": "gtx",
        "sl": "en",
        "tl": "zh-TW",
        "dt": "t",
        "q": text,
    }
    for attempt in range(max_retries):
        try:
            resp = requests.get(url, params=params, timeout=10)
            resp.raise_for_status()
            result = resp.json()
            translated = "".join(part[0] for part in result[0] if part[0])
            if translated:
                return translated
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2 * (attempt + 1))
                continue
            print(f"  Translation error (attempt {attempt+1}): {e}", file=sys.stderr)
    return text


def make_srt_entry(text, start, end):
    """Create a single SRT entry, splitting text into at most 2 lines."""
    max_line = 35
    if len(text) <= max_line:
        return {"text": text, "start": start, "end": end}

    # Find a good midpoint to split into 2 lines
    mid = len(text) // 2
    best = mid
    for punct in ['，', '。', '、', '；', '：', ' ']:
        idx = text.rfind(punct, mid - 15, mid + 15)
        if idx > 0:
            best = idx + 1
            break
    line1 = text[:best].strip()
    line2 = text[best:].strip()
    return {"text": f"{line1}\n{line2}", "start": start, "end": end}


def generate_srt(video_id, srt_name):
    """Generate a Chinese SRT file for a video."""
    os.makedirs(SRT_DIR, exist_ok=True)
    srt_path = os.path.join(SRT_DIR, f"{srt_name}.srt")

    print(f"\n{'='*60}")
    print(f"Processing: {srt_name}")
    print(f"Video ID: {video_id}")
    print(f"{'='*60}")

    # Step 1: Fetch transcript
    print("  Fetching English transcript...")
    try:
        snippets = fetch_transcript(video_id)
    except Exception as e:
        print(f"  ERROR fetching transcript: {e}", file=sys.stderr)
        return False
    print(f"  Got {len(snippets)} snippets")

    # Step 2: Merge into reasonable segments
    print("  Merging into segments...")
    merged = merge_snippets_to_sentences(snippets)
    print(f"  Merged into {len(merged)} segments")

    # Step 3: Translate each segment
    print("  Translating to Traditional Chinese...")
    srt_entries = []
    seq = 1

    for i, seg in enumerate(merged):
        translated = translate_text(seg["text"])
        time.sleep(0.5)  # Rate limiting

        entry = make_srt_entry(translated, seg["start"], seg["end"])
        srt_entries.append({
            "seq": seq,
            "start": entry["start"],
            "end": entry["end"],
            "text": entry["text"],
        })
        seq += 1

        if (i + 1) % 10 == 0:
            print(f"  Translated {i+1}/{len(merged)} segments...")

    # Step 4: Write SRT file
    print(f"  Writing SRT file ({len(srt_entries)} entries)...")
    with open(srt_path, "w", encoding="utf-8") as f:
        for entry in srt_entries:
            f.write(f"{entry['seq']}\n")
            f.write(f"{seconds_to_srt_time(entry['start'])} --> {seconds_to_srt_time(entry['end'])}\n")
            f.write(f"{entry['text']}\n")
            f.write("\n")

    print(f"  Done! Saved to {srt_path}")

    # Return snippets for timestamps.json
    return snippets


def update_timestamps(video_id, snippets):
    """Update timestamps.json with new transcript data."""
    if os.path.exists(TIMESTAMPS_FILE):
        with open(TIMESTAMPS_FILE, "r", encoding="utf-8") as f:
            timestamps = json.load(f)
    else:
        timestamps = {}

    timestamps[video_id] = [
        {"text": s["text"], "start": s["start"], "duration": s["duration"]}
        for s in snippets
    ]

    with open(TIMESTAMPS_FILE, "w", encoding="utf-8") as f:
        json.dump(timestamps, f, ensure_ascii=False, indent=2)


def main():
    # Determine which videos to process
    existing_srts = set()
    if os.path.isdir(SRT_DIR):
        for f in os.listdir(SRT_DIR):
            if f.endswith(".srt"):
                existing_srts.add(f.replace(".srt", ""))

    to_process = [(vid, name) for vid, name in VIDEOS if name not in existing_srts]

    if not to_process:
        print("All SRT files already exist!")
        return

    print(f"Found {len(to_process)} videos to process:")
    for vid, name in to_process:
        print(f"  - {name} ({vid})")

    success = 0
    failed = []

    for vid, name in to_process:
        try:
            snippets = generate_srt(vid, name)
            if snippets:
                update_timestamps(vid, snippets)
                success += 1
        except Exception as e:
            print(f"  FAILED: {e}", file=sys.stderr)
            failed.append(name)

    print(f"\n{'='*60}")
    print(f"Results: {success} succeeded, {len(failed)} failed")
    if failed:
        print(f"Failed: {', '.join(failed)}")


if __name__ == "__main__":
    sys.stdout.reconfigure(line_buffering=True)
    main()
