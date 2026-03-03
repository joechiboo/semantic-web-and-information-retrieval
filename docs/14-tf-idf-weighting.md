# TF-IDF Weighting (TF-IDF 加權)

**影片連結：** https://www.youtube.com/watch?v=4-P3ckZprBk

---

## 英文逐字稿 (English Transcript)

We've now introduced two weights for terms and documents to use in our information retrieval ranking process: term frequency and inverse document frequency. In this segment we're going to put them together to get the TF-IDF weight of terms. The TF-IDF weight of a term in a document, right here, is simply the product of its TF weight scaled with a log term as we discussed before, times its inverse document frequency weight. This is the best known weighting scheme for terms in information retrieval. There's been a lot of research, and there are many others. But if you only know one, it's the one to know. Note in particular one fine point. So this little dash or a hyphen here in this TF-IDF weighting, that's a hyphen, it's not a minus sign, that we're taking a product. So sometimes people indicate that more explicitly by using a dot or using a multiplication sign. So, what are the features of TF-IDF weighting? Tf-idf weighting increases with the number of times a term occurs in a document so that the TF-IDF weight for a query term depends on the document. It's not independent of the document. And then the TF-IDF weight for a term also goes up with the rarity of the term in the collection. That's from the IDF weighting here. So using this to find the ranking of documents for a query, what we're doing to work out the score of the query in the document is we're taking the terms that appear in both the query and the document. The rest of them have no weighting, and we're working out this TD-IDF weight for each of those terms and then we're summing them to get the score of the document with respect to the query. So what have we done here? What we've done is we've gradually moved from first binary vectors in the original model of doing Boolean information retrieval, to count vectors which were used when we just had an unscaled term frequency. To now we have weight vectors for a document and hence a weight matrix between terms and documents and that's now what we see here. So each document is now being represented by a real-valued vector. So for example, the document Julius Caesar is being represented by this vector. So that for each document, it's in the vector space of real valued numbers where the dimensionality is the number of different terms in our collection again. Okay, and then when we have a bunch of these vectors for each document in our collection, we have a term, a term document matrix which is now a real valued matrix. We'll say a little bit more later about what some of the properties of this is. But hopefully, seeing this kind of term document matrix of real numbers is enough to see how we can do a ranking of documents according to some query, according to these TF-IDF scores that we've assigned for each term and each document So that's TF-IDF weighting, one of the most central concepts in information retrieval systems.

---

## 中文翻譯 (Chinese Translation)

我們現在已經介紹了在資訊檢索排序過程中用於詞項和文件的兩種權重：詞頻和逆文件頻率。在這個段落中，我們要將它們結合在一起，得到詞項的 TF-IDF 權重。一個詞項在文件中的 TF-IDF 權重，就在這裡，它就是其經過對數縮放的 TF 權重（如我們之前所討論的）乘以其逆文件頻率權重的乘積。這是資訊檢索中最著名的詞項加權方案。已經有很多相關研究，也有許多其他方案。但如果你只知道一個，這就是你應該知道的那個。特別注意一個細節。這裡 TF-IDF 加權中的這個小短線或連字號，它是一個連字號，不是減號，我們是在取乘積。所以有時候人們會更明確地使用一個點或乘號來表示。那麼，TF-IDF 加權有什麼特徵呢？TF-IDF 加權隨著一個詞項在文件中出現的次數增加而增加，因此查詢詞項的 TF-IDF 權重取決於文件。它不是獨立於文件的。然後，一個詞項的 TF-IDF 權重也隨著該詞項在文件集中的稀有程度而增加。這來自這裡的 IDF 加權。因此，使用這個來找出查詢的文件排序，我們計算查詢在文件中的分數所做的是，取同時出現在查詢和文件中的詞項。其餘的詞項沒有權重，然後我們為每個這樣的詞項計算 TF-IDF 權重，再將它們加總以得到文件相對於查詢的分數。那麼我們在這裡做了什麼？我們所做的是逐步從最初進行布林資訊檢索的二元向量模型，到我們只有未縮放詞頻時使用的計數向量，再到現在我們有文件的權重向量，從而有了詞項和文件之間的權重矩陣，這就是我們現在看到的。所以現在每個文件都由一個實數值向量表示。例如，文件 Julius Caesar 由這個向量表示。因此對於每個文件，它在實數值的向量空間中，其維度同樣是我們文件集中不同詞項的數量。好的，當我們的文件集中每個文件都有這些向量時，我們就有了一個詞項-文件矩陣，它現在是一個實數值矩陣。我們稍後會再多談一些這個矩陣的某些特性。但希望看到這種由實數組成的詞項-文件矩陣足以讓你理解，我們如何根據我們為每個詞項和每個文件分配的 TF-IDF 分數，對文件按照某個查詢進行排序。這就是 TF-IDF 加權，資訊檢索系統中最核心的概念之一。

---

## 重點摘要 (Key Summary)

- **TF-IDF 定義：** TF-IDF 權重是詞頻權重 (TF) 與逆文件頻率權重 (IDF) 的乘積，即 TF-IDF = (1 + log10(tf)) x log10(N/df)。
- **最重要的加權方案：** TF-IDF 是資訊檢索中最著名的詞項加權方案，如果只能了解一個加權方法，就應該了解這個。
- **連字號不是減號：** TF-IDF 中的連字號 (-) 是連接符號，不是減號；TF 和 IDF 之間的關係是相乘而非相減。
- **TF-IDF 的兩大特徵：**
  - 權重隨詞項在文件中出現的次數增加而增加（來自 TF 的貢獻）。
  - 權重隨詞項在文件集中的稀有程度增加而增加（來自 IDF 的貢獻）。
- **文件排序方法：** 對於每個文件，取查詢和文件中共同出現的詞項，計算每個詞項的 TF-IDF 權重並加總，作為該文件相對於查詢的分數。
- **向量表示的演進：** 從布林檢索的二元向量（0/1），到詞頻的計數向量（自然數），再到 TF-IDF 的權重向量（實數值），文件的表示逐步精細化。
- **詞項-文件矩陣：** 每個文件由一個實數值向量表示，所有文件組成一個實數值的詞項-文件矩陣，可用於根據 TF-IDF 分數進行文件排序。
