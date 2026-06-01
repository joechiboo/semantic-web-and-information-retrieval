# 期末考弱點追蹤

> 每題練習後記錄缺漏的關鍵字、概念、計算
> 考前最後衝刺時，**只看這份就好**

---

## Q1 — Feast or Famine + Why Ranked Retrieval

### ❌ 第一次練習缺漏

1. **沒明確說是 Boolean Retrieval 的問題**
2. **沒解釋為什麼兩極化**（AND 太嚴格、OR 太寬鬆）
3. **沒提到 Scoring 0~1 這個關鍵字**
4. **沒解釋為何 Ranked 解決 Feast or Famine**（使用者只看前面幾筆）

### ⭐ 必寫英文關鍵字

- **Feast or Famine Problem**
- **Scoring**（0~1）
- **Ranking**
- **Boolean Retrieval**（要明確指出是它的問題）

### 一句話補強

> Boolean Retrieval 的 Feast or Famine：AND 太少、OR 太多 → Ranked Retrieval 給每個文件 0~1 的 Scoring 排序，使用者只看前面幾筆

---

## Q2 — Boolean vs Ranked 差異

### ❌ 第一次練習：直接看答案（沒概念）

### ⭐ 必記 5 個面向

| 面向 | Boolean | Ranked |
|------|---------|--------|
| 匹配方式 | Exact Match | Scoring (0~1) |
| 結果 | Set | Ranked List |
| 查詢語言 | Boolean Query | **Free Text Queries** |
| Feast/Famine | 有 | 解決 |
| 適合對象 | 專家 | 一般使用者 |

### 一句話記法

> Boolean 是「**精確匹配 + 集合 + 專家**」
> Ranked 是「**評分排序 + Free Text + 一般人**」

---

## Q3 — Jaccard Coefficient

### ❌ 第一次練習缺漏

- 公式 ✓ 對（A ∩ B / A ∪ B）
- ❌ 忘了計算範例
- ❌ 忘了兩個限制

### ⭐ 必背三項

**1. 公式：** `Jaccard(A, B) = |A ∩ B| / |A ∪ B|`

**2. 範例：**
- Q = {ides, of, march}
- Doc = {caesar, died, in, march}
- Jaccard = 1/6 ≈ 0.17

**3. 兩個限制（必背）：**
- 不考慮**詞頻 (Term Frequency)** → 引出 TF（影片 12）
- 不分**罕見詞 vs 常見詞** → 引出 IDF（影片 13）

### 一句話記法

> Jaccard = 交集/聯集，問題：詞頻和稀有度都不管

---

## Q4 — Bag of Words 限制

### ❌ 第一次練習：完全沒印象

### ⭐ 必背

**核心特性：** 不考慮詞序，只考慮詞頻

**演進：**
```text
Binary Vector [0,1,1] → Count Vector [0,3,7]
```

**致命例子：**
- "John is quicker than Mary"
- "Mary is quicker than John"
- → **向量完全相同，但意思相反**

### 一句話記法

> Bag of Words = 不管順序、只管次數 → John/Mary 例子

---

## Q5 — Log 詞頻加權

### ❌ 第一次練習缺漏

- 公式方向對（1 + log）✓
- **但理由說錯**：說「< 10 的 log = 0」（錯！）
- 正確：**log(0) = -∞** 會壞掉，所以要分兩種情況

### ⭐ 必背三項

**1. 公式：**
```text
w = 1 + log₁₀(tf)   if tf > 0
w = 0               if tf = 0
```

**2. 權重數字：**
- tf = 1 → w = 1
- tf = 10 → w = 2
- tf = 1000 → w = 4
- → **tf 變 10 倍，w 只多 1**

**3. 為什麼用 log：**
- **Sublinear Scaling**（次線性增長）
- 避免「出現 30 次 = 30 倍相關」的不合理線性假設

### 一句話記法

> log(0) = -∞ → 分兩段；用 log 製造 Sublinear Scaling

---

## Q6-Q10

（看完影片 13、14 後補上）

---

## 📌 最後衝刺速記（考前一晚看）

> 這區塊會在所有題目練完後，整理出每題「**最容易漏寫的關鍵字**」

| Q | 最易漏 |
|---|--------|
| Q1 | Scoring (0~1) + 為何解決 Feast/Famine |
| ... | ... |