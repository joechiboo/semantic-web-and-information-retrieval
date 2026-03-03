# Evaluating Search Engines (搜尋引擎評估)

**影片連結：** https://www.youtube.com/watch?v=b7pfLpVBN84

---

## 英文逐字稿 (English Transcript)

In this section I'll tell you a little bit more about evaluating the quality of a search engine. There are many measures for the quality of a search engine. There are technical ones such as how fast does it index, and how fast does it search. We can look at things like the expressiveness of the query language, whether they're able to express complex informational needs with things like phrase queries, negations, disjunctions. People have other desires like having an uncluttered UI and a system that doesn't cost a lot to use. All of these are measures that are measurable. That we can quantify them and we can get some, some kind of score of what is their goodness. But in practice all of those measures while important tend to be dominated by another measure of user happiness that, is the user happy in using this search engine? And speed of response and size of the index are certainly factors. But by themselves, blindingly fast useless answers won't make a user happy. So a huge part of user happiness is, are the results returned the results that they want? And so that's the metric of relevance of results to a user's information need. I mentioned this right at the beginning, but just to reiterate once more, when evaluating an IR system that we evaluate with respect to an information need. So an information need is translated into a query, and that's what the IR system actually runs. But relevance is assessed relative to the information need, not the query. So for example, if the information need is the person's looking for information on whether drinking red wine is more effective than white wine for reducing your risks of heart attacks, they'll come up with some query. For example it might be wine red white heart attack effective. And that will be submitted to a search engine. And in evaluating the effectiveness of the search engine in returning relevant results, we're not asking are the results that the search engine returns documents that simply have those words on the page. Rather, we're saying do these documents address the user's information need. Okay, well how can we go about doing that? Well, if the search engine returns a set of results. Well, then, what we can do for evaluation is if we start off with three things, if we have some benchmark collection of documents that we can use for evaluation. And we have some benchmark set of queries, which are in some sense representative of information needs of interest. And then we've gathered this third thing which is assessor judgments of whether particular documents are relevant to particular queries. Commonly in practice this can't be assembled exhaustively, certainly not if the document collection is large. But at least for a particular set of documents that are returned by particular search engines, we can get the assessor to judge whether those documents are relevant to the queries. Well, if we have a result set with just these three things, we're in business because we can use exactly the same measures that we looked at previously: precision, recall, and the F measure that combines them. And these are suitable good measures for exactly the same reason that they are good measures for when we're talking about things like named entity recognition. That normally only a few documents will be relevant to a particular query, and so we can measure that much better by looking at these measures of precision and recall. But what if we've now moved on to a search engine that returns ranked results. We can't just, totally straightforwardly use these measures of precision, recall, and F measure, because the system can return any number of results. In fact the number it returns normally depends on how often we keep on clicking asking for more. But if we sort of look at any initial subset of the results, we can then work out the precision recall for that subset. And then by putting them together we can come up with a precision recall curve. Let's look at how that works. So here are the first ten results for a search engine, where we've labeled each result as either relevant or not relevant according to an assessor's judgment. So then we can take any initial sub sequence of these documents and work out a recall and precision. So for the first document, the system got it right, it's a relevant document. And let's assume that overall there are ten relevant documents in the collection. So it's gotten one out of the ten relevant documents, and so its recall is 0.1. And well since that document was relevant, the system was right on the first answer, its precision is one at this point. Well, the next document was not relevant so the recall of the first two documents, we're down to here now, is 0.1, and the precision is now 0.5. Another not relevant document so the recall was still 0.1, and the precision is now dropped to 0.33. And the, if we look at the set of the top four documents we've now found two of the ten relevant ones, so recall is 0.2, and our precision has gone back up again to 0.5. The fifth one is also relevant so now our recall is up to 0.3, and our precision is up to three out of five, 0.6, then we can keep on going down. Maybe you guys could work out what some of these entries are down here. The other measure I want to mention, one of the most recently, most used recent measures is mean average precision. If we look at the ranked retrieval results ordered this way to give me a bit more room. And so the first document returned is relevant. The second one is not relevant. Say, the third one is not relevant. Then a relevant one, then another relevant one, not relevant, relevant, relevant. Let's say those are our top eight results. What you're doing for mean average precision, first of all you're working in average precision for one query. And so the way you do that is by saying, let's work out the precision at each point that a relevant document is returned, cause that's when you're increasing recall. So here, the precision is one. Here, there are now four documents so the precision is a half. Here there are five documents so the precision is 0.6. Here there are seven documents of which, four of them are relevant. So that's this is around 0.58. You guys can correct my arithmetic. Here we now have eight documents, of which five are relevant, and that's 0.625 and then what we're doing to work out the mean average precision is we're kind of keeping on calculating those numbers. In practice, normally, they aren't calculated exhaustively, but they're calculated up to some point, let's say 100. And then you're calculating an average function of all those numbers. And that's then the average precision for one query. You then calculate the same average precision for all the other queries in your benchmark query collection. And you would again take the average of that and that then gives you mean average precision. So, in particular, this is what's referred to as macro-averaging. It's each query that counts equally in the calculation of mean average precision. So this is a good measure that evaluates to some extent, precision at different recall levels, while still being weighted most to what the precision is like for the top few returned documents. Then at the level of across different queries, it's giving equal weight to different queries, which tends to be a useful thing to do because you are always interested in how systems return, work on queries of rare terms as well as queries of common terms. So this is a pretty good measure to think about using for evaluating information retrieval systems. Okay there's even more methods that I could talk about, but that's probably a good sense of how about, how to go about evaluating the performance of a ranked retrieval system.

---

## 中文翻譯 (Chinese Translation)

在這一節中，我會多告訴你一些關於如何評估搜尋引擎品質的內容。衡量搜尋引擎品質的標準有很多。有技術性的標準，例如索引建立的速度有多快，搜尋的速度有多快。我們可以查看查詢語言的表達能力，例如它們是否能夠用片語查詢、否定、析取等方式來表達複雜的資訊需求。人們也有其他的期望，比如擁有整潔的使用者介面和使用成本不高的系統。

所有這些都是可衡量的指標。我們可以量化它們，並得到某種品質分數。但在實踐中，所有這些指標雖然重要，往往會被另一個使用者滿意度的指標所主導，那就是：使用者在使用這個搜尋引擎時是否開心？

回應速度和索引大小當然是因素。但光靠這些，快得令人眼花繚亂但毫無用處的答案不會讓使用者開心。所以使用者滿意度的很大一部分在於，返回的結果是否是他們想要的？這就是結果與使用者資訊需求的相關性指標。

我在一開始就提到了這一點，但再重申一次，當評估一個資訊檢索系統時，我們是根據資訊需求來評估的。資訊需求被翻譯成查詢，那才是資訊檢索系統實際運行的內容。但相關性是相對於資訊需求來評估的，而不是相對於查詢。

舉例來說，如果資訊需求是一個人想要尋找關於喝紅酒是否比白酒更能有效降低心臟病風險的資訊，他們會想出某個查詢。例如可能是「wine red white heart attack effective」（紅酒白酒心臟病有效）。這將被提交給搜尋引擎。在評估搜尋引擎返回相關結果的有效性時，我們不是在問搜尋引擎返回的結果是否只是頁面上簡單地包含那些詞的文件。相反地，我們是在問這些文件是否解決了使用者的資訊需求。

好的，那我們該怎麼做呢？如果搜尋引擎返回一組結果。那麼我們可以做的評估是，如果我們先有三樣東西：如果我們有一些可以用來評估的基準文件集合；如果我們有一些基準查詢集，在某種意義上代表了感興趣的資訊需求；然後我們收集了第三樣東西，即評審員對於特定文件是否與特定查詢相關的判斷。

通常在實踐中，這不可能被完整地組裝，當然如果文件集合很大的話就更不可能了。但至少對於由特定搜尋引擎返回的特定文件集，我們可以讓評審員判斷這些文件是否與查詢相關。

如果我們有一個包含這三樣東西的結果集，我們就可以開始了，因為我們可以使用與之前完全相同的度量：精確率、召回率和結合它們的 F 度量。這些是合適的好度量，原因與它們在我們談論命名實體識別等事情時是好度量完全相同。通常只有少數文件與特定查詢相關，所以我們可以透過查看這些精確率和召回率的度量來更好地衡量。

但如果我們現在已經轉向了一個返回排名結果的搜尋引擎呢？我們不能完全直接地使用精確率、召回率和 F 度量這些指標，因為系統可以返回任意數量的結果。事實上，它返回的數量通常取決於我們持續點擊要求更多的頻率。

但如果我們看結果的任何初始子集，我們就可以計算出該子集的精確率和召回率。然後通過把它們組合在一起，我們可以得到一條精確率-召回率曲線。讓我們看看這是怎麼運作的。

這裡是搜尋引擎的前十個結果，其中我們根據評審員的判斷將每個結果標記為相關或不相關。然後我們可以取這些文件的任何初始子序列，計算召回率和精確率。

對於第一個文件，系統做對了，它是一個相關文件。假設集合中總共有十個相關文件。所以它找到了十個相關文件中的一個，因此它的召回率是 0.1。由於該文件是相關的，系統在第一個答案上是正確的，此時它的精確率是一。

第二個文件不相關，所以前兩個文件的召回率，我們現在到了這裡，是 0.1，精確率現在是 0.5。又一個不相關的文件，所以召回率仍然是 0.1，精確率現在降到了 0.33。

如果我們看前四個文件的集合，我們現在找到了十個相關文件中的兩個，所以召回率是 0.2，精確率又回升到 0.5。第五個也是相關的，所以現在我們的召回率上升到 0.3，精確率上升到五分之三，即 0.6，然後我們可以繼續往下算。也許你們可以算出下面一些項目的數值。

我想提到的另一個指標，也是最近最常使用的指標之一，是平均精確率均值（Mean Average Precision，MAP）。如果我們按這種方式排列排名式檢索結果，給我多一點空間。

第一個返回的文件是相關的。第二個不相關。假設第三個不相關。然後一個相關的，然後又一個相關的，不相關，相關，相關。假設這些是我們的前八個結果。

對於平均精確率均值，你要做的首先是計算一個查詢的平均精確率。做法是這樣的：讓我們在每個返回相關文件的點計算精確率，因為那是你增加召回率的時候。

所以在這裡，精確率是一。在這裡，現在有四個文件，所以精確率是二分之一。這裡有五個文件，所以精確率是 0.6。這裡有七個文件，其中四個是相關的，所以大約是 0.58。你們可以校正我的算術。這裡我們現在有八個文件，其中五個是相關的，那就是 0.625。

然後我們要做的是計算平均精確率均值，就是持續計算這些數字。在實踐中，通常它們不會被完整計算，但會計算到某個點，比如說 100。然後你計算所有這些數字的平均值。這就是一個查詢的平均精確率。

然後你對基準查詢集中的所有其他查詢計算相同的平均精確率。你再取這些的平均值，那就得到了平均精確率均值。

特別是，這就是所謂的巨觀平均（macro-averaging）。在平均精確率均值的計算中，每個查詢的權重是相等的。

所以這是一個好的指標，它在某種程度上評估了不同召回率水準下的精確率，同時仍然最重視前幾個返回文件的精確率。在跨不同查詢的層面上，它給予不同查詢相等的權重，這往往是一件有用的事情，因為你總是對系統如何處理罕見詞項的查詢以及常見詞項的查詢都感興趣。

所以這是一個在評估資訊檢索系統時值得考慮使用的相當好的指標。好的，還有更多的方法我可以談論，但這大概已經讓你了解了如何評估排名式檢索系統性能的好方法。

---

## 重點摘要 (Key Summary)

- **搜尋引擎品質的多種衡量標準**：包括索引速度、搜尋速度、查詢語言表達能力、使用者介面整潔度和使用成本等，但這些往往被使用者滿意度所主導。
- **使用者滿意度的核心是相關性**：再快的速度也無法彌補無用的結果。使用者最在意的是搜尋結果是否符合他們的資訊需求。
- **以資訊需求評估，而非以查詢評估**：資訊需求被翻譯成查詢，但相關性是相對於原始資訊需求來判斷的，而不是僅僅看文件是否包含查詢中的詞。
- **評估所需的三要素**：(1) 基準文件集合；(2) 代表性的基準查詢集；(3) 評審員對文件與查詢相關性的判斷。
- **精確率與召回率**：可以用於評估搜尋引擎，與命名實體識別等任務中使用的原因相同——通常只有少數文件與特定查詢相關。
- **排名式結果的精確率-召回率曲線**：由於排名式搜尋引擎可以返回任意數量的結果，我們可以對結果的每個初始子集計算精確率和召回率，組合成精確率-召回率曲線。
- **精確率-召回率的變化範例**：前十個結果中，隨著查看的文件數增加，精確率和召回率會隨相關/不相關文件的出現而波動變化。
- **平均精確率均值 (MAP)**：最常使用的評估指標之一。先計算每個查詢的平均精確率（在每個相關文件被返回的點計算精確率，然後取平均），再對所有查詢的平均精確率取平均。
- **巨觀平均 (Macro-averaging)**：MAP 使用巨觀平均，每個查詢在計算中權重相等，這確保了對罕見詞項和常見詞項的查詢都給予同等關注。
- **MAP 的優點**：能在一定程度上評估不同召回率水準下的精確率，同時最重視前幾個返回文件的精確率，是評估資訊檢索系統的良好指標。
