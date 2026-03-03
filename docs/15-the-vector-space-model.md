# The Vector Space Model (向量空間模型)

**影片連結：** https://www.youtube.com/watch?v=o5nflzfX5tw

---

## 英文逐字稿 (English Transcript)

Hi again. Okay we've already laid some of the ground work with notions like term frequency and inverse document frequency. In this segment what I want to introduce is probably the retrieval model of the vector space model, which is one of the most commonly used models of information retrieval in real systems. So we saw in the previous segment how we turn documents into real valued vectors. And so we now have a V-dimensional vector space where V is the number of words in our vocabulary. The terms, the words, are the axes of the space, and documents you can think of as either just points in this space, or vectors from the origin pointing out to those points. So we now have a very high dimensional space. Tens of millions of dimensions in a real system when you apply this such as in a web search engine. The crucial property of these vectors is that they're very sparse vectors. Most of the entries are zero, because each individual document only typically has a few hundred or thousand words in it. So then if we have this vector space of documents, how do we handle querying it when a query comes in? And the key idea there is that we treat queries in exactly the same way. They're also going to be vectors in the same space. And then if we do that we can rank documents according to their proximity to the query in this space. So proximity corresponds to similarity of vectors, and therefore it's roughly the reverse of distance. And we're doing this because we want to get away from the, you're either in or out, Boolean model, and have a relative score as to how well a document matches a query. We're going to rank more relevant documents higher than less relevant documents. Let's try and make that all a bit more precise. So how can we formalize proximity in a vector space? The first attempt is just to take the distance between two points. That is the distance between the end points of their vectors. And the standard way to do that in a vector space would be Euclidean distance between the points. But it turns out Euclidean distance by itself isn't actually a good idea. And that's because Euclidean distance is large for vectors of different lengths. Let me explain what I mean by that. Let's suppose, here is our vector space. Well, what we're finding is the distance between here and here is large. In particular it's larger than either the distance here or the distance there. But if we actually think of this in terms of an information retrieval problem and look at what's in our space, that seems wrong. So in this teeny example, the two word axes shown are here for gossip and here for jealous. And what our query is, this is the query that would come out precisely if your query is gossip and jealous. So it has both of those words occurring with equal weight. Well if we then look at our documents, what we find is document one seems to have a lot to do with gossiping and nothing to do with jealousy. And document three has a lot to do with jealousy and nothing to do with gossiping. Whereas document two seems just the kind of document we want to get, one that has a lot to do with both gossiping and jealously. So the terms in the document D2 are very similar to the ones in Q, so we want to be saying that that is actually the most similar document. So this suggests a way to solve this problem and move forward. And that is, rather than just talking about distance, what we want to start looking at is the angle in the vector space. So the idea is we can use angle instead of distance. So let's in particular motivate that once more by considering this thought experiment. Suppose that we take a document and append it to itself, giving us a document D prime. So clearly semantically, D and D prime have the same content, they cover the same information, But if we're just working in a regular vector space with Euclidean distance, the distance between the two documents will be quite large. That's because if we had a vector, and we had, this was the vector for D, then the vector for D prime would be twice as long, pointing out here, and so that we have a quite large distance between these two vectors. So we don't want to do that, instead what we want to notice is that these two vectors are in a line so the angle between two vectors is zero, corresponding to maximal similarity. And so the idea is, we're going to rank documents according to that angle between the document and the query. And so the following two documents are equivalent. Ranking documents in decreasing order of the angle between the query and the document, and ranking documents in increasing order of the cosine of the angle between the query and the document. And so I'll go through that in a little bit more detail. But you'll often hear the phrase cosine similarity, and this is what we're introducing here. And the secret here is just to notice that cosine is a monotonically decreasing function for angles between the interval zero and 180 degrees. So here's the cosine which you should remember. So if the angle is zero, the cosine of it is one. If it's, if it's perpendicular, 90 degrees, the, the cosine is zero. And it can keep on going right up to 180 degrees and the cosine is continuing to descend to minus one. So essentially, all we have, need to observe here is that cosine is a monotonically decreasing function, in the range of zero to 180. And so therefore cosine score serves as a kind of inverse of angle. And, well that might still make it seem a rather strange thing to use. I mean, we could have just taken the reciprocal of the angle, or the negative of the angle, and that would've also turned things around. So we got a measure of closeness between documents as a similarity measure. But it turns out that the cosine measure is actually standard, because there's actually a very efficient way to evaluate the cosine of the angle between documents using vector arithmetic, where we don't actually use any transcendental functions like cosine that would take a long time to compute. So the starting point of going through this is getting an idea of the length of a vector, and how to normalize the length of a vector So, for any vector so if we have a vector X, we can work out the length of the vector by summing up each of its components squared and then taking the square root around the outside. So that, if have something like a vector that's 3,4, what we're going to do is take three squared nine, four squared sixteen, and then take the, add those gives 25. Take the square root gives five. And that's the length of the vector just like in the standard Pythagorean triangle. Okay so if we then take any vector and divide it by its length we then get a unit length vector, which will, you can think of as a vector that touches the surface of a unit hypersphere around the origin. Now if we go back to the example that we had earlier of two documents, D and D appended to itself to give D prime, you can see that these documents, if they're both length normalized will both go back to exactly the same position. And because of that, once you length normalize vectors, long and short documents have comparable weights. So, the secret of our cosine measure is that we do this length normalization. So here's the cosine similarity between two documents, which is the cosine of the angle between the two documents. And the way we do that is in the numerator, we calculate here a dot product. So we're taking the individual components of the vector here, component by component, and multiplying them and taking their sum. But then the way we do that is that we've then got this denominator, which is considering the lengths of the vectors. And you can write it like this. But actually what it's equivalent to is taking each vector and length normalizing it. And then taking the dot product of the whole thing, because it's these sort of two parts. You can factor apart as you wish. And so of, fill, written out in full it's over here that we have the length normalizations on the bottom and then this summed up dot product on the top. Okay where each of these elements QI is a TF-IDF weight of term I in the query. And DI is the TF-IDF weight of the term in the document. In particular what we might want to do is actually length normalize our document vectors in advance. And length normalize our cosine, length normalize our query vector once the query comes in. And if we do that, this cosine similarity measure is simply the dot product of length-normalized vectors. And, so, we're simply just taking this sum here in the vector space. Where as we discussed before, in reality we won't do it over all elements of the vector. We'll just do it over the terms of the vocabulary that are in the intersection of the ones that appear in q and the document. So going back, to the kind of picture we had before, we now again have our vector space, which again we're showing with just two axes here to keep it viewable, which are now poor and rich. And we can take any document vector and we can map it down to unit length by doing by this length normalization. And when we do that we get all document vectors, being vectors that touch the surface of this unit hypersphere, which is just a circle in two dimensions. And so then when we want to order documents by similarity to a query, we take this query here and we're working out the angle, or the cosine of the angle to other, to other documents. So in particular the cosine will be highest for small angles. So we'll be, if we order these documents in terms of the cosine of the angle, the document that will rank first will be d2, then it'll be d1, and then it will be d3. Okay. Now let's now go through this concretely with an example. So, in this example what we have is three novels of Jane Austen's and we are going to represent them in the vector space, length normalized. Then we're going to work out the cosine similarity between the different novels. So, in other words in this example there isn't actually any query vector. We're just working out the similarity between the different novels that are our documents. So the starting off point is starting with these term frequency count vectors, for the different novels. And so what we can see is, affection is one of Jane Austin's favorite words that appears frequently in every novel. The word Wuthering only occurs in Wuthering Heights. And then other words like jealous and, jealous and gossip occur occasionally. And so this is going to be our vocabulary for this example that I give. And what we're going to want to do is take these term frequency vectors and turn them into length normalized vectors on the unit hypersphere. Now for this example I'm just going to use term frequency weighting. We're going to leave out idf weighting to keep it a bit simpler. Let's see what happens on the next slide. Okay, so here we've done log frequency weighting of the kind we saw before. So what were the zeros, stay zero, and then we're having mapping down, so we're getting a weighting of three for the number of times that affection appeared in Sense and Sensibility. But these vectors aren't yet of the same length. This is clearly the longest of the vectors. So the next step is to length normalize them. So now here are the length normalized vectors for the three documents, and you can see how this vector has gotten much shorter than it was here by scaling it down. And the property that we have for each of these vectors for their being length normalized is that if you took this quantity squared, plus this quantity squared, plus this quantity squared, you would get one. And therefore the square root of that sum would also be one. So they're length one vectors. So given that they're length one vectors we can then calculate cosine similarities as simply the dot product between the vectors. So let's see what happens when we do that. Okay, so then we have the cosine similarity between Sense and Sensibility and Pride and Prejudice is taking these pair-wise products and summing them together. And it gives us a cosine similarity of 0.94, so they're very similar. And then we can do it for the other cases, and what we see that for Sense and Sensibility and Wuthering Heights, it's 0.79. And for the final pair, these two, it's 0.69. And the thing that we might wonder is, why do we have that the cosine similarity of Sense and Sensibility and Pride and Prejudice is higher than that for Sense and Sensibility and Wuthering Heights? And so we can try and look at that. So we're going to be comparing this one with the other two. And what we can see is that, this part of the Wuthering Heights vector doesn't help at all in producing similarity with Sense and Sensibility. The biggest component in the Sense and Sensibility vector is this one. And so that generates a lot of similarity with Pride and Prejudice, which also has that word very prominently represented, where that word is less represented in Wuthering Heights. And so therefore, this dot product here, that this term in the dot product is much larger, and so we get greater similarity. And so you can see there that it's sort of the ratio of occurrence of different words in the document has a big effect on measuring overall similarity. Okay, I hope that example helped to make it more specific, and that you now have a good idea of what the vector space model of information retrieval is. It's the idea that we can rank documents for retrieval, based on their similarity of angles in a high dimensional vector space.

---

## 中文翻譯 (Chinese Translation)

大家好。我們已經為詞頻和逆文件頻率等概念奠定了一些基礎。在這一段中，我想介紹的可能是向量空間模型的檢索模型，這是在實際系統中最常使用的資訊檢索模型之一。

在前一段中，我們看到了如何將文件轉換為實數值向量。因此，我們現在有一個 V 維的向量空間，其中 V 是我們詞彙表中的單詞數量。這些詞項，也就是單詞，是空間的座標軸，而文件你可以把它們想像成這個空間中的點，或者是從原點指向這些點的向量。

所以我們現在有一個非常高維度的空間。在實際系統中應用時，例如在網路搜尋引擎中，會有數千萬個維度。這些向量的關鍵特性是它們是非常稀疏的向量。大多數的值都是零，因為每個單獨的文件通常只包含幾百或幾千個單詞。

那麼，如果我們有了這個文件的向量空間，當查詢進來時，我們該如何處理查詢呢？關鍵的想法是，我們以完全相同的方式來處理查詢。查詢也將是同一空間中的向量。如果我們這樣做，我們就可以根據文件在這個空間中與查詢的接近程度來對文件進行排名。因此，接近程度對應於向量的相似度，所以它大致上是距離的反面。

我們這樣做是因為我們想要擺脫那種「你要嘛在裡面，要嘛在外面」的布林模型，而是要有一個相對的分數來表示文件與查詢的匹配程度。我們要將更相關的文件排在比較不相關的文件前面。

讓我們試著把這一切說得更精確一些。那麼我們如何在向量空間中形式化接近程度呢？第一個嘗試就是取兩個點之間的距離，也就是它們向量端點之間的距離。在向量空間中，標準的做法是取點之間的歐幾里得距離。但事實證明，歐幾里得距離本身其實不是一個好主意。這是因為歐幾里得距離對於長度不同的向量來說會很大。

讓我解釋一下我的意思。假設這裡是我們的向量空間。我們發現這裡和這裡之間的距離很大。特別是，它比這裡的距離或那裡的距離都要大。但如果我們實際上從資訊檢索問題的角度來思考，看看我們空間中有什麼，那似乎是錯的。

在這個小例子中，顯示的兩個單詞軸，這裡是「gossip（八卦）」，這裡是「jealous（嫉妒）」。我們的查詢就是，如果你的查詢是「gossip and jealous」，這正是會產生的查詢。所以它包含了這兩個權重相等的單詞。

如果我們查看我們的文件，我們會發現文件一似乎與八卦有很大關係，但與嫉妒無關。文件三與嫉妒有很大關係，但與八卦無關。而文件二似乎正是我們想要得到的文件，它與八卦和嫉妒都有很大關係。所以文件 D2 中的詞項與 Q 中的非常相似，所以我們想說那實際上是最相似的文件。

這提示了一種解決這個問題並向前推進的方法。也就是說，與其只談論距離，我們想要開始看的是向量空間中的角度。所以想法是我們可以用角度代替距離。

讓我們再用一個思想實驗來進一步說明這一點。假設我們取一個文件並將它附加到自身，得到一個文件 D'。很明顯地，在語意上，D 和 D' 有相同的內容，它們涵蓋相同的資訊。但如果我們只是在普通的向量空間中使用歐幾里得距離，兩個文件之間的距離將會相當大。那是因為如果我們有一個向量，這是 D 的向量，那麼 D' 的向量會是兩倍長，指向這裡，所以這兩個向量之間有相當大的距離。

所以我們不想那樣做，相反地，我們想要注意到的是，這兩個向量在一條直線上，所以兩個向量之間的角度是零，對應於最大相似度。

因此，想法是我們將根據文件和查詢之間的角度來對文件進行排名。所以以下兩件事是等價的：按照查詢和文件之間角度的遞減順序排列文件，以及按照查詢和文件之間角度的餘弦值的遞增順序排列文件。

我會更詳細地說明這一點。但你經常會聽到「餘弦相似度」這個詞，這就是我們在這裡介紹的內容。這裡的秘密就是注意到餘弦在零到 180 度的區間內是一個單調遞減函數。

這裡是你應該記住的餘弦函數。如果角度是零，它的餘弦是一。如果是垂直的，90 度，餘弦是零。它可以一直到 180 度，餘弦持續下降到負一。所以基本上，我們需要觀察的就是，餘弦在零到 180 度的範圍內是一個單調遞減函數。因此，餘弦分數作為角度的一種反函數。

那麼，這可能仍然使它看起來是一個相當奇怪的東西。我的意思是，我們可以取角度的倒數，或角度的負值，那也可以把事情反轉過來。所以我們得到了一個作為相似度度量的文件間接近程度度量。但事實證明，餘弦度量實際上是標準的，因為有一種非常有效的方法可以使用向量運算來計算文件之間角度的餘弦，而我們實際上不需要使用任何像餘弦這樣計算起來很慢的超越函數。

所以介紹這個的起點是了解向量的長度，以及如何正規化向量的長度。對於任何向量，如果我們有一個向量 X，我們可以透過將其每個分量平方然後求和，再取外面的平方根來計算向量的長度。所以如果有一個向量是 (3, 4)，我們要做的是取 3 的平方得 9，4 的平方得 16，然後把它們加起來得 25。取平方根得 5。這就是向量的長度，就像標準的畢達哥拉斯三角形一樣。

好的，所以如果我們取任何向量並除以它的長度，我們就得到一個單位長度的向量，你可以把它想成是一個觸及原點周圍單位超球面表面的向量。

現在如果我們回到之前的例子，兩個文件，D 和 D 附加到自身得到 D'，你可以看到這些文件如果都經過長度正規化，它們都會回到完全相同的位置。因此，一旦你對向量進行長度正規化，長文件和短文件就有了可比較的權重。

所以我們餘弦度量的秘密就是我們做了這個長度正規化。這裡是兩個文件之間的餘弦相似度，也就是兩個文件之間角度的餘弦。我們的做法是在分子中，我們計算一個點積。所以我們逐分量地取向量的各個分量，逐個相乘然後求和。但然後我們有這個分母，它考慮了向量的長度。你可以這樣寫。但實際上它等同於取每個向量並對其進行長度正規化，然後取整體的點積，因為它是這兩個部分。你可以隨意分解。

完整寫出來，我們在下面有長度正規化，在上面有求和的點積。其中每個元素 QI 是詞項 I 在查詢中的 TF-IDF 權重，DI 是詞項在文件中的 TF-IDF 權重。

特別是，我們可能想要提前對文件向量進行長度正規化，並在查詢進來時對查詢向量進行長度正規化。如果我們這樣做，這個餘弦相似度度量就只是長度正規化向量的點積。

所以我們只是在向量空間中取這個總和。正如我們之前討論的，實際上我們不會對向量的所有元素都這樣做。我們只會對出現在查詢和文件交集中的詞彙表中的詞項這樣做。

回到我們之前的那種圖片，我們再次有我們的向量空間，這裡我們只顯示兩個軸以保持可視性，它們現在是「poor（窮）」和「rich（富）」。我們可以取任何文件向量，透過長度正規化將其映射到單位長度。當我們這樣做時，所有文件向量都成為觸及這個單位超球面表面的向量，在二維中就只是一個圓。

然後當我們想要根據與查詢的相似度來排序文件時，我們取這個查詢，計算與其他文件的角度或角度的餘弦。特別是，餘弦對於小角度最大。所以如果我們按角度的餘弦來排序這些文件，排名第一的文件將是 d2，然後是 d1，最後是 d3。

好的。現在讓我們用一個具體的例子來說明這一點。在這個例子中，我們有三部珍．奧斯汀的小說，我們要在向量空間中以長度正規化來表示它們。然後我們要計算不同小說之間的餘弦相似度。換句話說，在這個例子中，實際上沒有任何查詢向量。我們只是在計算作為我們文件的不同小說之間的相似度。

起點是從這些不同小說的詞頻計數向量開始。我們可以看到，「affection（情感）」是珍．奧斯汀最喜歡的詞之一，在每部小說中都頻繁出現。「Wuthering」這個詞只出現在《乘風破浪》（咆哮山莊）中。然後其他詞如「jealous（嫉妒）」和「gossip（八卦）」偶爾出現。這就是我在這個例子中要使用的詞彙表。我們要做的是取這些詞頻向量，把它們轉換成單位超球面上的長度正規化向量。

在這個例子中，我只使用詞頻加權。為了簡單起見，我們將省略 IDF 加權。讓我們看看下一張投影片會發生什麼。

好的，這裡我們做了之前看到的對數頻率加權。所以原來是零的保持為零，然後我們進行映射，所以我們得到了「affection」在《理性與感性》中出現次數的權重 3。但這些向量還不是相同長度的。這個明顯是最長的向量。所以下一步是對它們進行長度正規化。

現在這裡是三個文件的長度正規化向量，你可以看到這個向量通過縮小比例後比這裡短了很多。我們對每個向量的長度正規化特性是，如果你取這個量的平方加上這個量的平方加上這個量的平方，你會得到一。因此該和的平方根也等於一。所以它們是長度為一的向量。

既然它們是長度為一的向量，我們就可以將餘弦相似度簡單地計算為向量之間的點積。讓我們看看結果如何。

好的，那麼《理性與感性》和《傲慢與偏見》之間的餘弦相似度是取這些成對的乘積並將它們加在一起。結果給我們的餘弦相似度是 0.94，所以它們非常相似。然後我們可以對其他情況做同樣的計算，我們看到《理性與感性》和《乘風破浪》（咆哮山莊）之間是 0.79。最後一對是 0.69。

我們可能會好奇的是，為什麼《理性與感性》和《傲慢與偏見》的餘弦相似度比《理性與感性》和《乘風破浪》的高？我們可以試著看看原因。我們要將這個與其他兩個進行比較。我們可以看到，《乘風破浪》向量的這個部分對於產生與《理性與感性》的相似度完全沒有幫助。《理性與感性》向量中最大的分量是這個。因此它與《傲慢與偏見》產生了很多相似度，那本書也突出地包含了這個詞，而這個詞在《乘風破浪》中的表現較少。因此，這裡的點積，這個點積中的這一項要大得多，所以我們得到了更大的相似度。

所以你可以看到，文件中不同單詞出現的比例對衡量整體相似度有很大影響。好的，我希望這個例子有助於使其更具體，並且你現在對資訊檢索的向量空間模型有了很好的理解。其核心思想是我們可以根據文件在高維向量空間中的角度相似度來對檢索結果進行排名。

---

## 重點摘要 (Key Summary)

- **向量空間模型基本概念**：文件被轉換為 V 維實數值向量，其中 V 是詞彙表中的單詞數量。詞項是空間的座標軸，文件是空間中的點或從原點出發的向量。
- **高維稀疏特性**：在實際系統（如網路搜尋引擎）中，向量空間可以有數千萬個維度，但每個向量非常稀疏，因為單個文件通常只包含幾百到幾千個單詞。
- **查詢也是向量**：查詢被視為同一向量空間中的向量，文件根據與查詢的接近程度來排名，這有別於布林模型的「全有或全無」方式。
- **歐幾里得距離的問題**：歐幾里得距離不是好的相似度度量，因為向量長度不同會導致距離很大，即使內容相似的文件也可能被判定為不相似。
- **使用角度取代距離**：將文件附加到自身後語意不變，但歐幾里得距離會變大；而兩個向量在同一直線上，角度為零，表示最大相似度。
- **餘弦相似度**：餘弦在 0 到 180 度之間是單調遞減函數，因此餘弦分數可以作為角度的反函數。使用向量運算可以高效計算餘弦值，無需計算超越函數。
- **向量長度正規化**：將向量除以其長度得到單位向量，使長文件和短文件具有可比較的權重。長度正規化後的餘弦相似度等同於正規化向量的點積。
- **餘弦相似度公式**：分子是兩個向量的點積，分母是兩個向量長度的乘積。其中 QI 是查詢中詞項 I 的 TF-IDF 權重，DI 是文件中的 TF-IDF 權重。
- **具體範例（珍．奧斯汀小說）**：使用對數頻率加權和長度正規化後，《理性與感性》與《傲慢與偏見》的餘弦相似度為 0.94，與《乘風破浪》為 0.79，說明不同單詞出現的比例對整體相似度有很大影響。
- **核心結論**：向量空間模型的核心思想是根據文件在高維向量空間中的角度相似度來對檢索結果進行排名。
