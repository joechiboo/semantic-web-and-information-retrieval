# 期中考 Q&A 複習卷

> **考試格式：** 英文出題，可用中文回答。英文看不懂可問教授。
> 以問答題 (Essay Question) 格式整理，模擬考試作答方式
> 涵蓋影片：01、02、05、06、07（共 10 題）

---

## 影片 01 - Introduction to Information Retrieval (資訊檢索導論)

### ⭐ Q1：What is Information Retrieval (IR)?【必考】

**中：** 什麼是 Information Retrieval (IR)？

**A：**

> Information Retrieval 是從儲存於電腦中的**大型集合 (Large Collections)** 裡，找到能滿足使用者**資訊需求 (Information Need)** 的**非結構化文件 (Unstructured Documents)**（通常為文字）。

**三個關鍵詞要寫到：**

1. Large Collections（大型集合）
2. Information Need（資訊需求）
3. Unstructured Documents（非結構化文件）

**💡 延伸可以補充：** 應用場景如 Web Search、Email Search、企業知識庫、法律檢索

---

### ⭐ Q2：Describe the Classic Search Model【必考，可能要畫圖】

**中：** 描述 Classic Search Model（經典搜尋模型）

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

**具體範例：**

| 階段 | 內容 |
|------|------|
| User Task | 用人道方式趕走車庫的老鼠 |
| Information Need | 不殺死老鼠的方式移走牠們 |
| Query | `how trap mice alive` |

**要能描述的關鍵觀念：**

1. 每層「翻譯」都可能丟失資訊（Task → Need → Query）
2. Query Misformulation（查詢表述不佳）會降低結果品質
3. 搜尋是**迭代過程 (Iterative Process)**，使用者會根據結果修正查詢
4. **評估基準是 Information Need，不是 Query**

---

### Q3：What are Precision and Recall? How are they calculated?

**中：** Precision 和 Recall 分別是什麼？如何計算？

**A：**

| 指標 | 公式 | 白話解釋 |
|------|------|----------|
| **Precision（精確率）** | 正確的結果 / 全部回傳的結果 | 「你給我的東西裡面，有多少是我要的？」 |
| **Recall（召回率）** | 正確的結果 / 全部相關的東西 | 「所有我要的東西，你幫我找到了多少？」 |

**範例：** 車庫裡有 100 隻老鼠，捕鼠器抓到 20 隻（15 老鼠 + 5 蟑螂）

- Precision = 15 / 20 = 75%
- Recall = 15 / 100 = 15%

**💡 考試可能追問：**

- **Trade-off**：提高 Precision 會降低 Recall，反之亦然
- **評估基準**：相對於 Information Need，不是 Query

---

## 影片 02 - Simple Introduction to Semantic Networks (語意網路簡介)

### Q4：What is a Semantic Network? Explain Nodes, Edges, and Arcs

**中：** 什麼是語意網路？Node、Edge、Arc 是什麼？

**A：**

> Semantic Network 是一種**知識 (Knowledge) 的圖形化表示 (Graphical Representation)**，使用由互相連接的**節點 (Nodes)** 和**弧 (Arcs)** 所構成的**有向圖 (Directed Graph)** 來表示知識。

**基本組成：**

| 元素 | 說明 |
|------|------|
| **Node（節點）** | 代表物件 (Object) 或實體 (Entity)，如 Apple、Tom、Cat |
| **Edge（邊）** | 無方向的連線，用於無向圖 (Undirected Graph) |
| **Arc（弧）** | 有方向的連線（帶箭頭），用於有向圖 (Directed Graph) |

**範例（語意網路用 Arc，因為關係有方向性）：**

```text
Apple ──is a──→ Fruit
Tom ──is a──→ Cat ──likes──→ Cream
Cat ──sat on──→ Mat
```

**💡 Edge vs Arc：**

- `Fruit ──is a──→ Apple` ✗（水果不是蘋果，方向錯）
- 所以語意網路用的是有方向的 Arc，不是無方向的 Edge

---

### Q5：What are the advantages and disadvantages of Semantic Networks?

**中：** 語意網路的優缺點？

**A：**

| 優點 (Advantages) | 缺點 (Disadvantages) |
| ------------------ | --------------------- |
| 彈性且易於視覺化 | 不是完整的知識表示方式 (Not a complete knowledge representation) |
| 自然的知識表示方式 | 缺乏操作性知識 (Lacks operational knowledge) |
| 透明傳達意義，無歧義 | 無法表示程序或步驟的重要性 (Cannot represent procedures) |
| 可使用演繹推理 (Deductive Reasoning) 和繼承 (Inheritance) | |
| 可靈活新增新節點 | |

**💡 記法：**

- 優點 = 「容易用、容易畫、容易理解」
- 缺點 = 「表達能力有限，尤其無法講『怎麼做』」

---

## 影片 05 - Term-Document Matrices (詞項-文件矩陣)

### Q6：What is a Term-Document Matrix? Why is it impractical for large collections?

**中：** 什麼是詞項-文件矩陣？為什麼對大型集合不實用？

**A：**

**定義：** Term-Document Matrix 是一個布林矩陣 (Boolean Matrix)：

- **列 (Rows)** = 詞項 (Terms)
- **行 (Columns)** = 文件 (Documents)
- **值 (Values)** = 0 或 1（該詞是否出現在該文件）

**範例：** 莎士比亞劇本 + 查詢 `Brutus AND Caesar AND NOT Calpurnia`

→ 取出每個詞的向量，做 AND / NOT 布林運算，就能找到答案

**為什麼不實用（規模問題 + 稀疏性）：**

假設有 100 萬文件 × 50 萬詞項：

- 矩陣有**半兆 (500K × 1M)** 個格子
- 但 1s 最多只有 10 億個（文件平均 1000 詞 × 100 萬文件）
- **絕大多數格子是 0，極度稀疏 (Sparse)**
- 儲存這麼大的矩陣不划算

**grep 為什麼也不行？**

1. 線性掃描太慢 (Linear Scan)
2. NOT 查詢不好實作
3. 無法做鄰近搜尋 (Proximity Search)
4. 無法做排名 (Ranking)

**💡 結論：** 這個矩陣是重要的**概念性資料結構**，但實作上要用更好的方式 → **Inverted Index**

---

## 影片 06 - The Inverted Index (倒排索引)

### Q7：What is an Inverted Index? Describe its structure

**中：** 什麼是倒排索引？它的結構是什麼？

**A：**

**定義：** Inverted Index 是一種資料結構，對每個詞項記錄它出現在哪些文件，利用矩陣的稀疏性達成高效儲存和檢索。

**類比：** 就像**課本後面的索引頁**——從「詞」查「在哪些文件」。

**兩側結構：**

```text
      左側（Dictionary）              右側（Postings Lists）
  ┌────────────────────┐        ┌──────────────────┐
  │ 詞項 + 文件頻率     │  →→→  │ 文件 ID 列表      │
  │ (Terms + doc freq) │Pointers│ (Lists of docIDs) │
  ├────────────────────┤        ├──────────────────┤
  │ brutus   2         │   →    │ [1, 2]           │
  │ caesar   2         │   →    │ [1, 2]           │
  │ capitol  1         │   →    │ [1]              │
  └────────────────────┘        └──────────────────┘
  相對小，放記憶體 (Memory)       非常大，放硬碟 (Disk)
```

**關鍵特性：**

- **Postings List 按 Document ID 排序**（為後續 Merge Algorithm 做準備）
- Dictionary 和 Postings 存在不同地方（記憶體 vs 硬碟）

---

### Q8：Describe the Inverted Index building process

**中：** 描述倒排索引的建構流程

**A：**

**前處理：**

```text
原始文件
  ↓
Tokenization（斷詞）：切成 [Friends] [Romans] [countrymen]
  ↓
Normalization（正規化）：統一大小寫 → [friends] [romans] [countrymen]
  ↓
Stemming（詞幹提取）：去掉字尾 → [friend] [roman] [countryman]
  ↓
（可選）Stop Words 處理：去除 the、a、of 等常見詞
```

**建索引三步驟：**

1. **標上文件 ID**：每個 token 記錄來自哪個文件
   - 例：`(cat, 1)`, `(like, 1)`, `(cat, 2)`, `(dog, 2)`

2. **排序**：
   - 主鍵：詞的字母順序
   - 次鍵：文件 ID

3. **合併 (Consolidation)**：
   - 同文件內的重複項合併（cat 在文件 2 出現 2 次 → 只留 1 筆）
   - 同詞的所有文件組成 Postings List

**💡 重點：** 排序是最花時間的步驟，但排完後 Postings List 自然就按 Document ID 排好，為下一步（Merge Algorithm）做準備。

---

## 影片 07 - Query Processing with Inverted Index (使用倒排索引的查詢處理)

### Q9：Write the INTERSECT algorithm for AND query on two postings lists

**中：** 寫出兩個 Postings Lists 做 AND 查詢的合併演算法 (Merge Algorithm)

**A：**

**虛擬碼 (Pseudocode)：**

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

**核心概念（雙指標掃描 Two-pointer Scan）：**

- 兩個指標同時掃描兩個排序好的 Postings Lists
- 比對當前 Document ID：
  - **相等** → 加入結果，兩個指標都往前
  - **p1 較小** → 只動 p1
  - **p2 較小** → 只動 p2
- 任一指標到底就結束

**時間複雜度：** O(x + y)，x、y 為兩個 Postings Lists 的長度

---

### Q10：Why must postings lists be sorted by Document ID?

**中：** 為什麼 Postings Lists 必須按 Document ID 排序？

**A：**

**排序是 Merge Algorithm 能達到 O(x + y) 線性時間的關鍵。**

**有排序：** 用雙指標掃描，每次移動較小的那個指標，一次掃過就完成
→ **時間複雜度 O(x + y)**

**沒排序：** 每個 p1 都要跟整個 p2 列表比對，變成巢狀迴圈
→ **時間複雜度 O(x × y)**

**對比範例：**

| Posting Lists 長度 | 有排序 O(x+y) | 沒排序 O(x×y) |
|-------------------|---------------|---------------|
| x = 1000, y = 1000 | 2000 次 | 1,000,000 次 |

**💡 所以 Inverted Index 的建構階段就要把 Postings List 排序好（影片 06 的第 2 步排序），這樣影片 07 的查詢才能跑得快。**

---

## 🔥 整體邏輯鏈（考試串聯記憶）

```text
影片 05：grep 太慢 → 用 Matrix → 但太大太稀疏  （問題）
            ↓
影片 06：改用 Inverted Index（Dictionary + Postings Lists）（解法）
            ↓
影片 07：用雙指標 Merge Algorithm 做 AND 查詢，O(x+y) （應用）
```

這三部是**一條邏輯鏈**，考試可能會問：「為什麼從 X 改到 Y？」或「解釋這整個演進過程」。