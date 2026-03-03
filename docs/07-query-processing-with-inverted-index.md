# Query Processing with the Inverted Index (使用倒排索引的查詢處理)

**影片連結：** https://www.youtube.com/watch?v=5KbynCj7yRQ

---

## 英文逐字稿 (English Transcript)

In this segment, we're gonna keep on looking at the inverted index, and see how it's an efficient data structure for doing query operations in an IR system. And in particular, we'll step through in detail how you can perform a common kind of query, an AND query for two terms. So, starting off now, we'll look at the details of query processing. And then we'll have a later segment where we'll talk in even more detail about the kind of queries we can process. So suppose we want to process a query. So suppose our query is Brutus and Caesar. Well, let me even do a simpler example than that. Suppose the very first kind of query we want to look at is just a query for Brutus. Well, how to do that is totally straightforward, what we do is locate Brutus in the dictionary and then we return its postings list that we look up and say okay this is the set of documents where Brutus occurs and we don't need to do anything else. But now let's go to that fraction more complicated case. Well then we're going to locate, for Brutus and Caesar, we're going to locate both the words in the dictionary, look up their postings lists, and what we'd like to do is then work out what are the documents that contain both Brutus and Caesar. And doing the putting them together is standardly referred to as merging the two postings lists. Now that term can actually be misleading because what we're doing for an AND query is we're actually intersecting the two sets of documents to find the documents that, in which both words occur. Whereas merging suggests doing some kind of putting them together in a union operation. But the term merge is used actually in both cases. So the merge algorithm family refers to a family of algorithms where you can step through a pair of sorted lists and do various Boolean operations on that. Let's look in concrete detail how that happens. Okay, so the way we do a merge operation to do Brutus and Caesar is like this. We start with a pointer which points at the head of both lists, And what we're going to be wanting to do is then work out what's in the intersection. So the way we do that is we ask are these two pointers pointing at the same, an equal doc ID. And the answer is no. And so what we do is then advance the pointer that has the smaller doc ID. So now I have two pointers like this and we say does, is, are the two pointers pointing at the same document ID? And here the answer is yes. So we put that into our result list and then if we've done that, we can then advance both pointers. We now say, are these pointers both pointing at the same doc ID? No. Is the first list greater, first, the thing pointed to by the first list pointer greater than the thing pointed to by the second list pointer? No, so we advance the bottom pointer one. Then we say, is the doc ID pointed at by the two pointers equal? No, and so again, we advance the smaller one. Equal, no, advance the smaller one. At this point, they're again both pointing at the same doc ID. So we add that to our result set, and we advance both pointers. Are they the same? No, What we do is advance the smaller one. Are they the same? No, we advance the smaller one. Same, no, advance the smaller one. Same, no, advance the smaller one. Same, no. And at this point, when we try and advance the smaller one, one of our lists are, is exhausted. And so then there can be no other items in the intersection and so we can stop. And so this is our return document set. Documents two and eight contained both Brutus and Caesar. So I hope we went through that carefully enough that you can see if the lists lengths are X and Y then this merge algorithm takes big O X plus Y time. That it's linear in the sum of the lengths of the two postings lists. And you should also have seen what's crucial to make this operation linear and what's crucial to making it linear is the fact that these postings lists were sorted in order of document ID. Precisely because of that, we could do a linear scan through the two postings lists, where if that hadn't been the case, then it would have turned into an N squared algorithm. Okay. Here's the postings list intersection algorithm one more time, as a real algorithm, but hopefully you can see it's doing exactly the same as what I was by hand. So we start here with the answer set as zero. And then we're going to be doing this while loop while the postings lists are both not equal to nil, cause as soon as one's nil, we can stop. So that's the and operation. Okay, so then at each step, what we do is ask whether the two, the document ID of the two pointers is the same. If so we add it to our answer. If not and sorry, and if they are the same we can advance both pointers and if not, we work out which doc ID is smaller and then we advance that pointer, so either this one or this one. And that was exactly what I was doing and then as soon as one of the document lists runs out, we can return our answer set. Okay, I hope that made sense and you now feel like you can write your own code to do the intersection of postings lists using the merge algorithm.

---

## 中文翻譯 (Chinese Translation)

在這個段落中，我們將繼續研究倒排索引，看看它如何作為一個高效的資料結構來執行資訊檢索系統中的查詢操作。特別是，我們將詳細地逐步說明如何執行一種常見的查詢類型——兩個詞項的 AND 查詢。那麼，現在開始，我們將看查詢處理的細節。之後會有另一個段落，我們會更詳細地討論我們可以處理的查詢類型。

假設我們想要處理一個查詢。假設我們的查詢是 Brutus AND Caesar。好吧，讓我先做一個比那更簡單的例子。假設我們要看的第一種查詢只是查詢 Brutus。要做到這一點完全是直截了當的，我們所做的就是在字典中找到 Brutus，然後返回我們查到的它的張貼列表，然後說好，這就是 Brutus 出現的文件集合，我們不需要做其他任何事情。

但現在讓我們看稍微複雜一點的情況。那麼對於 Brutus AND Caesar，我們要在字典中找到這兩個詞，查找它們的張貼列表，然後我們想要找出哪些文件同時包含 Brutus 和 Caesar。將它們組合在一起的操作在標準術語中被稱為合併（merging）兩個張貼列表。這個術語實際上可能會造成誤導，因為對於 AND 查詢，我們實際上是在對兩組文件取交集，以找到兩個詞都出現的文件。而「合併」暗示的是某種聯集操作，把它們放在一起。但「合併」這個術語實際上在兩種情況下都被使用。所以合併演算法家族指的是一系列演算法，你可以逐步走過一對已排序的列表，並對其進行各種布林運算。

讓我們具體詳細地看看這是如何發生的。好的，我們執行合併操作來處理 Brutus AND Caesar 的方式如下。我們從一個指向兩個列表頭部的指標開始，我們想要做的就是找出交集中有什麼。我們的做法是問這兩個指標是否指向相同的、相等的文件 ID。答案是否。所以我們所做的就是推進具有較小文件 ID 的那個指標。

現在我有兩個這樣的指標，我們問這兩個指標是否指向相同的文件 ID？這裡答案是的。所以我們把它放入我們的結果列表中，然後如果我們這樣做了，就可以同時推進兩個指標。

我們現在問，這兩個指標是否都指向相同的文件 ID？不是。第一個列表指標所指的值是否大於第二個列表指標所指的值？不是，所以我們推進下面那個指標一步。然後我們問，兩個指標所指的文件 ID 是否相等？不是，所以我們再次推進較小的那個。相等嗎？不是，推進較小的那個。

此時，它們再次都指向相同的文件 ID。所以我們將其加入結果集，並推進兩個指標。它們相同嗎？不是。我們所做的就是推進較小的那個。它們相同嗎？不是，推進較小的那個。相同嗎？不是，推進較小的那個。相同嗎？不是，推進較小的那個。相同嗎？不是。

而此時，當我們試圖推進較小的那個時，我們的其中一個列表已經耗盡了。因此不可能再有其他項目在交集中，所以我們可以停止了。這就是我們返回的文件集合。文件 2 和文件 8 同時包含了 Brutus 和 Caesar。

所以我希望我們足夠仔細地走過了這個過程，讓你們能看到如果列表長度分別是 X 和 Y，那麼這個合併演算法的時間複雜度是 O(X + Y)。它與兩個張貼列表長度之和呈線性關係。你們也應該已經看到了使這個操作成為線性的關鍵因素，而使其成為線性的關鍵在於這些張貼列表是按文件 ID 的順序排序的。正是因為如此，我們才能對兩個張貼列表進行線性掃描，如果不是這樣的話，它就會變成一個 N 平方的演算法。

好的。這裡再次展示張貼列表交集演算法，作為一個真正的演算法，但希望你們可以看到它做的事情與我剛才手動做的完全一樣。所以我們從這裡開始，將答案集設為空。然後我們要執行這個 while 迴圈，只要兩個張貼列表都不等於 nil，因為只要有一個是 nil，我們就可以停止了。這就是 AND 操作。

好的，那麼在每一步中，我們所做的是問兩個指標的文件 ID 是否相同。如果是的話，我們就把它加入答案中。如果不是——抱歉，如果它們相同，我們可以同時推進兩個指標；如果不同，我們找出哪個文件 ID 較小，然後推進那個指標，所以不是這個就是那個。這就是我剛才所做的事情，然後一旦其中一個文件列表用完了，我們就可以返回我們的答案集。

好的，我希望這講得很清楚了，現在你們覺得自己可以撰寫自己的程式碼，使用合併演算法來做張貼列表的交集運算。

---

## 重點摘要 (Key Summary)

- **單詞查詢的處理**：對於只查詢一個詞項（如 Brutus）的情況，只需在字典中找到該詞並返回其張貼列表即可，非常直接。
- **AND 查詢的處理**：對於兩個詞項的 AND 查詢（如 Brutus AND Caesar），需要在字典中找到兩個詞，取得各自的張貼列表，然後對兩個列表進行交集運算。
- **合併演算法（Merge Algorithm）**：這是一個逐步走過兩個已排序列表的演算法家族，可以對其執行各種布林運算（交集、聯集等）。雖然稱為「合併」，但在 AND 查詢中實際上是在做交集運算。
- **交集運算的具體步驟**：
  1. 在兩個列表的頭部各放置一個指標
  2. 比較兩個指標所指的文件 ID
  3. 如果相同，將該文件 ID 加入結果集，並同時推進兩個指標
  4. 如果不同，推進指向較小文件 ID 的指標
  5. 當任一列表耗盡時，停止運算
- **時間複雜度**：合併演算法的時間複雜度為 O(X + Y)，其中 X 和 Y 分別是兩個張貼列表的長度，與列表長度之和呈線性關係。
- **排序的關鍵作用**：張貼列表按文件 ID 排序是使交集運算達到線性時間複雜度的關鍵。如果列表未排序，演算法將退化為 O(N^2) 的時間複雜度。
- **演算法實作要點**：使用 while 迴圈，在兩個列表都非空時持續運行；每步比較文件 ID，相等則加入結果並推進兩個指標，不等則推進較小者的指標。
