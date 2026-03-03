# Calculating TF-IDF Cosine Scores (計算 TF-IDF 餘弦分數)

**影片連結：** https://www.youtube.com/watch?v=k1tD7pYKWuM

---

## 英文逐字稿 (English Transcript)

Okay. Let me tell you a little bit more about how TF-IDF scores and the cosine similarity measure get used together in a ranked IR retrieval system. I'm not going to get a lot into the details of making these systems practical and efficient, but at least give you a little bit more of a sense. So the first thing that you might already started to notice is that TF-IDF weighting isn't really one thing, there's really a family of measures. Let's just look at that in a little bit more detail. So first of all, you have the term frequency and what you do with the term frequency. And you could just have the natural term frequency, but we suggested that that is usually muted by something like log weighting. And that's indeed the most common thing to do. But it's not the only method that's been used. There have been a bunch of other methods that have been suggested for normalizing term frequency. And if we move on to the document frequency, we can not use document frequency weighting at all. We could use this kind of log inverse document frequency weighting, which is again, extremely common. But again, there are other things that people have tried out doing. So if we put these two things together we have TF-IDF weighting, giving us a vector. But, well we may well want to normalize those vectors in some way to have better similarity computations. And so we discussed using the cosine length normalization and it turns out that it has some advantages and some disadvantages, so again there are other things people have tried including both of these and other ones that have came up more recently so things like pivoted length normalization. So in general, we have a kind of a broad menu of choices. And so, at the beginning here of each column, I've given some letter names to these choices. These were choices, these were choices that were developed in the context of the SMART information retrieval system which is a very famous, pioneering information retrieval system that was developed at Cornell by Jerry Salton who was really the father of a lot of modern information retrieval. And so this is, these choices could be given names by giving letters from these. So if you were using the system that we've mainly been talking about, that would be coming out as LTC for logarithm, logarithmic IDF and cosine weighting. And so it, this kind of weighting it then turns out can be used both for queries and documents differently, and so let's go through a little bit how that all comes out. We can have different weightings for queries versus documents. And if we follow this SMART notation, the standard way that they represented things is by these six letters with the dot in the middle, where there is document weighting scheme followed by the query weighting scheme. And there are various variants, but one that was quite standard coming out of the SMART work in the 1990s was this one. So we'll just mention this one in a little bit more detail. If we do the query part of it first what we find out is that, so there's log query normalization. Now this is actually, only makes a difference if you have long queries which might mention words multiple times. If, really, you have short queries, and no word is mentioned more than once, that you're just going to be getting a weight of one for words that appear, and zero for words that don't appear. There's then IDF weighting of the query terms, and cosine normalization. The treatment for the documents is the same except there's actually no IDF normalization of the documents. And that's something that you might want to think about for a moment. Is that a bad idea? There's some reasons to want to do that. One of them is well, you've already put in an IDF factor for the same words in the query, cause remember that you're only going to get non-zero scores for words that occur in both the query and the document. And that there are some advantages in terms of efficiency, of compressing indices if you're not putting IDF in there. Let's take this weighting scheme and again go through a concrete example. So, we're just gonna be working out the score for precisely one document against one query using this weighting scheme, but we'll do it in great depth. Okay, so our document is car insurance, auto insurance. It's a bit of a fake document but we wanted something short, and then the query is best car insurance. So if we go to the query first, best car insurance, these are its raw weights, and so then we're gonna scale those with logarithmic scaling but since each word only occurred once, it stays one. We then get the document of frequency of each of those words which we map onto an inverse document frequencies. So, the rarer words like insurance are getting the highest weighting there. We then multiply this column by this column, which ends up looking just like the document frequency score, except for the word that didn't occur. And then we turn that into a unit vector with cosine normalization and so this our final representation of the query vector. We then move to the document. So the document has some term frequencies that aren't just zero one. So, we reduce those with term frequency weightings so that they look like that. In this case there is no IDF component on the document, so the weights go to being exactly the same just coming from term frequency. And then we again do cosine normalization, which gives us this as our final document vector. Okay, so then to work out the score for this document, for this query. We're then working out the cosine similarity, which is simply the dot product of these two length normalized vectors. And so that's then this vector here. Where only the bottom two components are non-zero. So we add those up and the overall score is 0.8. So the document is a good match for the query. Though, I mean, do remember when you're looking at cosine similarities, that because of the fact that the cosine kind of is sort of flat up the top here. You know, flat descending. It means that you tend to get, for fairly similar documents, that cosine scores are sort of biased fairly high. So it's more important to remember the ordering than the precise values. Okay. But that shows you how we evaluated that document. And then we'd want to evaluate a bunch of other documents and then we'd want to rank according to their cosine similarity scores. A little exercise you might like to do based on this example is, well if you know what the IDF scores are here and the document frequencies you should actually be able to work out what is the number of documents being used as a basis of this example. Okay, now let's go through how we can work out cosine scores in a vector space retrieval system for a document collection. This is the rough kind of algorithm that we're going to want to use. So what we're gonna assume here is that the query is a typical short web-like query. So we're only going to be thinking of the words as either occurring or not occurring in the query. And also, we're gonna skip one other step then. We're not actually going to do any length normalization of the query. And part of the reason of that is when you have a situation like this, length normalization of the query is actually unnecessary because the query vector has some length and for whatever it is, the effective length normalization would just be a rescaling that applies to all query document calculations and wouldn't change the final result. Okay. So given that background, what do we do? So we start off by having a scores array for all documents, which we set to zero. And so we're going to accumulate in here the score of a document for different query terms. And so these scores are often also referred to as accumulators. Okay and then we're also going to have another array for the lengths of the different documents. And so then what we do is go through each term in the query, and we say, well. The query term is actually just going to be one. And then we fetch the postings list for that query. So then, for each document in the postings list, the term has a frequency in that document and we may then want to scale that by doing something like log weighting or something like that and to give us our document weight for the term. And then we are doing the components for the dot product here and summing them into the scores array. So in essence we're kind of, the outer iteration here is for each query term, and we're working out the components of the cosine score for each query term and accumulating it in this scores array. But we haven't actually done any length normalization of the documents either yet. So then, the next step is to work out the length of each document, and then divide these scores by the length of the document. So this then does the length normalization for different document sizes. So given the assumptions I mentioned at the beginning of, the query vector is one zero and we don't need to length normalize it, we have something that is now ordered the same as a length normalized cosine similarity score for the documents. And so then for our ranking, what we just wanted to return is the some number K of documents, their ID's or a representation of them, that has the highest value for scores. Now if you think about it a little, this isn't quite yet a practical algorithm. So that if our document collection is huge, we wouldn't actually want to build an array which has a cell for every document. Say that we might have, you know, twenty billion documents or something like that. And so systems use methods to work out which are likely documents, and only have accumulators for those documents. And similarly at the end it's not a good way to find the most relevant documents by simply doing a linear scan of this scores array. And so there are more efficient data structures to do that. But I hope that that's given you a general idea of how we can build cosine similarity scoring into a ranked retrieval engine. So to summarize, the essence of what we've covered for vector space retrieval is the following steps. That the query is represented as a TF-IDF vector. The document is also weighted as a TF-IDF. The document is also represented as TF-IDF vector. And then, to score a pair of a query and a document, we're working out cosine similarity scores, which we straightforwardly use to rank the documents with. And then what we'll do in the first instance is return some top K's. For example, the top ten documents according to this score to the user as their initial results. And if they ask for more, we can then show them more. Okay, so that's the general idea of how we can start to build a TF-IDF ranked retrieval system.

---

## 中文翻譯 (Chinese Translation)

好的。讓我再多告訴你一些關於 TF-IDF 分數和餘弦相似度度量如何在排名式資訊檢索系統中一起使用的內容。我不會深入討論使這些系統實用和高效的細節，但至少會讓你有更多的了解。

首先，你可能已經開始注意到，TF-IDF 加權其實不是單一的方法，它實際上是一系列度量方法。讓我們更詳細地看看這一點。

首先，你有詞頻以及你對詞頻做的處理。你可以只使用自然詞頻，但我們建議通常透過對數加權之類的方法來削弱它。這確實是最常見的做法。但這不是唯一被使用過的方法。已經有一堆其他方法被建議用來正規化詞頻。

如果我們繼續看文件頻率，我們可以完全不使用文件頻率加權。我們可以使用這種對數逆文件頻率加權，這也是非常常見的。但同樣地，人們也嘗試過其他方法。

所以如果我們把這兩者放在一起，我們就有了 TF-IDF 加權，給我們一個向量。但是，我們很可能想要以某種方式正規化這些向量，以便有更好的相似度計算。我們討論了使用餘弦長度正規化，事實證明它有一些優點和缺點，所以人們也嘗試了其他方法，包括這些方法和最近出現的其他方法，比如樞軸長度正規化。

所以總的來說，我們有一個相當廣泛的選擇菜單。在每一欄的開頭，我給這些選擇取了一些字母名稱。這些選擇是在 SMART 資訊檢索系統的背景下開發的，SMART 是一個非常著名的、開創性的資訊檢索系統，由 Cornell 大學的 Jerry Salton 開發，他確實是許多現代資訊檢索的奠基者。

因此，這些選擇可以用這些字母來命名。如果你使用的是我們主要討論的系統，那就是 LTC，代表對數、對數 IDF 和餘弦加權。

這種加權方式可以分別用於查詢和文件，讓我們來看看這一切是怎麼組合在一起的。我們可以對查詢和文件使用不同的加權。如果我們遵循這個 SMART 記法，他們表示事物的標準方式是中間有一個點的六個字母，其中文件加權方案在前，查詢加權方案在後。

有各種變體，但一個在 1990 年代 SMART 研究中相當標準的是這個。我們就稍微更詳細地提一下這個。

如果我們先做查詢部分，我們發現，有對數查詢正規化。實際上，這只有在你有可能多次提到某些詞的長查詢時才有區別。如果你真的有短查詢，沒有任何詞被提到超過一次，那麼出現的詞你只會得到權重一，不出現的詞得到零。然後是查詢詞項的 IDF 加權和餘弦正規化。

文件的處理方式是一樣的，除了實際上沒有對文件做 IDF 正規化。這是你可能想要思考一下的事情。這是一個壞主意嗎？有一些原因想要這樣做。其中之一是，你已經在查詢中為相同的詞放入了 IDF 因子，因為請記住，你只會對同時出現在查詢和文件中的詞得到非零分數。而且在效率方面，如果你不放入 IDF，在壓縮索引方面有一些優勢。

讓我們取這個加權方案，再次通過一個具體例子來說明。我們只是要精確地計算一個文件對一個查詢的分數，使用這個加權方案，但我們會非常深入地做。

好的，我們的文件是「car insurance, auto insurance」（汽車保險，自動保險）。這是一個有點假的文件，但我們想要一個簡短的東西，然後查詢是「best car insurance」（最佳汽車保險）。

如果我們先看查詢，「best car insurance」，這些是它的原始權重，然後我們要用對數縮放來調整它們，但由於每個詞只出現了一次，所以它保持為一。然後我們得到每個詞的文件頻率，我們將其映射到逆文件頻率。所以像「insurance」這樣較罕見的詞在那裡得到了最高的權重。

然後我們將這一欄乘以這一欄，結果看起來就像文件頻率分數，除了那個沒有出現的詞。然後我們用餘弦正規化將其轉換為單位向量，所以這就是我們查詢向量的最終表示。

然後我們轉到文件。文件有一些不只是零一的詞頻。所以我們用詞頻加權來降低它們，使它們看起來像那樣。在這個情況下，文件沒有 IDF 分量，所以權重完全一樣，只來自詞頻。然後我們再次做餘弦正規化，這給了我們最終的文件向量。

好的，那麼要計算這個文件對這個查詢的分數，我們就要計算餘弦相似度，它就是這兩個長度正規化向量的點積。這就是這裡的這個向量，其中只有最下面兩個分量是非零的。我們把它們加起來，總分是 0.8。所以這個文件與查詢很匹配。

不過，我的意思是，當你看餘弦相似度時，請記住由於餘弦在頂部附近是比較平坦的，你知道，平緩下降。這意味著對於相當相似的文件，你傾向於得到偏高的餘弦分數。所以記住排序比精確值更重要。

好的。但這向你展示了我們如何評估那個文件。然後我們會想要評估一堆其他文件，然後我們會想要根據它們的餘弦相似度分數來排名。

基於這個例子，你可能想做的一個小練習是，如果你知道這裡的 IDF 分數和文件頻率，你實際上應該能夠算出這個例子使用了多少文件作為基礎。

好的，現在讓我們來看看如何在向量空間檢索系統中為文件集合計算餘弦分數。這是我們要使用的大致演算法。

我們在這裡假設查詢是一個典型的短網路式查詢。所以我們只考慮詞在查詢中出現或不出現。而且我們也要跳過另一個步驟。我們實際上不會對查詢做任何長度正規化。部分原因是，當你遇到這種情況時，查詢的長度正規化實際上是不必要的，因為查詢向量有某個長度，無論它是什麼，長度正規化的效果只是一個適用於所有查詢-文件計算的重新縮放，不會改變最終結果。

好的。在這個背景下，我們該怎麼做？首先，我們有一個所有文件的分數陣列，我們將其設為零。我們將在這裡為不同的查詢詞項累積文件的分數。所以這些分數通常也被稱為累加器。

然後我們也會有另一個陣列用於不同文件的長度。然後我們要做的是遍歷查詢中的每個詞項，我們說，查詢詞項的權重實際上就是一。然後我們取出該查詢的倒排列表。

對於倒排列表中的每個文件，該詞項在那個文件中有一個頻率，我們可能想要通過對數加權之類的方法來縮放它，以給出我們該詞項的文件權重。然後我們在這裡做點積的分量計算，並將它們累加到分數陣列中。

所以本質上，外層迭代是對每個查詢詞項，我們計算每個查詢詞項的餘弦分數分量，並將其累積在這個分數陣列中。但我們還沒有對文件做任何長度正規化。

所以下一步是計算每個文件的長度，然後將這些分數除以文件的長度。這就對不同大小的文件做了長度正規化。

所以根據我在開頭提到的假設，查詢向量是一零的，我們不需要對它進行長度正規化，我們現在得到的東西與文件的長度正規化餘弦相似度分數具有相同的排序。

然後對於我們的排名，我們只想返回某個數量 K 的文件，它們的 ID 或表示，具有最高的分數值。

現在如果你稍微想一下，這還不是一個完全實用的演算法。如果我們的文件集合很大，我們實際上不會想建立一個為每個文件都有一個單元的陣列。比如說我們可能有兩百億個文件之類的。所以系統使用方法來找出哪些是可能的文件，只為那些文件設置累加器。

同樣地，在最後，通過簡單地線性掃描這個分數陣列來找到最相關的文件也不是一個好方法。所以有更高效的資料結構來做這件事。但我希望這已經給了你一個大致的概念，了解我們如何將餘弦相似度評分建構到排名式檢索引擎中。

總結一下，我們所涵蓋的向量空間檢索的精髓是以下步驟。查詢被表示為 TF-IDF 向量。文件也被加權為 TF-IDF。文件也被表示為 TF-IDF 向量。然後，要為查詢和文件的配對評分，我們計算餘弦相似度分數，直接用它來對文件進行排名。

然後在第一時間，我們會返回一些前 K 個結果。例如，根據這個分數將前十個文件返回給使用者作為他們的初始結果。如果他們要求更多，我們可以再展示更多。

好的，這就是我們如何開始建構 TF-IDF 排名式檢索系統的大致概念。

---

## 重點摘要 (Key Summary)

- **TF-IDF 是一系列方法**：TF-IDF 加權不是單一方法，而是一系列度量方法的組合，包括不同的詞頻處理方式（自然詞頻、對數加權等）、不同的文件頻率處理方式（不使用、對數逆文件頻率等），以及不同的正規化方式（餘弦正規化、樞軸長度正規化等）。
- **SMART 記法**：由 Cornell 大學的 Jerry Salton 開發的 SMART 資訊檢索系統提出了一套用字母命名加權方案的記法。例如 LTC 代表對數詞頻、對數 IDF 和餘弦正規化。
- **查詢與文件可以使用不同加權**：SMART 記法使用六個字母加一個點來表示，點前是文件加權方案，點後是查詢加權方案。
- **文件省略 IDF 的理由**：一種常見做法是在文件端不做 IDF 正規化，原因包括：查詢端已經包含了相同詞的 IDF 因子，且不放入 IDF 有助於索引壓縮效率。
- **具體計算範例**：以文件「car insurance, auto insurance」和查詢「best car insurance」為例，詳細展示了如何計算 TF-IDF 餘弦分數。最終得分為 0.8，表示文件與查詢匹配良好。
- **餘弦分數的偏高特性**：由於餘弦函數在頂部附近較為平坦，相似文件的餘弦分數往往偏高，因此排序順序比精確數值更重要。
- **向量空間檢索演算法**：使用累加器（accumulators）陣列，對每個查詢詞項遍歷其倒排列表，累積點積分量，最後除以文件長度做正規化。
- **短查詢的簡化**：對於典型的短網路查詢，可以跳過查詢的長度正規化，因為它只是一個對所有文件-查詢計算都相同的縮放因子，不影響排名結果。
- **實務考量**：實際系統中不會為每個文件建立累加器（可能有數十億文件），而是使用方法找出可能的文件，並使用更高效的資料結構來找出最高分的文件。
- **向量空間檢索總結**：查詢和文件都表示為 TF-IDF 向量，使用餘弦相似度評分來排名文件，返回前 K 個結果給使用者。
