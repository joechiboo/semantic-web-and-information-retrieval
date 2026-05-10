# 期中考 A4 速記表

## 10 題關鍵字（缺即扣分）

| # | 必寫關鍵字 |
|---|----------|
| Q1 | **Large Collections** / **Information Need** / **Unstructured Documents** + 應用：Web/Email/Enterprise/Legal |
| Q2 | 圖（Task→Need→Query→SE↔Coll→Result→Refine）+ 4 觀念：翻譯丟失 / **Misformulation** / **Iterative** / 評估看 **Need** |
| Q3 | P=∩/檢索, R=∩/相關 + 老鼠 15/20、15/100 + **Trade-off** + 評估基準=**Need** |
| Q4 | Boolean(0/1) + **半兆**(1M×500K) + **稀疏 99%+** + grep 4：慢/NOT 難/無鄰近/無 Ranking |
| Q5 | **Dictionary**(doc freq, **Memory**) + **Postings**(**Disk**) + **按 docID 排序** |
| Q6 | 4 階段：Tokenization/Normalization/Stemming/Stop Words + 3 步驟：**標 ID → 排序 → Consolidation** |
| Q7 | 雙指標「**誰小誰動**」+ **O(x+y)** vs O(x×y) |
| Q8 | **AND/OR/NOT** + **Exact Match** + **No Ranking** + 從 **doc freq 最低**開始（Dict 存 doc freq）|
| Q9 | 引號相鄰 + 兩連續詞當 term + **False Positives** + **Dictionary Blowup (V²)** |
| Q10 | 記**位置** + 目的=**支援片語/鄰近**（非 ranking）+ **Two-level Merge** + **2-4 倍**大小 |

## Inverted Index 結構（必畫）
```
   Dictionary (Memory)         Postings Lists (Disk)
┌────────────────────┐         ┌──────────────────┐
│ Term  | doc freq   │ pointer │                  │
├───────┼────────────┤────────→│                  │
│brutus | 2      ────┼────────→│  [1, 2]          │
│caesar | 2      ────┼────────→│  [1, 2]          │
└────────────────────┘         └──────────────────┘
```

## INTERSECT 演算法（Q7 必背）
```
INTERSECT(p1, p2)
1  answer ← ⟨⟩
2  while p1 ≠ NIL and p2 ≠ NIL
3    do if docID(p1) = docID(p2)
4         then ADD(answer, docID(p1)); p1←next(p1); p2←next(p2)
5         else if docID(p1) < docID(p2) then p1←next(p1)
6              else p2←next(p2)
7  return answer
```

## ⚠️ 三大死穴
1. **Q9 ≠ Q10**：Biword 限制是 **V² 字典爆炸**；Positional 代價是 **2-4 倍**
2. **題目問什麼答什麼**：Q3 trade-off 別漏
3. **結構畫對也要寫特性**：Q5 排序+Memory/Disk、Q8 Exact Match+No Ranking、Q10 目的=支援片語
