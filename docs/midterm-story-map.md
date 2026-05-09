# 期中考 Story Map — 資料結構演化全景

> **用途：** 把 10 題 Q&A 串成一個完整故事，看清楚每題在整個敘事中的位置。
> **適用：** 想理解「為什麼會發展出這個資料結構/演算法」的全局複習。
> **配套檔案：** `midterm-review-qa.md`（10 題詳解）、`00-midterm-summary.md`（章節摘要）

---

## 整體故事線

> **「我有一大堆文件，使用者想找東西，怎麼辦？」**
>
> 這是 IR 的核心問題。整個期中考範圍就是在回答這個問題，從**最笨的方法**逐步演化到**現代搜尋引擎的核心技術**。

---

## 五幕劇 — 全景時間軸

```
              [問題]                  [解法]                    [代價/限制]
影片 05:  ① grep 線性掃描太慢    →  ② Term-Document Matrix  →  半兆 cells / 99% 是 0
                                                                    │
                                                                    ↓ 觀察：只記 1 的位置
影片 06:  ③ 矩陣太大太稀疏      →  ④ Inverted Index         →  需要 Tokenize/Normalize/
              (sparse)              (Dictionary + Postings)      Stem/StopWord 前處理
                                                                    │
                                                                    ↓ 為了讓查詢更快
影片 07:  ⑤ AND 查詢怎麼做      →  ⑥ Postings 排序 +         →  必要前提:Postings
                                      INTERSECT 雙指標            必須按 docID 排序
                                                                    │
                                                                    ↓ 多詞 / 模型化
影片 08:  ⑦ 多詞 AND 順序很重要 →  ⑧ Boolean Model +         →  仍只能精確匹配,
                                      Query Optimization          沒有 ranking
                                      (從 doc freq 最低開始)         │
                                                                    ↓ 但無法處理「相鄰」
影片 09:  ⑨ 片語查詢無法處理    →  ⑩a Biword Index          →  ✗ False Positive
              (無位置資訊)                                          ✗ 字典爆炸 O(n²)
                                                                    │
                                                                    ↓ 標準解法
                                  ⑩b Positional Index       →  比非位置索引大 2-4 倍
                                      + Two-level Merge          (約原文 1/3~1/2)
                                                                    │
                                                                    ↓ 工程最佳化
                                  ⑩c Hybrid Index           →  常見片語用 Biword、
                                      (Melbourne 2004)           罕見用 Positional
                                                                  → 4× 速度，+26% 空間
```

---

## 五個演化階段（詳細展開）

### 🔵 階段 1：grep 線性掃描（被淘汰的 baseline）

**做法：** Unix 的 `grep`，逐字元/逐行掃描所有文件。

**為什麼小規模可以？** 莎士比亞全集很小，硬碟一秒掃完。

**為什麼大規模不行？4 個致命缺點：**

| # | 問題 | 例子 |
|---|------|------|
| 1 | **Linear Scan 太慢** | 整個 web 一次掃一遍？不可能 |
| 2 | **NOT 不好實作** | grep 找「不包含」要負向 flag，效率差 |
| 3 | **無法做 Proximity Search** | 「Romans 在 countrymen 附近」grep 做不到 |
| 4 | **無法 Ranking** | 只能說「有/沒有」，不能說「最相關的是哪幾筆」 |

> 💡 **記憶口訣：「慢、否、近、排」** — 慢、否定難、鄰近做不到、無法排名

---

### 🔵 階段 2：Term-Document Matrix（概念上很美，實作上不可行）

**結構：**

```
            Antony   Julius   The      Hamlet   Othello  Macbeth
            and      Caesar   Tempest
            Cleopatra
Antony      1        1        0        0        0        1
Brutus      1        1        0        1        0        0
Caesar      1        1        0        1        1        1
Calpurnia   0        1        0        0        0        0
Cleopatra   1        0        0        0        0        0
mercy       1        0        1        1        1        1
worser      1        0        1        1        1        0
```

**布林查詢怎麼做？**

`Brutus AND Caesar AND NOT Calpurnia`：
1. 取 `Brutus` 的 row 向量：`110100`
2. 取 `Caesar` 的 row 向量：`110111`
3. 取 `Calpurnia` 的 row 向量：`010000`，**取補集** → `101111`
4. 三個向量做 AND（bit-wise）：`100100`
5. 對應到文件 1 (Antony & Cleopatra) 和文件 4 (Hamlet) → 答案

**規模問題（必背數字）：**

| 參數 | 數字 | 符號 |
|------|------|------|
| 文件數 | 1,000,000 | **N** |
| 平均文件長度 | 1,000 詞 | — |
| 每詞平均 bytes | 6 bytes | — |
| 文件總大小 | 6 GB | — |
| 不同詞項數 | 500,000 | **M** |
| **矩陣大小** | **N × M = 半兆 (5×10¹¹) cells** | — |

**稀疏性 (Sparsity)：**
- 矩陣最多有 **10 億 (10⁹) 個 1**（因為 1M docs × 1000 詞 = 10⁹ tokens）
- 半兆 cells 中，**99.8%+ 是 0**
- → **巨大浪費**

**核心觀察（引出下一階段）：**
> **「我們應該只記錄 1 的位置，不要存 0」** ← 這就是 Inverted Index 的起源

---

### 🔵 階段 3：Inverted Index（現代 IR 的基石）

**核心點子：** 把矩陣的每一**行**（某個詞的出現分布）改用**只記 docID 的 list** 表示。

#### 3a. 為什麼用「可變長度 List」而不是「固定陣列」？

| 詞 | 出現文件數 |
|----|------------|
| `the` | 幾乎所有文件 |
| `Calpurnia` | 1 個文件 |

→ 固定陣列要嘛浪費（短的詞填一堆空位），要嘛不夠用。
→ 而且**動態加入新文件**時，固定陣列要重新分配，可變 list 容易擴充。

#### 3b. 結構雙層：Dictionary（左）+ Postings（右）

```
┌─────────────────────┐         ┌──────────────────────────┐
│  Dictionary         │         │  Postings Lists          │
│  (relatively small) │         │  (large)                 │
│                     │         │                          │
│  Term     | df      │         │                          │
│  ─────────┼─────    │         │                          │
│  Brutus   |  2  ────┼────────→│  [1, 4]                  │
│  Caesar   |  4  ────┼────────→│  [1, 2, 4, 6]            │
│  Calpurnia|  1  ────┼────────→│  [2]                     │
│  ...                │         │                          │
│                     │         │                          │
│  📍 IN MEMORY       │         │  📍 ON DISK              │
└─────────────────────┘         └──────────────────────────┘
   ~500K 個詞項                     上限 ~10 億筆 (1M×1000)
   壓縮：共用前綴                   壓縮：只存 docID 差值
```

**關鍵術語：**
- 一筆 `(term, docID)` 對 = **a Posting**（單數）
- 所有 Postings Lists 的總和 = **the Postings**（集合名詞）

**為什麼 Dictionary 在記憶體、Postings 在硬碟？**
- Dictionary 小，每次查詢都要查 → 必須在 RAM
- Postings 大，但每次查詢只要讀**少數幾個**詞的 list → 放硬碟，需要時連續讀進來（**continuous run** 是高效硬碟存取的關鍵）

#### 3c. ⭐ 必考：Postings List 按 docID 排序
> 這是為了**下一階段的 INTERSECT 雙指標演算法**鋪路。

#### 3d. 索引建構流程（5 階段）

```
原始文件
   │
   ▼
① Tokenization（斷詞）
   • 處理標點：John's → John ? John's ?
   • 處理連字號：state-of-the-art → 一個詞還是四個？
   │
   ▼
② Normalization（正規化）
   • 大小寫統一：USA = U.S.A. = usa
   • 同義拼法統一
   │
   ▼
③ Stemming（詞幹還原）
   • authorize, authorization → author
   • friends → friend
   │
   ▼
④ Stop Words（停用詞，可選）
   • 移除 the, a, of, to...
   • ⚠️ 現代系統常常保留（例：搜尋「To Be Or Not To Be」需要這些詞）
   │
   ▼
⑤ Indexing（建索引核心 3 步）
   ┌─────────────────────────────────┐
   │ a. 標 docID：每個 token 標來源  │
   │ b. SORT：主鍵=詞、次鍵=docID    │  ← 最花時間
   │ c. MERGE：同詞同文件去重複，    │
   │    同詞跨文件組成 Postings List │
   └─────────────────────────────────┘
   → Postings List **自然就按 docID 排好了**
```

---

### 🔵 階段 4：Boolean Retrieval Model + Query Optimization

**Boolean Retrieval Model：**
- 用戶用 AND / OR / NOT 組合詞
- 文件「精確匹配」或「不匹配」，**沒有 ranking**

**INTERSECT 雙指標（影片 07，AND 查詢的核心）：**

```
p1: [1, 4, 8, 16, 32]
p2: [2, 4, 8, 16, 64]
       ↑      ↑

雙指標掃描：
  相等  → 加入結果，兩指標都動
  p1<p2 → 只動 p1
  p2<p1 → 只動 p2

時間複雜度：O(x + y)
若沒排序：O(x × y) — 1000×1000 = 1,000,000 次（vs 排序後 2000 次）
```

**Query Optimization（影片 08）：**
- 多詞 AND 查詢時，**從 doc freq 最低的詞開始**
- 例：`Brutus(1M) AND Caesar(1M) AND Calpurnia(1K)`
  → 從 Calpurnia 開始 → 最快縮小範圍
- 為什麼可行？Dictionary 已經存了 doc freq，O(1) 查得到

**Boolean Model vs Ranked Model：**

| 比較項 | Boolean Model（期中） | Ranked Model（期末） |
|--------|----------------------|---------------------|
| 結果 | 「符合」或「不符合」二元 | 每份文件給一個分數 |
| 排序 | ❌ 沒有排名 | ✅ 按相關性排序 |
| 結果數量 | 要嘛 0，要嘛爆量 | 永遠回傳「最相關的前 K 名」 |
| 使用者門檻 | 高（要會寫布林表達式） | 低（自然語言查詢） |
| 典型應用 | 法律檢索（WestLaw）、企業搜尋 | Google、Bing |

---

### 🔵 階段 5：Phrase Queries — Inverted Index 的不足

**問題場景：** 搜尋 `"information retrieval"`（要求兩詞**相鄰**）
- 用標準 Inverted Index：只能知道兩個詞**都在某文件**
- 但「I went to **university** at Stanford for **information**」也會誤中
- → **沒有位置資訊**

#### 5a. 第一次嘗試：Biword Index（不是標準解法）

**做法：** 把每對相鄰詞當成一個 dictionary entry

```
原文：Friends, Romans, Countrymen

biword               →  postings
─────────────────────────────────
"friends romans"     →  [17, 33]
"romans countrymen"  →  [17, 92]
```

**處理長片語：** 拆成多個 biword 做 AND
- `"stanford university palo alto"`
  → `"stanford university"` AND `"university palo"` AND `"palo alto"`

**兩個問題：**

| # | 問題 | 嚴重度 |
|---|------|--------|
| 1 | **False Positives** | 中 — 拆解後可能匹配到實際不連續的片語 |
| 2 | ⚠️ **Dictionary Blowup（字典爆炸）** | 高 — 字典變成 **詞數²** 規模 |

→ Triword、Quadword 索引完全不可行 → **Biword 不是標準解法**

#### 5b. 標準解法：Positional Index

**做法：** Postings 中除了 docID，**還記錄該詞在文件中的位置**

```
be → 993,427 documents;
     <docID, [positions]>
     1: ⟨7, 18, 33, 72, 86, 231⟩;
     2: ⟨3, 149⟩;
     4: ⟨17, 191, 291, 430, 434⟩;
     5: ⟨363, 367⟩
```

**Two-level Merge（兩層合併演算法）：**

```
查詢：「information retrieval」

第一層（外層）：Merge docID
   找出 information 和 retrieval 都出現的文件

第二層（內層）：Merge position
   在每個共同文件中，找
   pos(retrieval) == pos(information) + 1
```

**範例：** 文件 4 中
- `information` 在位置 37
- `retrieval` 在位置 38（37+1=38 ✓）→ 是片語！

**也可處理 Proximity Query：**
- `information /3 retrieval` → 改成檢查 `|pos1 - pos2| ≤ 3`
- ✨ Biword Index **完全做不到**這個

**位置索引的代價：**

| 比較項 | 非位置索引 | 位置索引 |
|--------|-----------|---------|
| 大小 vs 原文 | ~10% | ~33%~50% |
| 倍數 | 1× | **2-4×** |
| 受文件長度影響 | 否 | 是（長文影響大） |

#### 5c. 工程最佳化：Hybrid Index（Melbourne 2004）

**直覺：** 常被查的片語每次都做 Two-level Merge 太浪費（例：`Michael Jackson`、`The Who`）

**做法：** 兩種索引合用
- **常見片語**（如 "Michael Jackson"）→ 預先建 **Biword Index**
- **罕見片語** → 走 **Positional Index** 兩層合併

**結果（必記數字）：**
- ⚡ 查詢時間 = 純位置索引的 **1/4**（4 倍快）
- 💾 空間多 **+26%**

**現代延伸：** 動態快取常被查的片語的交集結果（dynamic cache）

---

## 🔗 三條串起整個故事的「引線」

理解這三條引線，10 題就是同一個故事的不同切面。

### 引線 1：資料結構的演化
```
Term-Document Matrix（Q4）
    ↓ 太大太稀疏
Inverted Index（Q5, Q6）
    ↓ 不能處理片語
Positional Index（Q10）
```

### 引線 2：查詢處理的演化
```
單詞查詢
    ↓
AND 查詢 → INTERSECT 雙指標（Q7）
    ↓
多詞 AND → Query Optimization（Q8）
    ↓
片語查詢 → Two-level Merge（Q10）
```

### 引線 3：評估與設計目標
```
Precision / Recall（Q3）—— 衡量好壞
    ↓
Information Need vs Query（Q1, Q2）—— 評估基準
    ↓
所有資料結構設計都是為了：又快、又準、又能 scale
```

---

## 🎯 三個易考的轉折點（背起來等於分數）

### 轉折 1：為什麼從 Matrix 走到 Inverted Index？
> **「矩陣 99% 是 0，只記 1 的位置就好」** — 利用稀疏性 (sparsity)

### 轉折 2：為什麼 Postings 要排序？
> **「為了 INTERSECT 雙指標 O(x+y) 線性查詢」** — 不排序就是 O(x×y) 慢千倍

### 轉折 3：為什麼從 Biword 走到 Positional？
> **「Biword 字典爆炸 O(n²)，且做不到 proximity；Positional 用空間換功能」**

---

## 🎯 考試題型分類

| 題型 | 對應題目 | 答題策略 |
|------|---------|---------|
| **定義題** | Q1, Q4, Q5, Q8, Q9, Q10 | 寫關鍵詞 + 一句話解釋 |
| **流程題（畫圖）** | Q2, Q5, Q6 | 一定要畫圖 + 標每階段名稱 |
| **計算題** | Q3 | 公式 + 代入例子 |
| **演算法題** | Q7 | 寫 pseudocode + 解釋複雜度 |
| **比較題** | Q9 vs Q10 | 表格對比優缺點 |
