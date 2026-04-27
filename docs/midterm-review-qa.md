# 期中考 Q&A 複習卷

> **考試格式：** 英文出題，可用中文回答。英文看不懂可問教授。
> 涵蓋影片：01、05、06、07、08（共 10 題）
> ⚠️ 02（語意網路）不考，本卷已移除
> ⚠️ 08 的 WestLaw 與歷史內容不考

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

**前處理：**

```text
原始文件
  ↓
Tokenization（斷詞）：[Friends] [Romans] [countrymen]
  ↓
Normalization（正規化）：統一大小寫
  ↓
Stemming（詞幹提取）：去掉字尾
  ↓
（可選）Stop Words：去除 the、a、of 等
```

**建索引三步驟：**

1. **標上文件 ID**：每個 token 記錄來自哪個文件
2. **排序**：主鍵=詞字母順序、次鍵=文件 ID
3. **合併 (Consolidation)**：同文件重複合併、同詞組成 Postings List

**💡 重點：** 排序是最花時間的步驟，但排完後 Postings List 自然按 Doc ID 排好。

---

## 影片 07 - Query Processing with Inverted Index

### Q7：Write the INTERSECT algorithm for AND query

**A：**

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

**時間複雜度：** **O(x + y)**

---

### Q8：Why must postings lists be sorted by Document ID?

**A：**

**排序是 Merge Algorithm 達到 O(x + y) 的關鍵。**

| | 有排序 | 沒排序 |
|--|--------|--------|
| 演算法 | 雙指標掃描 | 巢狀迴圈 |
| 時間複雜度 | **O(x + y)** | O(x × y) |

**對比：** x = y = 1000

- 有排序：2000 次
- 沒排序：1,000,000 次

**💡 因此 Inverted Index 建構時就要把 Postings List 排序好（影片 06 第 2 步），讓查詢能跑得快。**

---

## 影片 08 - The Boolean Retrieval Model

### Q9：What is the Boolean Retrieval Model? Explain Query Optimization for AND queries

**A：**

**Boolean Retrieval Model：**

> 一種資訊檢索模型，使用者用 **Boolean 運算子**（AND / OR / NOT）組合詞項，文件「精確匹配」或「不匹配」這個布林表達式，沒有排名。

**運算子：**

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

### Q10：Adapt the merge algorithm for `A AND NOT B` and `A OR NOT B`

**A：**

#### A AND NOT B（在 A 但不在 B）

**真值表：**
| in_A | in_B | A AND NOT B | 包含 |
|------|------|-------------|------|
| T | T | F | ✗ |
| T | F | T | ✓ |
| F | T | F | ✗ |
| F | F | F | ✗ |

**演算法（O(x + y)，類似 INTERSECT）：**

```csharp
List<int> AND_NOT(List<int> ListA, List<int> ListB)
{
    List<int> result = new List<int>();
    int i = 0, j = 0;
    while (i < ListA.Count && j < ListB.Count)
    {
        if (ListA[i] == ListB[j]) { i++; j++; }      // 兩邊都有 → 不加
        else if (ListA[i] < ListB[j])
        {
            result.Add(ListA[i]);                     // 在 A 不在 B → 加
            i++;
        }
        else j++;                                     // 在 B 不在 A → 跳過
    }
    while (i < ListA.Count) result.Add(ListA[i++]);  // ⚠️ 收尾：A 剩下的都加
    return result;
}
```

#### A OR NOT B（在 A 或不在 B）

**真值表：**
| in_A | in_B | A OR NOT B | 包含 |
|------|------|------------|------|
| T | T | T | ✓ |
| T | F | T | ✓ |
| F | T | F | ✗ |
| F | F | T | ✓ ← 關鍵 |

**演算法（O(N)，必須走全部 N 個文件）：**

```csharp
List<int> OR_NOT(List<int> ListA, List<int> ListB, int N)
{
    List<int> result = new List<int>();
    int i = 0, j = 0;
    for (int d = 1; d <= N; d++)
    {
        bool in_A = (i < ListA.Count && ListA[i] == d);
        bool in_B = (j < ListB.Count && ListB[j] == d);
        if (in_A || !in_B) result.Add(d);
        if (in_A) i++;
        if (in_B) j++;
    }
    return result;
}
```

**💡 OR NOT 為何需要 N？** 因為「F F」的文件（兩邊都沒有）也要包含，必須走全部才看得到。

#### 三種操作對比

| 操作 | 條件 | 需要 N？ | 複雜度 |
|------|------|---------|--------|
| AND (INTERSECT) | `in_A && in_B` | ✗ | O(x+y) |
| AND NOT | `in_A && !in_B` | ✗ | O(x+y) + 收尾 |
| **OR NOT** | `in_A \|\| !in_B` | **✓** | **O(N)** |

---

## 🔥 整體邏輯鏈

```text
05：grep 太慢 → Matrix → 但太大太稀疏  （問題）
       ↓
06：改用 Inverted Index（Dictionary + Postings Lists）（解法）
       ↓
07：用雙指標 Merge Algorithm 做 AND 查詢，O(x+y)（基本應用）
       ↓
08：Boolean Retrieval Model + Query Optimization
    + Merge 演算法擴充：AND NOT、OR NOT（進階應用）
```