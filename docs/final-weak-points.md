# 期末考弱點追蹤（按優先度排序）

> 時間不夠時，**從上往下練**（紅色最弱、需要最多練習）
> 更新日期：2026-06-10（晚上）

---

## 📊 練習進度追蹤（2026-06-12 第二輪無提示測試）

| 題 | 之前最高 | 今天（無提示）| 變化 | 還缺什麼 |
|----|---------|--------------|------|---------|
| Q1 | 95% | **95%** ⭐ | 持平 | 達標 ✅ |
| Q2 | 90% | 80% | ⬇️ 10% | **漏「匹配方式」面向** |
| Q3 | 85% | 85% | 持平 | 加英文 TF/IDF |
| Q4 | 75% | **90%** ⭐ | ⬆️ 15% | **突破 John/Mary 例子！** |
| Q5 | 80% | 80% | 持平 | 還是缺 Sublinear Scaling |
| Q6 | 95% | 80% | ⬇️ 15% | **寫成 tf_t（應該 df_t）** |
| Q7 | 80% | **85%** | ⬆️ 5% | **寫到 multi-term 概念！** |
| Q8 | 85% | **90%** ⭐ | ⬆️ 5% | **df_t 寫對！** 缺括號 |
| Q9 | 70% | 75% | ⬆️ 5% | Score(q,d) + q∩d 條件 |
| Q10 | 75% | 75% | 持平 | 每階段都缺公式 |

🎯 **整體平均：83.5%**

### ⚠️ 退步警訊（要重點記）

1. **Q2 漏「匹配方式」** → 5 個面向缺一不可，**匹配方式最重要！**
2. **Q6 把 df 寫成 tf** → IDF 用的是 **df**（Document Frequency），不是 tf！

✅ **達標 90+：Q1, Q2, Q6**（3 題）
🟡 **接近 80-85%：Q3, Q5, Q7, Q8, Q10**（5 題）
🔴 **最弱：Q4, Q9**（缺例子 / 公式名稱）

---

## 🚨 剩下需要記的東西（最終衝刺）

### Q4 必背：John/Mary 例子

```text
"John is quicker than Mary"  → 向量
"Mary is quicker than John"  → 完全相同向量
                              ↑ 意思相反！
```

### Q5 必背：英文關鍵字

**Sublinear Scaling** = 次線性縮放（Sub=低於、Linear=線性、Scaling=縮放）

### Q7 必背：兩個關鍵點

**1. IDF 對「單一詞項查詢」無影響，只對「多詞查詢」有用**

精確說法：
- 單一詞項查詢（single-term query）：IDF 只是常數倍率，不改變排序
- 多詞查詢（multi-term query）：IDF 區分查詢中不同詞的重要性

**黃金句（英文）：**
> "IDF has no effect on **single-term queries**; it only matters for **multi-term queries** because it allows the system to distinguish the importance of different terms in the query."

**範例：** Query = `the quantum`
- the：IDF ≈ 0（常見詞）→ 幾乎不影響
- quantum：IDF 高（罕見詞）→ 主導排序

**2. DF vs CF（try vs insurance 例子）**

| 詞 | DF | CF | 鑑別力 |
|----|-----|-----|--------|
| try | 高（廣泛分散）| 高 | 低 |
| insurance | 低（集中）| 高 | **高** |

→ CF 都高但 DF 不同 → **DF 能反映鑑別力，CF 不能 → IR 用 DF**

### Q8 必寫：df_t

`(1 + log₁₀ tf_t,d) × log₁₀(N / df_t)`
                              ↑↑↑
                          有兩個字母！

### Q9 必背：完整公式

```text
Score(q, d) = Σ TF-IDF(t, d)
            t ∈ q ∩ d
```

關鍵：**Score(q,d)** + **q ∩ d** 條件

### Q10 必補：每階段加公式

```text
Jaccard：|A∩B|/|A∪B|
TF：1 + log₁₀(tf)
IDF：log₁₀(N/df)
TF-IDF：(1 + log₁₀ tf) × log₁₀(N/df)
```

---

## 🔴 最弱（優先練習）

### Q1 — Feast or Famine + Why Ranked Retrieval

**第 3 次達 80%！還差「使用者只看前面」這句**

**4 個必補的點：**
1. 明確說是 **Boolean Retrieval** 的問題
2. 解釋 AND/OR 為什麼兩極化
3. 寫 **Scoring (0~1)** 關鍵字
4. 解釋為何 Ranked 解決（**使用者只看前面幾筆**）

**口訣：** Boolean F/F → Ranked Scoring → 只看前面

---

### Q2 — Boolean vs Ranked 差異

**40%，5 個面向只寫 2 個**

**必記 5 面向：**

| Boolean | Ranked |
|---------|--------|
| Exact Match | Scoring (0~1) |
| Set | Ranked List |
| Boolean Query | **Free Text Queries** ⭐ |
| 有 F/F | 解決 |
| 專家 | 一般使用者 |

**最容易漏：Free Text Queries**

---

### Q5 — Log 詞頻加權

**公式對、理由錯**

**錯誤理解：** 「< 10 的 log = 0」
**正確：** `log(0) = -∞` 會爆炸 → 分兩種情況

**必背：**

```text
w = 1 + log₁₀(tf)   if tf > 0
w = 0               if tf = 0
```

**為何用 log：** **Sublinear Scaling**（次線性增長）

**數字：** tf=10 → w=2, tf=1000 → w=4

---

### Q6 — IDF 公式

**60%（數字算錯 + 沒寫公式）**

**錯誤：** 100000（10⁵）vs 1000000（10⁶）搞混

**必寫：**

```text
IDF(t) = log₁₀(N / df_t)
```

**數字（N = 10⁶ = 1,000,000）：**
- df = 1 → IDF = 6
- df = 10⁶ → IDF = 0

---

### Q8 — TF-IDF 公式 ⭐ 必考

**60%（公式不精確）**

**錯誤寫法：** `1 + log_t,d × log(N/d_t)`
**正確：** `(1 + log₁₀ tf_t,d) × log₁₀(N / df_t)`

**死穴：中間是相乘 ×，不是相減 -**

**必寫的解釋：**
- TF 部分：詞在文件多重要
- IDF 部分：詞整體多稀有
- Manning：「只能學一個 IR 加權方法就學這個」

---

## 🟡 中等（看過答案，沒測試過）

### Q3 — Jaccard Coefficient

**重點：**
- 公式：`|A∩B| / |A∪B|`
- 範例：march = 1/6
- **兩個限制：不考慮詞頻、不分罕見/常見**

### Q4 — Bag of Words

**重點：**
- 不考慮詞序、只考慮詞頻
- **John/Mary 例子**（向量同、意思反）

### Q9 — TF-IDF 評分

**剛看答案，要再測試**

```text
Score(q, d) = Σ TF-IDF(t, d)
            t ∈ q ∩ d
```

**步驟：**
1. 找出查詢和文件**共有**的詞
2. 對每個共有詞算 TF-IDF
3. 全部加總

---

## 🟢 較強（不用花太多時間）

### Q7 — TF / DF / CF 三方對比

**80%，三個 freq 全對 ⭐**

**還要加：**
- IDF 只對**多詞查詢**有用
- try vs insurance 例子（DF 高/低 vs CF 都高）

---

## ⚪ 還沒練

### Q10 — Jaccard → TF → IDF → TF-IDF 演進

**綜合題，最後再練**

---

## 📌 時間不夠時的衝刺順序

**最後 30 分鐘怎麼用：**

1. **Q1**（5 min）— 重寫一次完整答案
2. **Q8 公式**（3 min）— 默寫 `(1 + log tf) × log(N/df)`
3. **Q6 + Q7**（5 min）— IDF 公式 + TF/DF/CF
4. **Q5**（5 min）— Log 詞頻公式 + Sublinear
5. **Q2**（5 min）— 5 面向（特別記 Free Text Queries）
6. **Q10**（5 min）— 演進邏輯（Jaccard→TF→IDF→TF-IDF）
7. 看 [A4 速查表](final-cheatsheet-a4.md)（2 min）

---

## 🚨 三大死穴

1. **Q8：TF-IDF 是相乘 ×，不是相減 -**（連字號陷阱）
2. **Q7：IDF 對單詞查詢無影響**（只在多詞查詢有用）
3. **Q4：Bag of Words 致命例子是 John/Mary**

---

## 必背公式（默寫到會）

```text
TF:     w = 1 + log₁₀(tf)         if tf > 0
              0                    if tf = 0

IDF:    IDF(t) = log₁₀(N / df_t)

TF-IDF: (1 + log₁₀ tf) × log₁₀(N / df)   ⭐

Score:  Score(q,d) = Σ TF-IDF(t,d)   for t ∈ q∩d
```
