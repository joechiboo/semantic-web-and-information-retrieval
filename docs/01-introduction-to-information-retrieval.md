# Introduction to Information Retrieval (資訊檢索導論)

**影片連結：** https://www.youtube.com/watch?v=kNkCfaH2rxc

---

## 英文逐字稿 (English Transcript)

Hello, in this segment I am going to introduce the task of information retrieval, including in particular, what's now the dominant form: web search. The task of information retrieval can be maybe defined as follows. That our goal is finding material, which is usually documents, of an unstructured nature, usually text, that satisfies an information need, that's what the person is looking for information on, from within large collections, usually stored on computers. So there's lots of mentions there of prototypical cases and other kinds of information retrieval do exist. So there are things like music information retrieval where there are sounds, not text documents. But effectively, what we're going to talk about here is the case where all of those usually clauses hold.

There are many scenarios for information retrieval. The one that people think of first these days is almost invariably web search, But there are many others. So searching your email, searching the contents of your laptop computer, finding stuff in some company's knowledge base, doing legal information retrieval to find relevant cases for legal context or something like that.

It's always been the case that a large percentage of human knowledge and information is stored in the form of human language documents. And yet there's also for a long time been something of a paradox there. So this is just a kind of a not quite real graph to give a flavor of things. Don't really believe the numbers on the left-hand side are exactly what they mean. But what we're showing in the mid 1990's it was already the case that if you looked at the volume of data that there was some data that was in structured forms, by that I mean things like relational databases and spreadsheets, but there was already vastly more data in companies, organizations, and around people's homes that was in unstructured form, the form of human language text. However, despite that, in the mid 1990s structured data management retrieval was a developed field and there were already large database companies, where in the field of unstructured data management, there was very little. There were few teeny little companies that did various kinds of corporate document retrieval and things like that.

That situation just completely changed around the turn of the millennium. So, if we look today the situation is like this so the data volumes have gotten larger on both sides but in particular they've gotten larger on the unstructured side with massive outpouring of blogs, tweets, forums and all those other places that now store massive amounts of information. But there's also then been a turn around on the corporate side. So now we have huge companies that are addressing the problems of unstructured information retrieval, such as the major web search giants.

So let's start and just say a little bit about what are the base, what is the basic framework of doing information retrieval? So, we start off by assuming that we've got a collection of documents over which we are going to do retrieval. And, and at the moment we're going to assume that it's just a static collection. Later on we'll deal with, when documents get added to and deleted from that collection, and we can go out and find them in something like a web search scenario. Then our goal is to retrieve documents that are relevant to the user's information need, and helps the user complete a task.

Let me go through that once more a little bit more slowly with this picture. So at the start what we have is the user has some task that they want to perform. Let's take a concrete example. Suppose what I want to do is get rid of the mice that are in my garage and I'm the kind of person that doesn't really want to kill them with poison. So that's my user task that I want to achieve. And so to achieve that task, I feel what I need, more information, and so this is the information need. I want to know about getting rid of mice without killing them. This information need is the thing with respect to which we assess an information retrieval system. But we can't just take someone's information need and stick it straight into a computer. So what we have to do to be able to stick it into a computer is to translate the information need into something that goes into a search box. And so that's what's happened here, we now have a query. And so here's my attempt at a query, how trap mice alive, so that's taken this information need and I've made an attempt to realize it as a particular query. And so then it's that query that goes into the search engine, which leads, which then interrogates our document collection, and leads to some results coming back.

And that may be the end of the day, but sometimes if I'm not satisfied with how my information retrieval session is working, I might take the evidence I got from there and go back and come up with a better query. So I might decide that alive is a bad word and put in something like without killing, and see if that works any better.

Okay. What can go wrong here. Well there are a couple of stages of interpretation here. So first of all there was my initial task and I made some decisions as to what kind of information need I had. It could be that I got something wrong there, so I could have misconceptions. So maybe, getting rid of mice, the most Important issue is not whether or not I kill them, but whether I do it humanely. But we're not gonna deal with that issue so much. What we're more interested in here is the translation between the information need and the query. And there are lots of ways in which that could go wrong in misformulation of the query. So I might choose the wrong words to express the query, I might make use of query search operators like inverted commas, which might have a good or a bad effect on how the query actually works, And so those are choices in my query formulation which aren't altering my information need whatsoever.

That's important when we talk about how to evaluate information retrieval systems. That's a topic we'll say more about later, but let me just give you the first rough sense of this, cause we'll need it for everything that we do. So whenever we make a query to an information retrieval system, we're going to get some documents back and we want to know whether the results are good. And the very basic way in which we are gonna see whether they are good is as follows. We are going to think of two measures, which are complementary, one of which is precision. So precision is the fraction of the retrieved documents of the system that are relevant to the user's information needs. So that's whether, when you look at the results it seems like one document in ten is relevant to the information need you have or whether seven documents in ten are. That's assessing whether the mix of stuff you're getting back has a lot of bad results in it. The corres--, complementary measure is the one of recall. Recall is measuring how much of the good information that's in the document collection is the system succeeding in finding for you? The fraction of relevant docs in the collection that are retrieved.

We'll give more precise definitions and measurements for information retrieval later, but the one thing I want to express right now is that for these measures to make sense, they have to be evaluated with respect to the user's information need. For certain kinds of queries, such as the ones we'll look at in the following segments, the documents that get returned are deterministic in terms of what query is submitted. So if we were going, just going to evaluate what gets returned with respect to the user's query, then we'd necessarily say that the precision is 100%. But that's not what we do. What we do is think about the user's information need and the precision of the results is assessed relative to that. So in particular, if we just look back for a moment, if there's been a misformulation of the query by the user or just they didn't come up with a very good query that will be seen as lowering the precision of the returned results.

Okay. This is only the very beginning of our looking at information retrieval, but I hope you've already got a sense of how we think of the task of information retrieval and roughly how we conceive whether a search engine is doing a good or a bad job on it.

---

## 中文翻譯 (Chinese Translation)

大家好，在這個段落中，我將介紹資訊檢索的任務，特別包括目前最主流的形式：網路搜尋。資訊檢索的任務大致可以定義如下：我們的目標是從通常儲存在電腦中的大型集合裡，找到能夠滿足資訊需求（也就是使用者正在尋找的資訊）的素材，這些素材通常是文件，屬於非結構化的性質，通常是文字。所以這裡提到了很多典型的情況，而其他種類的資訊檢索確實也存在。例如音樂資訊檢索，處理的是聲音而非文字文件。但實際上，我們在這裡要談的是所有那些「通常」條件都成立的情況。

資訊檢索有許多應用場景。現今人們最先想到的幾乎都是網路搜尋，但還有許多其他場景。例如搜尋你的電子郵件、搜尋你筆記型電腦中的內容、在某家公司的知識庫中找東西、進行法律資訊檢索以找到與法律情境相關的案例等等。

一直以來，人類知識和資訊的很大一部分都是以人類語言文件的形式儲存的。然而長久以來這裡也存在某種矛盾。所以這只是一個不太精確的圖表，用來呈現大致的情況。不要太相信左邊的數字就是它們確切的含義。但我們要展示的是，在 1990 年代中期，如果你觀察資料量，會發現有些資料是結構化形式的，我指的是像關聯式資料庫和試算表之類的東西，但在公司、組織以及人們家中，已經有遠遠更多的資料是非結構化形式的，也就是人類語言文字的形式。然而，儘管如此，在 1990 年代中期，結構化資料管理與檢索已經是一個成熟的領域，而且已經有大型的資料庫公司存在；但在非結構化資料管理的領域中，幾乎什麼都沒有。只有少數幾家很小的公司在做各種企業文件檢索之類的事情。

這種情況在千禧年前後徹底改變了。所以，如果我們看看今天的情況是這樣的：兩邊的資料量都變大了，但特別是非結構化那一邊的資料量大幅增長，因為部落格、推文、論壇以及所有其他現在儲存了大量資訊的地方大量湧現。但在企業端也發生了翻轉。所以現在我們有大型公司在處理非結構化資訊檢索的問題，例如那些主要的網路搜尋巨頭。

那麼讓我們開始，先簡單介紹一下資訊檢索的基本框架是什麼？首先，我們假設我們有一個文件集合，我們將在這個集合上進行檢索。而且目前我們假設它只是一個靜態的集合。之後我們會處理文件被新增到集合中或從集合中刪除的情況，以及我們可以像在網路搜尋的場景中那樣去找到它們。然後我們的目標是檢索出與使用者資訊需求相關的文件，並幫助使用者完成任務。

讓我用這張圖片再更慢地講一遍。一開始，使用者有某個他們想要執行的任務。讓我們舉一個具體的例子。假設我想做的是清除車庫裡的老鼠，而我是那種不太想用毒藥殺死牠們的人。所以這就是我想要達成的使用者任務。為了達成這個任務，我覺得我需要更多的資訊，所以這就是資訊需求。我想知道如何在不殺死老鼠的情況下清除牠們。這個資訊需求就是我們用來評估資訊檢索系統的依據。但我們不能直接把某人的資訊需求塞進電腦裡。所以我們必須做的是將資訊需求轉換成可以放進搜尋框的東西。這就是這裡發生的事情，我們現在有了一個查詢。所以這是我嘗試的查詢：「how trap mice alive」（如何活捉老鼠），這是把資訊需求轉化成一個特定查詢的嘗試。然後這個查詢進入搜尋引擎，搜尋引擎查詢我們的文件集合，然後產生一些結果回來。

這可能就結束了，但有時候如果我對我的資訊檢索過程不滿意，我可能會利用得到的證據回頭想出一個更好的查詢。所以我可能會決定「alive」不是一個好詞，改成像「without killing」（不殺死）之類的，看看效果會不會更好。

好的。這裡可能會出什麼問題呢？嗯，這裡有幾個解讀的階段。首先，我有一個初始任務，然後我做了一些關於我有什麼樣的資訊需求的決定。有可能我在那裡就搞錯了，所以我可能有誤解。例如，清除老鼠最重要的問題可能不是我是否殺死牠們，而是我是否以人道的方式處理。但我們不太會處理那個問題。我們在這裡更感興趣的是資訊需求和查詢之間的轉換。在查詢的錯誤表述中，有很多地方可能出錯。所以我可能選錯了表達查詢的詞語，我可能使用了查詢搜尋運算子，像是引號，這可能對查詢實際運作產生好的或壞的影響。這些都是我在查詢表述中做的選擇，完全不會改變我的資訊需求。

這在我們談到如何評估資訊檢索系統時很重要。這個主題我們之後會多說一些，但讓我先給你一個粗略的概念，因為我們做的每件事都會需要它。所以每當我們向資訊檢索系統提出查詢時，我們會得到一些文件回來，而我們想知道這些結果是否好。我們判斷結果好壞的最基本方式如下。我們會考慮兩個互補的衡量指標，其中一個是精確率（Precision）。精確率是系統檢索出的文件中，與使用者資訊需求相關的文件所佔的比例。也就是說，當你查看結果時，十份文件中有一份與你的資訊需求相關，還是十份中有七份相關。這是在評估你得到的結果中是否夾雜了很多不好的結果。對應的互補衡量指標是召回率（Recall）。召回率衡量的是文件集合中的好資訊，系統成功為你找到了多少？也就是集合中相關文件被檢索出來的比例。

我們之後會給出更精確的資訊檢索定義和衡量方式，但我現在想表達的一件事是，要讓這些衡量指標有意義，它們必須相對於使用者的資訊需求來評估。對於某些類型的查詢，例如我們在接下來的段落中會看到的那些，所回傳的文件是由提交的查詢確定性地決定的。所以如果我們只是相對於使用者的查詢來評估回傳的結果，那麼我們必然會說精確率是 100%。但這不是我們做的事情。我們做的是考慮使用者的資訊需求，而結果的精確率是相對於資訊需求來評估的。所以特別是，如果我們回頭看一下，如果使用者錯誤地表述了查詢，或者他們就是沒有想出一個很好的查詢，這會被視為降低了回傳結果的精確率。

好的。這只是我們探討資訊檢索的開端，但我希望你已經對我們如何思考資訊檢索的任務、以及我們大致如何判斷一個搜尋引擎做得好不好有了一些概念。

---

## 重點摘要 (Key Summary)

- **資訊檢索的定義：** 從儲存於電腦中的大型集合裡，找到能滿足使用者資訊需求的非結構化文件（通常為文字）。
- **常見應用場景：** 網路搜尋、電子郵件搜尋、筆記型電腦內容搜尋、企業知識庫搜尋、法律資訊檢索等。
- **結構化 vs. 非結構化資料：** 1990 年代中期，非結構化資料量已遠超結構化資料，但當時結構化資料管理已是成熟領域，非結構化資料管理幾乎不存在。千禧年後，隨著部落格、推文、論壇等大量湧現，網路搜尋巨頭開始解決非結構化資訊檢索的問題。
- **資訊檢索的基本框架：** 假設有一個文件集合，目標是從中檢索出與使用者資訊需求相關、能幫助使用者完成任務的文件。
- **從任務到查詢的過程：** 使用者任務 -> 資訊需求 -> 查詢（輸入搜尋框的文字） -> 搜尋引擎檢索文件集合 -> 回傳結果。使用者可根據結果反覆調整查詢。
- **查詢表述的問題：** 使用者可能選錯詞語、誤用搜尋運算子等，導致查詢無法準確反映其資訊需求。評估系統時，是以使用者的資訊需求（而非查詢本身）作為基準。
- **精確率 (Precision)：** 系統回傳的文件中，與使用者資訊需求相關的文件所佔比例。衡量的是「回傳的結果中有多少是好的」。
- **召回率 (Recall)：** 文件集合中所有相關文件裡，被系統成功檢索出來的比例。衡量的是「好的資訊有多少被找到了」。
- **評估的關鍵原則：** 精確率和召回率必須相對於使用者的「資訊需求」來評估，而非相對於使用者提交的「查詢」。查詢表述不佳會導致精確率下降。
