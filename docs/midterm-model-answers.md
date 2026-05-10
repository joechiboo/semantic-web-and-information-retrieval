# 期中考模範答案速記卡

> 考前一晚速記用。每題只列「考試最少要寫到的內容」。
> 英文出題，中文作答。涵蓋影片 01、05、06、07、08、09。

---

## Q1：What is IR? (Information Retrieval)

> Information Retrieval 是從**大型集合（Large Collections）**中，找到能滿足使用者**資訊需求（Information Need）**的**非結構化文件（Unstructured Documents，通常為文字）**。
>
> 應用：**Web Search、Email Search、Enterprise Knowledge Base、Legal IR**。

**口訣：大、需、非** + 至少 2 個應用例子

---

## Q2：Classic Search Model【可能要畫圖】

```text
User Task（使用者任務）
    ↓
Information Need（資訊需求）
    ↓
Query（查詢）
    ↓
Search Engine ←→ Document Collection
    ↓
Results
    ↓
Query Refinement → 回到 Query
```

**四個必寫觀念：**
1. 每層「翻譯」可能丟失資訊（Task → Need → Query）
2. **Query Misformulation** 會降低結果品質
3. 搜尋是 **Iterative Process**（迭代過程）
4. **評估基準是 Information Need，不是 Query**

---

## Q3：Precision and Recall

| 指標 | 公式 |
|------|------|
| **Precision** | 相關 ∩ 檢索 / 檢索 |
| **Recall** | 相關 ∩ 檢索 / 相關 |

**例：** 100 隻老鼠，抓到 20 隻（15 老鼠 + 5 蟑螂）
- Precision = 15/20 = 75%
- Recall = 15/100 = 15%

**兩個延伸要點：**
- **Trade-off**：Precision ↑ → Recall ↓
- **評估基準**：相對於 **Information Need**，不是 Query

---

## Q4：Term-Document Matrix & 為什麼不實用

**定義：** Boolean Matrix
- 列 = Terms（詞項）
- 行 = Documents
- 值 = 0 或 1

**不實用的原因：**
- **規模問題**：100 萬文件 × 50 萬詞項 = **半兆**個 cells
- **稀疏性（Sparsity）**：99%+ 都是 0

**為什麼 grep 也不行？**
1. 線性掃描太慢
2. NOT 查詢不好實作
3. 無法做鄰近搜尋（Proximity Search）
4. 無法做排名（Ranking）

→ **解法：只記錄 1 的位置 → Inverted Index**

---

## Q5：Inverted Index 結構【可能要畫圖】

```text
   左側（Dictionary）           右側（Postings Lists）
┌──────────────────┐         ┌──────────────────┐
│ Terms + doc freq │  →→→   │ Lists of docIDs  │
├──────────────────┤Pointers ├──────────────────┤
│ brutus   2       │   →     │ [1, 2]           │
│ caesar   2       │   →     │ [1, 2]           │
└──────────────────┘         └──────────────────┘
   小，放 Memory               大，放 Disk
```

**關鍵特性：**
- Postings List 按 **Document ID 排序**（為 Merge Algorithm 鋪路）
- Dictionary 在 Memory，Postings 在 Disk

---

## Q6：Inverted Index 建構流程

**前處理 4 階段：**

| 階段 | 做什麼 |
|------|--------|
| **Tokenization** | 字元序列切成 word tokens |
| **Normalization** | 統一文字和查詢的形式（U.S.A. = USA）|
| **Stemming** | 不同詞型對到同一詞根（authorize/authorization）|
| **Stop Words** | 移除極常見詞（the, a）|

**建索引三步驟：**
1. 標上文件 ID
2. **排序**（主鍵=詞字母、次鍵=docID）← 最花時間
3. **合併（Consolidation）**：同詞組成 Postings List

---

## Q7：INTERSECT 演算法 + 為什麼要排序

```text
INTERSECT(p1, p2)
1  answer ← ⟨⟩
2  while p1 ≠ NIL and p2 ≠ NIL
3    do if docID(p1) = docID(p2)
4         then ADD(answer, docID(p1))
5              p1 ← next(p1)
6              p2 ← next(p2)
7         else if docID(p1) < docID(p2)   ← 注意是 <
8              then p1 ← next(p1)         ← 誰小誰動
9              else p2 ← next(p2)
10 return answer
```

**口訣：誰小誰動**

**為什麼要排序？**

|  | 有排序 | 沒排序 |
|--|--------|--------|
| 演算法 | 雙指標掃描 | 巢狀迴圈 |
| 複雜度 | **O(x + y)** | O(x × y) |

x = y = 1000 → 2000 次 vs 1,000,000 次

---

## Q8：Boolean Retrieval Model + Query Optimization

**Boolean Retrieval Model：**

> 使用者用 **AND/OR/NOT** 運算子組合詞項，文件對查詢做**精確匹配（exact match）**，**沒有排名（no ranking）**。

**三大特徵：**
1. AND/OR/NOT 運算子
2. **Exact Match**
3. **No Ranking**

**Query Optimization（AND 多詞查詢）：**

> 從 **Document Frequency（doc freq）最低**的詞開始處理。

範例：`Brutus AND Caesar AND Calpurnia`

| 詞 | doc freq |
|----|----------|
| Brutus | 1,000,000 |
| Caesar | 1,000,000 |
| Calpurnia | 1,000 |

→ 從 Calpurnia 開始（最短的 postings list），中間結果一直保持很小

**為什麼可行？** Dictionary 中存有每個詞的 **doc freq**，查詢前可快速排序決定處理順序。

---

## Q9：Phrase Queries + Biword Index

**Phrase Queries：**

> 使用者用引號 `"information retrieval"` 把多個詞當作**一個整體**查詢，要求**詞相鄰且順序正確**。

**為什麼標準 Inverted Index 不夠？**

只能告訴你某詞**有沒有出現**，**不知道相對位置**。
範例：「university at Stanford for information」雖然兩詞都有，但**不相鄰**，不該匹配。

**Biword Index：**

> 把每**兩個連續詞**當作一個「詞項」來索引。

範例：「Friends, Romans, countrymen」→
```text
friends romans     → [17, 33]
romans countrymen  → [17]
```

長片語拆成多個 biword 做 AND：
`"stanford university palo alto"` → `"stanford university"` AND `"university palo"` AND `"palo alto"`

**Biword Index 兩個限制：**

1. **False Positives**：拆解後可能匹配到不連續的組合
2. **Dictionary Blowup（字典爆炸）** ⚠️ 主要問題
   - 字典大小變成詞數的**平方**
   - 不能做 triword、quadword
   - **不是標準解法**

---

## Q10：Positional Index + 處理 Phrase Query

**Positional Index：**

> 在 Postings 中除了 docID 外，**還記錄該詞在文件中的位置**。
> 目的：**支援片語查詢和鄰近查詢**（Proximity Queries）。
> ⚠️ 跟 Rank 完全沒關係！

**結構：**
```text
term → < doc.freq;
         docID1: ⟨pos1, pos2, pos3, ...⟩;
         docID2: ⟨pos1, pos2, ...⟩;
         ... >
```

範例：
```text
be → 993,427 documents;
     1: ⟨7, 18, 33, 72, 86, 231⟩;
     2: ⟨3, 149⟩
```

**Two-level Merge（處理 `"information retrieval"`）：**

1. **第一層**：用 Merge Algorithm 找**同時包含兩個詞**的文件（合併 docID）
2. **第二層**：檢查 `pos(retrieval) - pos(information) = 1`（合併 position）

範例：文件 4 中 information 在位置 37、retrieval 在位置 38 → 是片語 ✓

**也能處理 Proximity Queries：**
`information /3 retrieval` → 檢查 `|pos1 - pos2| ≤ 3`

**代價：**
- 比非位置索引大 **2-4 倍**
- 約是原始文字大小的 **1/3 ~ 1/2**

---

## 🔥 整體邏輯鏈（一句話貫穿）

```text
05：grep 太慢 → Matrix → 但太大太稀疏
       ↓
06：改用 Inverted Index（Dictionary + Postings Lists）
       ↓
07：用雙指標 Merge Algorithm 做 AND 查詢，O(x+y)
       ↓
08：Boolean Retrieval Model + Query Optimization（從最小 doc freq 開始）
       ↓
09：標準 Inverted Index 不夠處理片語 → Biword 不可行（字典爆炸）
       ↓
10：Positional Index + Two-level Merge（標準解法）
```

---

## 🎯 易錯點 Top 5

1. **Q1 三關鍵字漏寫**：Large Collections / Information Need / **Unstructured Documents**
2. **Q7 比較方向反**：是「誰小誰動」，不是「誰大誰動」
3. **Q8 漏寫 Exact Match / No Ranking**
4. **Q10 目的寫錯**：是支援片語/鄰近查詢，**不是 Ranking、不是提升效率**
5. **Q9 把 Biword 和 Positional 講成「片語查詢的兩種類型」**：應該是「兩種解法」
