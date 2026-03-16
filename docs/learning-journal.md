# 學習日誌 (Learning Journal)

---

## 2026-03-16（上課 + 課後複習）

### 觀看影片

- [x] 01 - Introduction to Information Retrieval
- [x] 02 - Simple Introduction to Semantic Networks

### 學到的重點

**影片 01 - IR 導論：**
- IR 就是從大量非結構化資料中找到使用者需要的東西
- 搜尋流程：User Task → Information Need → Query → Results → Query Refinement
- Precision（精確率）= 回傳結果中有多少是對的
- Recall（召回率）= 該找到的東西中找到了多少
- 兩者有 Trade-off：精準↑ 則完整度↓，反之亦然
- 評估基準是「資訊需求 (Information Need)」，不是「查詢 (Query)」本身

**影片 02 - 語意網路簡介：**
- 語意網路 = 用圖 (Graph) 來表示知識
- Node（節點）= 物件 / 實體 (Object / Entity)
- Edge（邊）= 無向的連線；Arc（弧）= 有向的連線（帶箭頭）
- 語意網路用的是 Arc（有向邊），因為關係有方向性
- 範例：Apple →is a→ Fruit、Tom →is a→ Cat
- Edge 上的標籤 (Label) 表示關係類型：is a、likes、owned by、sat on

### 還不太懂的地方

- IR 的整體概念還需要多看幾次才能完全理解
- 後續影片會講到具體的索引和查詢實作方式

---