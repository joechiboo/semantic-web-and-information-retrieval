# 期中考 Q&A 複習卷

> **考試格式：** 英文出題，可用中文回答。英文看不懂可問教授。
> **內容來源：** 主要從**影片**出，較少作業形式（教授 2026-04-28 說明）
> **涵蓋影片：** 01、05、06、07、08、09（共 10 題）
> ⚠️ 02（語意網路）不考；08 的 WestLaw 與歷史內容不考

---

## 影片 01 - Introduction to Information Retrieval

### ⭐ Q1：What is Information Retrieval (IR)?【必考】

**A：**

> IR 是從**大型集合 (Large Collections)** 中，找到能滿足使用者**資訊需求 (Information Need)** 的**非結構化文件 (Unstructured Documents)**（通常為文字）。

**三個關鍵詞必須寫到：**

1. Large Collections
2. Information Need
3. Unstructured Documents

**💡 延伸：** 應用場景如 Web Search、Email Search、企業知識庫、法律檢索

---

### ⭐ Q2：Describe the Classic Search Model【必考，可能要畫圖】

**A：**

```text
    User Task（使用者任務）
         ↓
    Information Need（資訊需求）
         ↓
    Query（查詢）
         ↓
    Search Engine（搜尋引擎） ←→ Document Collection（文件集合）
         ↓
    Results（搜尋結果）
         ↓
    Query Refinement（查詢優化）→ 回到 Query
```

**範例：**

| 階段 | 內容 |
|------|------|
| User Task | 用人道方式趕走車庫的老鼠 |
| Information Need | 不殺死老鼠的方式移走牠們 |
| Query | `how trap mice alive` |

**四個關鍵觀念（必寫）：**

1. 每層「翻譯」可能丟失資訊（Task → Need → Query）
2. **Query Misformulation** 會降低結果品質
3. 搜尋是 **Iterative Process**（迭代過程）
4. **評估基準是 Information Need，不是 Query**

---

### Q3：What are Precision and Recall? How are they calculated?

**A：**

| 指標 | 公式 | 白話 |
|------|------|------|
| **Precision** | 相關 ∩ 檢索 / 檢索 | 「給我的裡面，多少是對的」 |
| **Recall** | 相關 ∩ 檢索 / 相關 | 「對的裡面，找到多少」 |

**例子：** 100 隻老鼠，捕鼠器抓到 20 隻（15 老鼠 + 5 蟑螂）

- Precision = 15/20 = 75%
- Recall = 15/100 = 15%

**💡 兩個延伸要點：**

- **Trade-off**：提高 Precision 會降低 Recall
- **評估基準**：相對於 Information Need，不是 Query

---

## 影片 05 - Term-Document Matrices

### Q4：What is a Term-Document Matrix? Why is it impractical for large collections?

**A：**

**定義：** Term-Document Matrix 是一個 **Boolean Matrix**：

- 列 (Rows) = Terms（詞項）
- 行 (Columns) = Documents（文件）
- 值 (Values) = 0 或 1（該詞是否出現）

**範例：** 莎士比亞劇本 → 取出每個詞的向量做布林運算（AND / NOT）回答查詢

**不實用的原因：**

| 原因 | 說明 |
|------|------|
| **規模問題** | 100 萬文件 × 50 萬詞項 = **半兆**個 cells |
| **稀疏性 (Sparsity)** | 1s 最多 10 億個，**99%+ 是 0** |

**為什麼 grep 也不行？**

1. 線性掃描太慢 (Linear Scan)
2. NOT 查詢不好實作
3. 無法做鄰近搜尋 (Proximity Search)
4. 無法做排名 (Ranking)

**💡 結論：** 只記錄 1 的位置 → 引出 **Inverted Index**

---

## 影片 06 - The Inverted Index

### Q5：What is an Inverted Index? Describe its structure【可能要畫圖】

**A：**

**類比：** 就像**課本後面的索引頁**——從「詞」查「在哪些文件」。

**兩側結構（必須能畫出來）：**

```text
      左側（Dictionary）              右側（Postings Lists）
  ┌────────────────────┐        ┌──────────────────┐
  │ Terms + doc freq   │  →→→  │ Lists of docIDs  │
  ├────────────────────┤Pointers├──────────────────┤
  │ brutus   2         │   →    │ [1, 2]           │
  │ caesar   2         │   →    │ [1, 2]           │
  │ capitol  1         │   →    │ [1]              │
  └────────────────────┘        └──────────────────┘
  相對小，放記憶體 (Memory)       非常大，放硬碟 (Disk)
```

**關鍵特性：**

- Postings List 按 **Document ID 排序**（為 Merge Algorithm 做準備）
- Dictionary 和 Postings 存在不同地方（Memory vs Disk）

---

### Q6：Describe the Inverted Index building process

**A：**

**前處理 4 個階段（Initial stages of text processing）：**

| 階段 | 做什麼 | 範例 |
|------|--------|------|
| **Tokenization** | 把字元序列切成 word tokens | `John's` 怎麼切 |
| **Normalization** | 統一文字和查詢的形式 | `U.S.A.` = `USA` |
| **Stemming** | 不同詞型對到同一詞根 | `authorize`, `authorization` |
| **Stop Words** | 移除極常見的詞（可選） | `the`, `a`, `to`, `of` |

**建索引三步驟：**

1. **標上文件 ID**：每個 token 記錄來自哪個文件
2. **排序**：主鍵=詞字母順序、次鍵=文件 ID
3. **合併 (Consolidation)**：同文件重複合併、同詞組成 Postings List

**💡 重點：** 排序是最花時間的步驟，但排完後 Postings List 自然按 Doc ID 排好。

---

## 影片 07 - Query Processing with Inverted Index

### Q7：Write the INTERSECT algorithm for AND query. Why must postings lists be sorted?

**A：**

**INTERSECT 演算法：**

```text
INTERSECT(p1, p2)
1  answer ← ⟨⟩
2  while p1 ≠ NIL and p2 ≠ NIL
3    do if docID(p1) = docID(p2)
4         then ADD(answer, docID(p1))
5              p1 ← next(p1)
6              p2 ← next(p2)
7         else if docID(p1) < docID(p2)
8              then p1 ← next(p1)
9              else p2 ← next(p2)
10 return answer
```

**核心觀念（雙指標 Two-pointer Scan）：**

- **相等** → 加入結果，兩指標都動
- **p1 較小** → 只動 p1
- **p2 較小** → 只動 p2

**為什麼 Postings 要排序？**

| | 有排序 | 沒排序 |
|--|--------|--------|
| 演算法 | 雙指標掃描 | 巢狀迴圈 |
| 時間複雜度 | **O(x + y)** | O(x × y) |

**對比：** x = y = 1000 時

- 有排序：2000 次
- 沒排序：1,000,000 次

**💡 因此 Inverted Index 建構時就要把 Postings List 排序好（影片 06 第 2 步），讓查詢能跑得快。**

---

## 影片 08 - The Boolean Retrieval Model

### Q8：What is the Boolean Retrieval Model? Explain Query Optimization for AND queries

**A：**

**Boolean Retrieval Model：**

> 一種資訊檢索模型，使用者用 **Boolean 運算子**（AND / OR / NOT）組合詞項，文件「精確匹配」或「不匹配」這個布林表達式，沒有排名。

**三個運算子：**

- `Brutus AND Caesar` → 兩者都要有
- `Brutus OR Caesar` → 至少一個有
- `Brutus AND NOT Caesar` → 有 Brutus 沒 Caesar

**Query Optimization（查詢最佳化）：**

對於 AND 多詞查詢，**從文件頻率最低的詞開始處理**。

**範例：** `Brutus AND Caesar AND Calpurnia`

| 詞 | doc freq |
|----|----------|
| Brutus | 1,000,000 |
| Caesar | 1,000,000 |
| Calpurnia | 1,000 |

→ 從 Calpurnia 開始（最短的 Postings List），AND 結果不會比 Calpurnia 大，能最快縮小範圍。

**💡 為什麼可行？** Dictionary 有存 doc freq，可以快速查詢決定處理順序。

---

## 影片 09 - Phrase Queries and Positional Indexes

### Q9：What are Phrase Queries? Explain Biword Index and its limitations

**A：**

**Phrase Queries（片語查詢）：**

> 使用者用引號 `"information retrieval"` 把多個詞當作**一個整體**查詢，要求詞**相鄰且順序正確**。

**為什麼標準 Inverted Index 不夠？**

標準 Inverted Index 只能告訴你某個詞**有沒有出現在文件**，但**不知道詞與詞之間是否相鄰**。

範例：搜尋 `"information retrieval"`，文件「I went to **university** at Stanford for **information**」雖然兩個詞都有，但**不是片語**，不該匹配。

**Biword Index（雙詞索引）：**

> 把每兩個連續詞當作一個「詞項」來索引。

範例：「Friends, Romans, countrymen」產生：

```text
biword          → docIDs
─────────────────────
friends romans  → [17, 33, ...]
romans countrymen → [17, ...]
```

**處理長片語：** 拆成多個 biword 做 AND
- `"stanford university palo alto"` → `"stanford university"` AND `"university palo"` AND `"palo alto"`

**Biword Index 的兩個問題：**

1. **False Positives（假陽性）**：拆解後可能匹配到不連續的片語
2. **字典爆炸 (Dictionary Blowup)** ⚠️ 主要問題
   - 字典大小變成詞數的**平方**
   - 不可能做 triword（三詞）或 quadword（四詞）索引

**💡 結論：** Biword Index **不是標準解法**，但可作為輔助（後面會提）。

---

### Q10：What is a Positional Index? How does it support phrase queries?

**A：**

**Positional Index（位置索引，標準解法）：**

> 在 Postings 中除了記錄 docID，**還記錄該詞在文件中的位置**。

**結構：**

```text
term → < doc.freq;
         docID1: ⟨pos1, pos2, pos3, ...⟩;
         docID2: ⟨pos1, pos2, ...⟩;
         ... >
```

**範例：**

```text
be → 993,427 documents;
     1: ⟨7, 18, 33, 72, 86, 231⟩;
     2: ⟨3, 149⟩;
     4: ⟨17, 191, 291, 430, 434⟩;
     5: ⟨363, 367⟩
```

→ `be` 在文件 1 的第 7、18、33... 個位置出現

**Two-level Merge（兩層合併演算法）：**

處理 `"information retrieval"` 片語查詢：

1. **第一層**：用 Merge Algorithm 找出**同時包含兩個詞**的文件（合併 docID）
2. **第二層**：在這些文件中，檢查 `information` 的位置 + 1 是否等於 `retrieval` 的位置（合併 position）

**範例：** 在文件 4 中：
- `information` 在位置 37
- `retrieval` 在位置 38（37 + 1 = 38 ✓）→ 是片語！

**也可處理 Proximity Queries（鄰近查詢）：**

如 `information /3 retrieval`（兩詞距離不超過 3）→ 改成檢查 `|pos1 - pos2| ≤ 3`

**Positional Index 的代價：**

- 比非位置索引大 **2-4 倍**
- 約是原始文字大小的 **1/3 ~ 1/2**（非位置索引大約是 10%）

**💡 混合方案：** 常用片語（如 "Michael Jackson"）用 Biword Index、罕見片語用 Positional Index → 速度快且空間省

---

## 🔥 整體邏輯鏈

```text
05：grep 太慢 → Matrix → 但太大太稀疏  （問題）
       ↓
06：改用 Inverted Index（Dictionary + Postings Lists）（解法）
       ↓
07：用雙指標 Merge Algorithm 做 AND 查詢，O(x+y)（基本應用）
       ↓
08：Boolean Retrieval Model + Query Optimization（多詞處理）
       ↓
09：Inverted Index 不夠處理片語 → Positional Index + Two-level Merge（進階）
```