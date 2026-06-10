# 期末考 A4 速記表

## 10 題關鍵字（缺即扣分）

| # | 必寫關鍵字 |
|---|----------|
| Q1 | Boolean → **Feast or Famine**（AND少/OR多）→ Ranked → **Scoring (0~1)** + **只看前面** |
| Q2 | 5 面向：**Exact Match/Set/Boolean Query/專家** ↔ **Scoring/Ranked List/Free Text/一般人** |
| Q3 | `|A∩B| / |A∪B|` + 範例 1/6 + **缺 TF + 缺稀有度** |
| Q4 | Bag of Words = **不管詞序、只管詞頻** + **John/Mary 反向同向量** |
| Q5 | `w = 1 + log₁₀(tf) if tf>0` + 避免 log(0)=-∞ + **Sublinear Scaling** + tf=10→w=2 |
| Q6 | `IDF = log₁₀(N/df)` + N=10^6, df=1 → IDF=6 + 全部都有 → IDF=0 |
| Q7 | IDF 只對**多詞查詢**有用 + **DF**（文件數）vs **CF**（總次數）→ try (df 高) vs insurance (df 低) |
| Q8 | ⭐ `TF-IDF = (1 + log₁₀ tf) × log₁₀(N/df)` + **連字號不是減號** + 詞頻 × 稀有度 |
| Q9 | `Score(q,d) = Σ TF-IDF(t,d) for t ∈ q∩d` + 向量演進 Binary→Count→**Weight** |
| Q10 | **Jaccard（無TF/IDF）→ TF（次線性）→ IDF（稀有度）→ TF-IDF（合體）** |

## 核心公式（必背）

```text
TF:      w = 1 + log₁₀(tf)    if tf > 0
                = 0            if tf = 0

IDF:     IDF(t) = log₁₀(N / df_t)

TF-IDF:  TF-IDF(t,d) = (1 + log₁₀ tf) × log₁₀(N/df)   ⭐

Score:   Score(q,d) = Σ TF-IDF(t,d)   for t ∈ q∩d
```

## 數字記憶表

| tf | log w | IDF (N=10^6) |
|----|-------|--------------|
| 1 | 1 | df=1 → 6 |
| 2 | 1.3 | df=100 → 4 |
| 10 | 2 | df=10K → 2 |
| 1000 | 4 | df=10^6 → 0 |

## ⚠️ 三大死穴

1. **Q8 TF-IDF 是相乘不是相減**（連字號 `-` 不是減號）
2. **Q7 IDF 對單詞查詢無影響**（只在多詞查詢有用）
3. **Q4 Bag of Words 致命例子是 John/Mary**（向量同、意思反）

## 整體演進邏輯

```text
Boolean (Exact Match, 無排名)
   ↓ 解決 Feast/Famine
Ranked Retrieval (Scoring 0~1)
   ↓ 開始評分
Jaccard (|A∩B|/|A∪B|) ← 缺 TF + 缺 IDF
   ↓ 加詞頻
TF (1 + log₁₀ tf, Sublinear)
   ↓ 加稀有度
IDF (log₁₀ N/df)
   ↓ 合體
TF-IDF ⭐ 經典加權
```