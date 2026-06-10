# 期末考 Q&A 複習卷

> **考試格式：** 英文出題，可用中文回答（與期中考同）
> **內容來源：** 主要從影片出，較少作業形式
> **涵蓋影片：** 10、11、12、13、14（共 10 題）
> 📅 期末考：2026-06-15

---

## 影片 10 - Introducing Ranked Retrieval

### ⭐ Q1：What is the "Feast or Famine" problem? Why do we need Ranked Retrieval?

**A：**

**Feast or Famine Problem（饗宴或飢荒問題）：**

> Boolean 查詢容易產生**極端結果**：
> - 用 **AND** 連接 → 結果**太少**（甚至 0 個）
> - 用 **OR** 連接 → 結果**太多**（數千甚至更多）

**真實例子（影片裡）：**

```text
Query: standard user Dlink 650
     → 20 萬筆結果（太多）

Query: standard user Dlink 650 no card found
     → 0 筆結果（太少）
```

要寫出**剛好**的查詢需要高度技巧，大多數使用者做不到。

**為什麼需要 Ranked Retrieval？**

> Ranked Retrieval 對每個文件**評分 (Scoring) 0~1**，按分數排序返回，使用者只看前面幾筆，**結果太多也沒關係**。

**關鍵字：**
- **Feast or Famine Problem**
- **Scoring**（0~1 分數）
- **Ranking**（排序）

---

### Q2：What are the key differences between Boolean Retrieval and Ranked Retrieval?

**A：**

| | Boolean Retrieval | Ranked Retrieval |
|--|-------------------|------------------|
| **匹配方式** | Exact Match（要嘛符合，要嘛不符合） | 評分 0~1 |
| **回傳結果** | 集合（set） | 排序清單（ranked list） |
| **查詢語言** | Boolean Query（AND/OR/NOT） | **Free Text Queries**（自然語言） |
| **Feast or Famine** | ❌ 有問題 | ✓ 解決 |
| **適合對象** | 專家使用者 | **一般使用者** |

**重點觀念：**

1. Ranked Retrieval 通常搭配 **Free Text Queries**
2. **Scoring 的基本原則：**
   - 查詢詞**不在**文件 → 分數 = 0
   - 查詢詞出現**越多次** → 分數**越高**
3. Ranked Retrieval 需要**好的評分系統**，才能讓排序前面的真的是好結果

---

## 影片 11 - Scoring with the Jaccard Coefficient

### Q3：What is the Jaccard Coefficient? How is it calculated? What are its limitations?

**A：**

**Jaccard Coefficient 公式：**

```text
Jaccard(A, B) = |A ∩ B| / |A ∪ B|
```

→ **兩個集合的交集 / 聯集**，值在 **0~1** 之間

**計算範例：**

```text
Query Q = {ides, of, march}
Doc 1   = {caesar, died, in, march}

A ∩ B = {march}                            → 1
A ∪ B = {ides, of, march, caesar, died, in} → 6

Jaccard(Q, Doc1) = 1/6 ≈ 0.17
```

**兩個致命限制：**

| 限制 | 說明 |
|------|------|
| **1. 不考慮詞頻 (Term Frequency)** | 一個詞出現 1 次 vs 100 次，Jaccard 給**同樣分數** |
| **2. 不分罕見詞 vs 常見詞** | "the" 和 "quantum" 同樣權重，但 quantum 顯然**更有資訊量** |

→ 這兩個限制就是引出後面 **TF（影片 12）** 和 **IDF（影片 13）** 的原因

---

## 影片 12 - Term-Frequency Weighting

### Q4：What is the Bag of Words model? What are its limitations?

**A：**

**Bag of Words Model（詞袋模型）：**

> 把文件看成「**裝著詞的袋子**」——**不考慮詞序，只考慮詞頻**。

**從向量角度看演進：**

```text
Boolean 時代：[0, 1, 1, 0, 1]   ← Binary Vector，記「有/無」
Bag of Words：[0, 3, 1, 0, 7]   ← Count Vector，記「出現幾次」
```

**致命限制（必背例子）：**

```text
"John is quicker than Mary"  → [John:1, is:1, quicker:1, than:1, Mary:1]
"Mary is quicker than John"  → [John:1, is:1, quicker:1, than:1, Mary:1]
                                ↑↑↑ 完全相同！但意思相反
```

→ **Bag of Words 無法區分這兩個句子**

**為什麼還是用 Bag of Words？**

- 簡單，可以做向量運算
- 雖然失去詞序，但對大部分檢索任務夠用
- 後面（影片 15）會用 **Positional Index** 補救詞序資訊

---

### Q5：Why do we use Log Frequency Weighting instead of raw term frequency? Write the formula

**A：**

**為什麼不用原始 tf？**

**直覺問題：**

| 文件 squirrel 出現次數 | 應該比 1 次相關幾倍？ |
|---------------------|-------------------|
| 1 次 | 基準 |
| 3 次 | 應該更相關 ✓ |
| 30 次 | **應該 30 倍相關嗎？❌** |

**結論：** 相關性隨次數**上升，但不該是線性**。需要**次線性 (Sublinear)** 的縮放方法。

**Log 詞頻加權公式（必背）：**

```text
       ┌  1 + log₁₀(tf)    if tf > 0
w_t,d = ┤
       └  0                if tf = 0
```

**為什麼加 1？**
- 因為 `log(0) = -∞` 會爆炸
- 加 1 讓 tf=1 時 w=1（合理基準）

**為什麼用 log？**
- 製造**次線性增長 (Sublinear Scaling)**
- 次數變多時，加分速度變慢

**權重數字（必記）：**

| tf | w |
|----|---|
| 0 | 0 |
| 1 | 1 |
| 2 | 1.3 |
| **10** | **2** |
| **1000** | **4** |

→ **tf 變 10 倍，w 只多 1**

**文件-查詢評分公式：**

```text
Score(q, d) = Σ  (1 + log₁₀(tf_t,d))
            t ∈ q ∩ d
```

**白話：**
- 只看「查詢和文件**都有**的詞」
- 每個詞算 `1 + log₁₀(tf)`
- 全部加起來 = 這個文件的分數

**特性：** 文件沒有任何查詢詞 → 分數 = 0

---

## 影片 13 - Inverse Document Frequency Weighting

### Q6：What is Inverse Document Frequency (IDF)? Write the formula

**A：**

**核心觀念：** **稀有詞比常見詞更有資訊量**，IDF 用來量化這種差異。

**公式（必背）：**

```text
IDF(t) = log₁₀(N / df_t)

N      = 文件集合的總文件數
df_t   = 包含詞項 t 的文件數
```

**為什麼用 log？** 跟 TF 一樣，避免極端值（如 N=10^6, df=1 時）造成過大影響。

**IDF 數值範例（假設 N = 1,000,000）：**

| df（出現於幾個文件）| IDF |
|------------------|-----|
| 1（極稀有）| **6** |
| 100（稍常見）| 4 |
| 10,000 | 2 |
| 1,000,000（全部都有）| **0**（無區分價值）|

→ **df 越大，IDF 越小**（常見詞不重要）

---

### ⭐ Q7：Distinguish between Term Frequency (TF), Document Frequency (DF), and Collection Frequency (CF). Why is IDF useful?

**A：**

**三種 Frequency 的差別（教授特別提醒易混淆）⚠️：**

| 名稱 | 縮寫 | 計算範圍 | 答的是什麼 |
|------|------|---------|----------|
| **Term Frequency** | **TF** | **單一文件** | 詞 t 在**這篇文件**出現幾次 |
| **Document Frequency** | **DF** | **整個集合** | **幾篇文件**包含詞 t |
| **Collection Frequency** | **CF** | **整個集合** | 詞 t 在**整個集合總共**出現幾次 |

**範例（一個簡單集合）：**

```text
Doc 1: "cat cat dog"
Doc 2: "cat bird"
Doc 3: "dog dog dog"

對「cat」這個詞：
  TF(cat, Doc 1) = 2  ← 在 Doc 1 出現 2 次
  TF(cat, Doc 2) = 1
  TF(cat, Doc 3) = 0

  DF(cat) = 2         ← Doc 1 和 Doc 2 有 cat（2 篇）
  CF(cat) = 3         ← 整個集合總共出現 3 次（2+1+0）
```

**速記口訣：**

> **TF = 在哪篇出現幾次**（單篇）
> **DF = 幾篇有**（集合）
> **CF = 總共幾次**（集合）

---

**為什麼 IDF 有用？**

IDF 是用 **DF** 算的：`IDF = log₁₀(N / DF)`

1. **罕見詞（如 quantum）→ IDF 高**，是好的「鑑別詞」
2. **常見詞（如 the）→ IDF 接近 0**，幾乎不影響評分
3. **解決 Jaccard 的問題**：不再把 "the" 跟 "quantum" 當同樣重要

**重要特性：** IDF 對**單一詞項查詢**無影響

> 因為 IDF 只是對所有文件**統一縮放**，不改變排序。
> **IDF 只在多詞查詢時才發揮作用**（區分查詢中不同詞的重要性）

---

**為什麼用 DF 不用 CF？**

DF 和 CF 都是「集合層級」的統計，但**用途不同**：

| | Document Frequency (DF) | Collection Frequency (CF) |
|--|-------------------------|---------------------------|
| 定義 | 包含詞 t 的**文件數** | 詞 t 在集合中**出現的總次數** |

**經典對比範例：**

| 詞 | 分佈特性 | DF | CF |
|----|---------|-----|-----|
| **try** | 很多文件都有，但每篇只 1 次 | **高** | **高** |
| **insurance** | 集中在保險文件，每篇出現多次 | **低** | **高** |

→ **DF 比 CF 更適合用於檢索**：

- CF 看不出「廣泛但淺薄」vs「集中且深入」的差別
- DF 能區分這兩種詞，更能反映「鑑別力」

---

## 影片 14 - TF-IDF Weighting

### ⭐ Q8：Write the TF-IDF formula. Why is it the most famous weighting scheme?

**A：**

**TF-IDF 公式（必背！期末考必考）：**

```text
TF-IDF(t, d) = (1 + log₁₀ tf_t,d) × log₁₀(N / df_t)
             ─────────────┬────── × ─────────┬──────
                  TF 部分              IDF 部分
```

**⚠️ 注意：** 中間的 `-` 是**連字號 (hyphen)**，不是減號！TF 和 IDF 之間是**相乘**，不是相減。

**為什麼是最重要的加權方案？**

> 「**如果你只能學一個 IR 加權方法，就是 TF-IDF**」（Manning 原話）

**TF-IDF 兩大特性：**

1. **權重隨詞在文件出現次數增加而增加**（來自 TF）
2. **權重隨詞在集合中的稀有度增加而增加**（來自 IDF）

→ 結合了「**這個詞在這個文件多重要**」+「**這個詞整體多稀有**」

**解決了 Jaccard 的兩個問題：**

| Jaccard 限制 | TF-IDF 解決方式 |
|-------------|-----------------|
| 不考慮詞頻 | TF 部分搞定 |
| 不分罕見/常見 | IDF 部分搞定 |

---

### Q9：How do we score a document using TF-IDF for a multi-term query?

**A：**

**評分公式：**

```text
Score(q, d) = Σ  TF-IDF(t, d)
            t ∈ q ∩ d
```

**步驟：**

1. 找出查詢和文件**共有**的詞 (t ∈ q ∩ d)
2. 對每個共有詞，算 **TF-IDF(t, d)**
3. 全部加總 = 該文件對查詢的分數

**範例（簡化版）：**

```text
Query:    "best car insurance"
Doc 1:    "car insurance auto insurance" (有 car, insurance)

共有詞：car, insurance

假設：
  car:        tf=1, df=18,000   → TF-IDF = (1+0) × log(10^6/18000) ≈ 1.7
  insurance:  tf=2, df=10,000   → TF-IDF = (1+0.3) × log(10^6/10000) ≈ 2.6

Score(q, Doc1) = 1.7 + 2.6 = 4.3
```

**向量表示演進（重要觀念）：**

```text
Boolean：  Binary Vector  [0, 1, 1, 0]     ← 0/1
TF：       Count Vector   [0, 3, 7, 0]     ← 自然數
TF-IDF：   Weight Vector  [0, 2.6, 1.7, 0] ← 實數值 ⭐
```

→ 每個文件變成一個**實數值向量**，整個文件集合是**實數值的詞項-文件矩陣**

---

### Q10：Trace the evolution from Jaccard to TF-IDF

**A：**

整個 Ranked Retrieval 加權方案的演進：

```text
1️⃣ Jaccard Coefficient
   公式：|A ∩ B| / |A ∪ B|
   問題：不考慮詞頻、不分罕見/常見

         ↓ 解決「不考慮詞頻」

2️⃣ Term Frequency (TF)
   公式：w = 1 + log₁₀(tf)
   進步：考慮詞頻，用 log 做次線性縮放
   剩問題：還是不分罕見/常見

         ↓ 解決「不分罕見/常見」

3️⃣ Inverse Document Frequency (IDF)
   公式：log₁₀(N / df)
   進步：罕見詞高分、常見詞低分
   特點：只在多詞查詢時有用

         ↓ TF 和 IDF 合體

4️⃣ TF-IDF Weighting ⭐
   公式：(1 + log₁₀ tf) × log₁₀(N/df)
   結合：詞頻 × 稀有度
   結果：IR 最經典的加權方案
```

**核心串聯：**

> **Jaccard 太簡單 → 加 TF 考慮詞頻 → 再加 IDF 區分稀有度 → 合體變 TF-IDF**

**每階段解決的問題：**

| 階段 | 文件向量 | 解決的問題 |
|------|---------|----------|
| Boolean | Binary [0,1] | （無評分，引出 Ranked）|
| Jaccard | Set | 開始有評分 |
| TF | Count Vector | 詞頻多 = 更相關 |
| IDF | （只是縮放係數）| 稀有詞 = 更重要 |
| **TF-IDF** | **Weight Vector（實數值）** | **詞頻 + 稀有度合體** |