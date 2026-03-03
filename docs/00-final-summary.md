# 期末考範圍 - Final

> Slide 6 (Ranked Retrieval)，共 5 部影片

---

### Traditional Information Retrieval -- Ranked Retrieval (排序檢索)

- [10 - Introducing Ranked Retrieval (排序檢索導論)](10-introducing-ranked-retrieval.md)
  - https://www.youtube.com/watch?v=ZrNmCtSrL48
  - Boolean 的「饗宴或飢荒」問題 (Feast or Famine Problem)
  - Ranked Retrieval（排序檢索）：對每個文件評分 (Scoring)（0~1），按分數排序返回
  - Free Text Queries（自由文字查詢）：取代布林語法

- [11 - Scoring with the Jaccard Coefficient (使用 Jaccard 係數評分)](11-scoring-with-jaccard-coefficient.md)
  - https://www.youtube.com/watch?v=MiX8_JVP6PE
  - Jaccard Coefficient = |A ∩ B| / |A ∪ B|，值在 0~1 之間
  - 局限性：不考慮詞頻 (Term Frequency)、不區分罕見詞 (Rare Terms) 與常見詞 (Common Terms)

- [12 - Term-Frequency Weighting (詞頻加權)](12-term-frequency-weighting.md)
  - https://www.youtube.com/watch?v=9UXM2NXVYY0
  - Bag of Words 模型（詞袋模型）：不考慮詞序 (Word Order)，只考慮詞頻 (Term Frequency)
  - Log 詞頻加權 (Log-frequency Weighting)：w = 1 + log₁₀(tf)（tf > 0 時），0（tf = 0 時）
  - 次線性增長 (Sublinear Scaling)：出現 10 次 → 權重 2，出現 1000 次 → 權重 4

- [13 - Inverse Document Frequency Weighting (逆文件頻率加權)](13-inverse-document-frequency-weighting.md)
  - https://www.youtube.com/watch?v=7nWlI_TVid0
  - IDF = log₁₀(N / df)，N = 文件總數，df = 包含該詞的文件數
  - 罕見詞 (Rare Terms) IDF 高（更有資訊量），常見詞 (Common Terms) IDF 低（甚至為 0）
  - IDF 對單詞查詢 (One-term Query) 無影響，只在多詞查詢 (Multi-term Query) 時有效
  - 文件頻率 (Document Frequency) vs 集合頻率 (Collection Frequency) 的差異

- [14 - TF-IDF Weighting (TF-IDF 加權)](14-tf-idf-weighting.md)
  - https://www.youtube.com/watch?v=4-P3ckZprBk
  - TF-IDF = (1 + log₁₀ tf) × log₁₀(N/df)
  - 資訊檢索中最經典的加權方案 (Weighting Scheme)
  - 演進：二元向量 (Binary Vector) → 計數向量 (Count Vector) → 權重向量 (Weight Vector)（實數值矩陣）

---

## 核心概念速查

### TF-IDF 公式

```
TF-IDF(t, d) = TF(t, d) × IDF(t)

TF(t, d) = 1 + log₁₀(tf)    （若 tf > 0）
          = 0                  （若 tf = 0）

IDF(t) = log₁₀(N / df_t)

N  = 文件集合總文件數
df = 包含詞項 t 的文件數
```