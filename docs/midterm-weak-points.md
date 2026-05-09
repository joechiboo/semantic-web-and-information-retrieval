# 期中考個人弱點清單

> **用途：** 記錄今天 (5/9) Q&A 練習中發現的盲點，明天精進模式直接打靶。
> **配套：** `midterm-review-qa.md`（10 題詳解）、`midterm-story-map.md`（全景圖）

---

## 📊 今日進度（5/9 週六）

| 題目 | 狀態 | 評估 |
|------|------|------|
| Q1 IR 定義 | ✅ 走過講義 | 三關鍵詞要記牢：Large Collections / Information Need / Unstructured Documents |
| Q2 Classic Search Model | ✅ 走過講義 | 4 個關鍵觀念要記：翻譯失真 / Query Misformulation / Iterative / 評估看 Need |
| Q3 Precision & Recall | ✅ 走過講義 | 老鼠例子背熟（15/20=75%、15/100=15%） |
| Q4 Term-Document Matrix | ⚠️ 練習過，有盲點 | 見下方 |
| Q5 Inverted Index 結構 | ⚠️ 練習過，有盲點 | 見下方 |
| Q6 Inverted Index 建構流程 | 🔴 不熟，僅讀過參考答案 | 明天重點補強 |
| Q7 INTERSECT 演算法 | ⏳ 待練習 | — |
| Q8 Boolean Model + Optimization | ⏳ 待練習 | — |
| Q9 Biword Index | ⏳ 待練習 | — |
| Q10 Positional Index | ⏳ 待練習 | — |

---

## 🔴 Q4 — Term-Document Matrix 盲點

### 寫到的
- 背景動機（grep 太慢）✅
- 結構：term=row, document=column ✅（容易記反，已確認方向對）
- 規模問題（有提到，但數字記錯）⚠️

### 漏掉/錯誤
| 點 | 嚴重度 |
|---|--------|
| 沒明確寫「值是 0/1（Boolean Matrix）」 | 高 |
| 沒寫如何用向量做布林查詢（AND/OR/NOT 例子） | 高 |
| ⭐ **完全沒提 Sparsity（稀疏性）** | **致命** |
| 沒寫核心結論：「只記 1 的位置 → 引出 Inverted Index」 | 中 |

### 數字訂正（必背）
| 參數 | 正確值 | 我寫的 |
|------|--------|--------|
| 文件數 N | **1,000,000** | ✅ |
| 每份文件平均詞數 | **1,000** | ❌ 寫成 10 萬 |
| 不同詞項數 M | **500,000** | ❌ 沒寫 |
| 矩陣大小 | **5×10¹¹（半兆 cells）** | ❌ 沒算 |

> 💡 **盲點根源：** 混淆了「**每份文件多長**」（1000 詞）和「**整個集合不同詞項有多少**」（500K）。
> 前者決定**總 token 數**（≤ 10⁹），後者決定**矩陣寬度**（500K 行）。

### 必背：Sparsity 的論證
```
矩陣總 cells   = 500,000 × 1,000,000 = 5×10¹¹（半兆）
最多有幾個 1   = 1,000,000 × 1,000  = 10⁹  （10 億）
                  ↑           ↑
                文件數     每文件平均詞數

→ 1 的比例 = 10⁹ / 5×10¹¹ = 0.2%
→ 99.8% 的 cells 都是 0 → 巨大浪費！
```

---

## 🟡 Q5 — Inverted Index 結構盲點

### 寫到的
- 基本結構（term → docID list）✅
- 範例 ✅
- 解決稀疏性（只存 1 的位置）✅
- Postings 按 docID 排序 + 為了 intersection ✅

### 漏掉
| 點 | 嚴重度 |
|---|--------|
| 沒明確命名 **Dictionary** 和 **Postings Lists** 兩部分 | 高 |
| 沒提 **Memory vs Disk** 的區分 | 高 |
| 沒提 Dictionary 也存 **doc frequency** | 中（Q8 會用到） |
| 沒解釋為什麼用 **variable-length list** | 中 |
| 沒提術語細節：a posting (單) vs the postings (集合) | 低 |

### 必背：兩部分結構
```
┌────────────────────────┐         ┌──────────────────────┐
│   Dictionary           │         │   Postings Lists     │
│   (相對小，~500K 詞)   │         │   (大，~10 億筆)      │
│   📍 IN MEMORY         │         │   📍 ON DISK         │
│                        │         │                      │
│  Term     | doc freq   │ pointer │                      │
│  ─────────┼────────    │────────→│                      │
│  Brutus   |  2     ────┼────────→│  [1, 2]              │
│  Caesar   |  4     ────┼────────→│  [1, 2, 4, 6]        │
│  Calpurnia|  1     ────┼────────→│  [2]                 │
└────────────────────────┘         └──────────────────────┘
```

**為什麼這樣分？**
- Dictionary 小，每次查詢都要查 → 必須在 RAM
- Postings 大，每次查詢只讀少數幾個 → 放硬碟連續讀

**為什麼 variable-length？**
- 不同詞的 doc freq 差異巨大（`the` vs `Calpurnia`）
- 動態加文件時固定陣列要重配

---

## 🔴 Q6 — Inverted Index 建構流程（明天重點補強）

### 必背的兩段架構

#### A. 前處理 4 階段（口訣：「切、正、根、停」）

| # | 階段 | 做什麼 | 範例 |
|---|------|--------|------|
| 1 | **Tokenization**（斷詞） | 切成 word tokens | `John's` → `John`? |
| 2 | **Normalization**（正規化） | 統一形式 | `U.S.A.` = `USA` |
| 3 | **Stemming**（詞幹還原） | 對到詞根 | `authorize` → `author` |
| 4 | **Stop Words**（停用詞，**可選**） | 移除常見詞 | 移除 `the`, `a` |

> ⚠️ Stop Words 是**可選**的；現代系統常**保留**（例：`"To Be Or Not To Be"`）

#### B. 建索引 3 步驟

1. **標 docID**：`(I, 1), (did, 1), (caesar, 1), (so, 2), ...`
2. **SORT**（最花時間）：主鍵=詞、次鍵=docID
3. **MERGE**：
   - 同詞同文件去重複
   - 同詞跨文件組成 Postings List
   - Dictionary 記 doc frequency

> ⭐ **關鍵副產品**：因為步驟 2 已按 docID 排過 → **Postings List 自然按 docID 排好**
> → 為 Q7 的 INTERSECT 雙指標掃描鋪好路

---

## 🎯 明天 (5/10) 精進模式重點

### 優先順序
1. **Q6 重練**（從零作答，不看參考）
2. **Q4 重練**（補上 Sparsity + 結論）
3. **Q5 重練**（補上 Dictionary/Postings 命名 + Memory/Disk）
4. **Q7~Q10 全套練習**（還沒練過）
5. **整體模擬考**：用英文出題、限時 60 分鐘做完

### 易混淆數字（背到反射動作）
| 數字 | 意義 |
|------|------|
| **1,000,000 (N)** | 文件數 |
| **500,000 (M)** | 不同詞項數 |
| **1,000** | 每份文件平均詞數 |
| **10⁹** | token 總數上限（也是 1 的個數上限） |
| **5×10¹¹** | 矩陣 cells 數（半兆） |
| **99.8%** | 0 的比例 |
| **2-4×** | Positional Index 比非位置索引大幾倍 |
| **1/4 速度、+26% 空間** | Hybrid Index 的 trade-off |

### 易踩的方向錯誤
- ❌ Term-Document Matrix：term 是 row 還是 column？→ **term=row, document=column**
- ❌ Trade-off 方向：嚴格 → P↑R↓；寬鬆 → P↓R↑
- ❌ 評估基準：是 Information Need，**不是** Query

---

## 📝 概念性盲點總結

> 共通模式：**「核心邏輯都對，但細節結構/命名/數字會漏」**

策略：
1. **背名稱**（Dictionary、Postings、Tokenization、INTERSECT...）
2. **背數字**（500K、1M、10⁹、半兆、99.8%、2-4×）
3. **背口訣**（「慢否近排」、「切正根停」、「P 看給的、R 看全的」）
4. **練畫圖**（Classic Search Model、Inverted Index 結構、Two-level Merge）
