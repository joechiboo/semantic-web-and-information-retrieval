# 期中考範圍 - Midterm

> Slide 1~5 (Course Introduction ~ IR Basics)，共 8 部影片

---

### Week 1 - Course Introduction (課程介紹)

> 開學第一週，剛過完年，沒有同學來。

---

### Week 2 - Information Retrieval & Semantic Networks

- [01 - Introduction to Information Retrieval (資訊檢索導論)](01-introduction-to-information-retrieval.md)
  - https://www.youtube.com/watch?v=kNkCfaH2rxc
  - IR 的定義：從大型非結構化文件集合 (Unstructured Document Collection) 中找到滿足使用者資訊需求 (Information Need) 的資料
  - 應用場景：Web 搜尋、Email 搜尋、企業知識庫 (Enterprise Knowledge Base)、法律檢索 (Legal IR)
  - 基本流程：User Task → Information Need → Query → Search Engine → Results
  - 評估指標：Precision（精確率）與 Recall（召回率）

- [02 - Simple Introduction to Semantic Networks (語意網路簡介)](02-simple-introduction-to-semantic-networks.md)
  - https://www.youtube.com/watch?v=K-yrnyvqXGo
  - 語意網路 = 知識的圖形化表示（Graphical Representation of Knowledge）
  - 節點（Nodes）= 物件/實體、邊（Edges）= 關係
  - 範例：Apple ──is a──→ Fruit、Tom ──is a──→ Cat

---

### Semantic Networks - 補充教材

- [03 - Semantic Networks - Additional Info (語意網路補充資訊)](03-semantic-networks-additional-info.md)
  - https://www.youtube.com/watch?v=3PgIC9KcSNE
  - 繼承（Inheritance）：Tweety → Canary → Bird → Animal
  - 例外處理（Exception Handling）：Penguin 走路而非飛行
  - 優缺點分析

- [04 - Detailed Introduction to Semantic Networks (語意網路詳細介紹)](04-detailed-introduction-to-semantic-networks.md)
  - https://www.youtube.com/watch?v=sY0kbo251A4
  - 語意網路歷史（Quillian, 1966）
  - 四個組成部分：Lexical、Structural、Procedural、Semantics
  - 繼承性質、非二元關係、概念圖（Conceptual Graph）
  - WordNet 簡介與應用

---

### Traditional Information Retrieval -- Basics (傳統資訊檢索基礎)

- [05 - Term-Document Matrices (詞項-文件矩陣)](05-term-document-matrices.md)
  - https://www.youtube.com/watch?v=e81nC0LO0A8
  - 詞項-文件矩陣 (Term-Document Matrix)：行=詞項 (Terms)、列=文件 (Documents)、值=0/1
  - 用向量布林運算 (Vector Boolean Operations) 回答查詢（AND/OR/NOT）
  - 矩陣稀疏性 (Sparsity) 問題：500K×1M = 半兆個元素，但幾乎都是 0

- [06 - The Inverted Index (倒排索引)](06-the-inverted-index.md)
  - https://www.youtube.com/watch?v=Wf6HbY2PQDw
  - 倒排索引 (Inverted Index) 結構：Dictionary（詞典）+ Postings Lists（倒排列表）
  - 索引建構流程：Tokenization（斷詞）→ Normalization（正規化）→ Stemming（詞幹提取）→ Indexing（建立索引）
  - Postings Lists 按 Document ID（文件編號）排序

- [07 - Query Processing with the Inverted Index (使用倒排索引的查詢處理)](07-query-processing-with-inverted-index.md)
  - https://www.youtube.com/watch?v=5KbynCj7yRQ
  - AND 查詢的合併演算法 (Merge Algorithm)（雙指標掃描 / Two-pointer Scan）
  - 時間複雜度 (Time Complexity) O(x + y)，線性於兩個 Postings Lists 長度之和
  - 關鍵：Postings Lists 必須按 Document ID 排序

- [08 - The Boolean Retrieval Model (布林檢索模型)](08-boolean-retrieval-model.md)
  - https://www.youtube.com/watch?v=TIN_02pJU-Y
  - Boolean Retrieval Model 的數學基礎：AND、OR、NOT
  - WestLaw 延伸布林查詢 (Extended Boolean Query)：距離運算子 (Proximity Operator)（/3）、萬用字元 (Wildcard)（!）
  - 查詢最佳化 (Query Optimization)：從文件頻率 (Document Frequency) 最低的詞項開始處理

- [09 - Phrase Queries and Positional Indexes (片語查詢與位置索引)](09-phrase-queries-and-positional-indexes.md)
  - https://www.youtube.com/watch?v=QVVvx_Csd2I
  - Biword Index（雙詞索引）：索引連續兩個詞的組合，字典膨脹 (Dictionary Blowup) 問題
  - Positional Index（位置索引，標準方案）：記錄詞項在文件中的位置 (Position)
  - 兩層合併演算法 (Two-level Merge)：先合併文件 ID，再檢查位置相容性
  - 位置索引大小約為非位置索引 (Non-positional Index) 的 2-4 倍

---

## 核心概念速查

### ⭐ 精確率與召回率 (Precision & Recall)【必考】

#### 公式

| 指標 | 公式 | 白話解釋 |
|------|------|----------|
| **Precision（精確率）** | 正確的結果 / 全部回傳的結果 | 「你給我的東西裡面，有多少是我要的？」 |
| **Recall（召回率）** | 正確的結果 / 全部相關的東西 | 「所有我要的東西，你幫我找到了多少？」 |

#### 範例：車庫裡有 100 隻老鼠，捕鼠器抓到 20 隻東西（15 隻老鼠 + 5 隻蟑螂）

| 指標 | 計算 | 結果 |
|------|------|------|
| Precision | 15 / 20 | 75%（抓到的裡面，多少是老鼠） |
| Recall | 15 / 100 | 15%（全部老鼠裡，抓到了多少） |

#### 對應到搜尋引擎

| 指標 | 搜尋引擎情境 |
|------|-------------|
| Precision | 搜尋結果第一頁 10 筆，7 筆相關 → 70% |
| Recall | 資料庫有 50 篇相關文件，只找到 7 篇 → 14% |

#### Trade-off（兩者的拉扯）

- **提高 Precision**（更精準）→ 條件設嚴格 → 漏掉更多 → Recall ↓
- **提高 Recall**（更完整）→ 條件設寬鬆 → 混入不相關的 → Precision ↓

範例：搜尋 `how trap mice alive`
- 加 `AND humane AND cage` → Precision ↑ 但 Recall ↓（漏掉用其他詞彙的好文章）
- 只搜 `mice` → Recall ↑ 但 Precision ↓（大部分結果無關）

#### 關鍵觀念

**評估原則：** Precision 和 Recall 是相對於使用者的「**資訊需求 (Information Need)**」來評估，而非相對於提交的「查詢 (Query)」。即使搜尋引擎完美執行了查詢，如果查詢本身沒有表達好需求，Precision 一樣會很低。

### 經典搜尋流程 (Classic Search Model)

```
使用者任務 (User Task)
    ↓
資訊需求 (Info Need)
    ↓
查詢 (Query)
    ↓
搜尋引擎 (Search Engine)  ←→  文件集合 (Collection)
    ↓
搜尋結果 (Results)
    ↓
查詢優化 (Query Refinement) → 回到「查詢」步驟
```

### 語意網路基本結構 (Semantic Network Structure)

```
Node (物件) ──Edge (關係)──→ Node (物件)

範例：
Apple ──is a──→ Fruit
Tom ──is a──→ Cat ──is a──→ Mammal ──are──→ Animal
Cat ──likes──→ Cream
Cat ──sat on──→ Mat
```