# 可能不考 - Extra

> Slide 7 (Ranked Retrieval 2)，共 3 部影片

---

### Traditional Information Retrieval -- Ranked Retrieval (2) (排序檢索進階)

- [15 - The Vector Space Model (向量空間模型)](15-the-vector-space-model.md)
  - https://www.youtube.com/watch?v=o5nflzfX5tw
  - 文件 (Document) 和查詢 (Query) 都是高維向量空間 (High-dimensional Vector Space) 中的向量
  - 餘弦相似度 (Cosine Similarity) = 兩向量夾角的餘弦值
  - 長度正規化 (Length Normalization)：消除文件長度差異
  - 公式：cos(q, d) = (q · d) / (|q| × |d|)

- [16 - Calculating TF-IDF Cosine Scores (計算 TF-IDF 餘弦分數)](16-calculating-tf-idf-cosine-scores.md)
  - https://www.youtube.com/watch?v=k1tD7pYKWuM
  - SMART 表示法 (SMART Notation)：lnc.ltc（文件用 lnc，查詢用 ltc）
  - 完整計算範例：文件 "car insurance auto insurance" vs 查詢 "best car insurance"
  - 排序檢索系統的演算法：累加器 (Accumulators) + 長度正規化 (Length Normalization)

- [17 - Evaluating Search Engines (搜尋引擎評估)](17-evaluating-search-engines.md)
  - https://www.youtube.com/watch?v=b7pfLpVBN84
  - 評估三要素：文件集合 (Document Collection)、查詢集合 (Query Set)、人工相關性判斷 (Human Relevance Judgments)
  - 精確率-召回率曲線 (Precision-Recall Curve)：不同截斷點 (Cut-off Points) 的精確率-召回率
  - 平均精確率均值 (Mean Average Precision, MAP)

---

## 核心概念速查

### Cosine Similarity 公式

```
cos(q, d) = Σ(qi × di) / (|q| × |d|)

|v| = √(Σ vi²)

長度正規化後：cos(q, d) = q̂ · d̂ （單位向量的內積）
```