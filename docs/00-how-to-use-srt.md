# 如何使用 SRT 字幕檔觀看課程影片

---

## 什麼是 SRT 字幕檔？

SRT（SubRip Text）是最常見的字幕格式，包含：
- 字幕序號
- 時間戳（開始 → 結束）
- 翻譯文字

```
1
00:00:00,000 --> 00:00:05,040
你好，在這個段落中我將介紹資訊檢索的任務

2
00:00:05,040 --> 00:00:10,296
包括目前最主流的形式：網路搜尋
```

---

## 使用方式

### 方法一：瀏覽器外掛（推薦）

在 YouTube 上直接載入中文字幕，邊看邊讀。

#### Substital（Chrome / Firefox）

1. 安裝外掛：
   - Chrome：[Substital - Chrome Web Store](https://chromewebstore.google.com/detail/substital/kkkbiiikppgjdiebcabaolkohplmakip)
   - Firefox：[Substital - Firefox Add-ons](https://addons.mozilla.org/firefox/addon/substital/)

2. 打開 YouTube 影片頁面

3. 點擊播放器右下角的 **Substital 圖示**（或瀏覽器工具列的圖示）

4. 選擇 **「Load subtitle from file」** → 選擇對應的 `.srt` 檔案

5. 字幕就會顯示在影片上了

> **小技巧：** 在 Substital 設定中可以調整字幕的字體大小、位置、背景透明度。

---

### 方法二：VLC 播放器（離線觀看）

如果你已經下載了影片檔案：

1. 用 VLC 開啟影片
2. 選單：**字幕 → 加入字幕檔案**
3. 選擇對應的 `.srt` 檔案

---

### 方法三：Potplayer（離線觀看）

1. 用 Potplayer 開啟影片
2. 右鍵 → **字幕 → 載入字幕**
3. 選擇對應的 `.srt` 檔案

---

## 字幕檔案對照表

| 影片 | 字幕檔 | YouTube 連結 |
|------|--------|-------------|
| 01 - 資訊檢索導論 | `01-introduction-to-information-retrieval.srt` | [連結](https://www.youtube.com/watch?v=kNkCfaH2rxc) |
| 02 - 語意網路簡介 | `02-simple-introduction-to-semantic-networks.srt` | [連結](https://www.youtube.com/watch?v=K-yrnyvqXGo) |
| 03 - 語意網路補充資訊 | `03-semantic-networks-additional-info.srt` | [連結](https://www.youtube.com/watch?v=3PgIC9KcSNE) |
| 04 - 語意網路詳細介紹 | `04-detailed-introduction-to-semantic-networks.srt` | [連結](https://www.youtube.com/watch?v=sY0kbo251A4) |
| 05 - 詞項-文件矩陣 | `05-term-document-matrices.srt` | [連結](https://www.youtube.com/watch?v=e81nC0LO0A8) |
| 06 - 倒排索引 | `06-the-inverted-index.srt` | [連結](https://www.youtube.com/watch?v=Wf6HbY2PQDw) |
| 07 - 使用倒排索引的查詢處理 | `07-query-processing-with-inverted-index.srt` | [連結](https://www.youtube.com/watch?v=5KbynCj7yRQ) |
| 08 - 布林檢索模型 | `08-boolean-retrieval-model.srt` | [連結](https://www.youtube.com/watch?v=TIN_02pJU-Y) |
| 09 - 片語查詢與位置索引 | `09-phrase-queries-and-positional-indexes.srt` | [連結](https://www.youtube.com/watch?v=QVVvx_Csd2I) |
| 10 - 排序檢索導論 | `10-introducing-ranked-retrieval.srt` | [連結](https://www.youtube.com/watch?v=ZrNmCtSrL48) |
| 11 - 使用 Jaccard 係數評分 | `11-scoring-with-jaccard-coefficient.srt` | [連結](https://www.youtube.com/watch?v=MiX8_JVP6PE) |
| 12 - 詞頻加權 | `12-term-frequency-weighting.srt` | [連結](https://www.youtube.com/watch?v=9UXM2NXVYY0) |
| 13 - 逆文件頻率加權 | `13-inverse-document-frequency-weighting.srt` | [連結](https://www.youtube.com/watch?v=7nWlI_TVid0) |
| 14 - TF-IDF 加權 | `14-tf-idf-weighting.srt` | [連結](https://www.youtube.com/watch?v=4-P3ckZprBk) |
| 15 - 向量空間模型 | `15-the-vector-space-model.srt` | [連結](https://www.youtube.com/watch?v=o5nflzfX5tw) |
| 16 - 計算 TF-IDF 餘弦分數 | `16-calculating-tf-idf-cosine-scores.srt` | [連結](https://www.youtube.com/watch?v=k1tD7pYKWuM) |
| 17 - 搜尋引擎評估 | `17-evaluating-search-engines.srt` | [連結](https://www.youtube.com/watch?v=b7pfLpVBN84) |

> **注意：** 03、04 影片為印地語授課，字幕翻譯品質較其他英文授課影片略差。

---

## 如何自行產生更多 SRT 字幕

如果需要為其他影片產生字幕，可以使用 `youtube-transcript-api`：

```bash
pip install youtube-transcript-api
```

```python
from youtube_transcript_api import YouTubeTranscriptApi

ytt_api = YouTubeTranscriptApi()
transcript = ytt_api.fetch('影片ID', languages=['en'])

for i, s in enumerate(transcript.snippets, 1):
    start = s.start
    end = s.start + s.duration
    # 將秒數轉換為 SRT 時間格式 HH:MM:SS,mmm
    # 翻譯 s.text 後寫入 .srt 檔案
```

SRT 時間格式轉換：

```python
def seconds_to_srt_time(seconds):
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    ms = int((seconds % 1) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
```

---

## 注意事項

- SRT 字幕的時間戳來自 YouTube 自動生成的逐字稿，可能有幾秒的偏差
- 翻譯是由 AI 生成，專有名詞可能需要對照英文原文理解
- 建議搭配筆記文檔（`.md` 檔）一起使用，筆記中有完整的逐字稿和重點摘要
