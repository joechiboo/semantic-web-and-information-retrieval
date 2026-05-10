# 期中考 A4 速記表 (Cheat Sheet)

> 一張紙搞定 — 列印或螢幕全看 | 配合默寫 Q1~Q10

---

## 📋 10 題關鍵字默寫提示

| # | 題目核心 | 必寫關鍵字（缺即扣分）|
|---|---------|-------------------|
| Q1 | What is IR? | **Large Collections** / **Information Need** / **Unstructured Documents** + 應用：Web/Email/Enterprise/Legal |
| Q2 | Classic Search Model | 圖 6 層 + 4 觀念：①翻譯丟失 ②**Misformulation** ③**Iterative** ④評估看 **Need** |
| Q3 | Precision & Recall | 公式 + 老鼠 15/20=75%、15/100=15% + **Trade-off** + 評估基準=**Need** |
| Q4 | Term-Doc Matrix 不實用 | Boolean Matrix(0/1) + **半兆 cells**(1M×500K) + **稀疏 99%+** + grep 4 點 |
| Q5 | Inverted Index 結構 | **Dictionary**(doc freq, Memory) + **Postings Lists**(Disk) + **按 docID 排序** |
| Q6 | 建構流程 | 前處理 4 階段 + 建索引 3 步驟（**標 ID → 排序 → Consolidation**）|
| Q7 | INTERSECT 演算法 | 雙指標「**誰小誰動**」+ **O(x+y)** vs O(x×y) |
| Q8 | Boolean Model | **AND/OR/NOT** + **Exact Match** + **No Ranking** + Optimization 從 **doc freq 最低**開始 |
| Q9 | Biword Index | Phrase=引號相鄰 + 兩連續詞當 term + **False Positives** + **Dictionary Blowup (V²)** |
| Q10 | Positional Index | 記**位置** + 目的=**支援片語/鄰近**（非 ranking）+ **Two-level Merge** + **2-4 倍**大小 |

---

## 🖼 三張必畫的圖

### 1. Classic Search Model (Q2)
```
User Task
  ↓
Information Need
  ↓
Query
  ↓
Search Engine ←→ Document Collection
  ↓
Results
  ↓
Query Refinement → 回到 Query
```

### 2. Inverted Index 兩側結構 (Q5)
```
   Dictionary (Memory)         Postings Lists (Disk)
┌────────────────────┐         ┌──────────────────┐
│ Term  | doc freq   │ pointer │                  │
├───────┼────────────┤────────→│                  │
│brutus | 2      ────┼────────→│  [1, 2]          │
│caesar | 2      ────┼────────→│  [1, 2]          │
└────────────────────┘         └──────────────────┘
```

### 3. Positional Index 結構 (Q10)
```
term → < doc.freq;
         docID1: ⟨pos1, pos2, ...⟩;
         docID2: ⟨pos1, pos2, ...⟩; >

範例：be → 993,427 docs;
       1: ⟨7, 18, 33, 72⟩;
       2: ⟨3, 149⟩
```

---

## 🔢 易混淆數字 / 術語對照

| 概念 | 屬於哪題 | 數字/特徵 |
|------|---------|----------|
| 半兆 cells (5×10¹¹) | Q4 | 1M docs × 500K terms |
| 99%+ 是 0 | Q4 | Sparsity |
| **2-4 倍**大小 | **Q10 Positional！** | 比非位置索引大 2-4 倍 |
| **V² 字典爆炸** | **Q9 Biword！** | Dictionary Blowup |
| O(x+y) | Q7 | 排序後雙指標 |
| O(x×y) | Q7 | 沒排序的代價 |

> ⚠️ **千萬別搞混：** 「2-4 倍」是 Q10 / 「V²」是 Q9

---

## 🧠 INTERSECT 演算法（Q7 完整背）

```
INTERSECT(p1, p2)
1  answer ← ⟨⟩
2  while p1 ≠ NIL and p2 ≠ NIL
3    do if docID(p1) = docID(p2)
4         then ADD(answer, docID(p1))
5              p1 ← next(p1); p2 ← next(p2)
6         else if docID(p1) < docID(p2)   ← 注意 <
7              then p1 ← next(p1)         ← 誰小誰動
8              else p2 ← next(p2)
9  return answer
```

---

## 🚨 個人三大易錯（重複犯過）

1. **「結構畫對但漏特性」** — Q5、Q8、Q10
   - Q5：漏「排序 + Memory/Disk」
   - Q8：漏「Exact Match + No Ranking」
   - Q10：漏「目的=支援片語」

2. **「題目問什麼漏什麼」** — Q3
   - 題目寫 trade-off 卻沒答 trade-off
   - **答前先把題目問句拆開逐項對應**

3. **「Q9/Q10 觀念交叉」**
   - Biword 限制 = **Dictionary Blowup (V²)**
   - Positional 代價 = **2-4 倍大小**

---

## ⚡ 邏輯鏈一句話（理解用）

> grep 慢 → Matrix 太稀疏 → Inverted Index → 雙指標 O(x+y) → Boolean Model → 標準 Index 不夠處理片語 → Biword 字典爆炸 → **Positional Index + Two-level Merge**（標準解法）

---

## ✍️ 答題策略 (考場 SOP)

1. **拆題目**：把英文題目每個問句畫線，逐項對答
2. **先寫關鍵字**：看到題目立刻寫下這張表的關鍵字（避免漏）
3. **舉例子**：能舉例就舉（Brutus/Caesar、information retrieval、老鼠等）
4. **畫得出圖就畫**：Q2、Q5、Q7、Q10 都可加分
