# Semantic Networks - Additional Info (語意網路 - 補充資訊)

**影片連結：** https://www.youtube.com/watch?v=3PgIC9KcSNE

---

## 英文逐字稿 (English Transcript)

Hi everyone, assalamu alaikum. So I'm going to continue about knowledge presentation, and this time going to look into semantic network. So what is semantic network? Semantic network is actually a method of knowledge representation using a graph made of interconnected nodes and arcs. Semantic networks are excellent in supporting system analysis, demonstrating changes, and showing inheritance relationships.

So let's look at the example. Okay, we have a semantic network of a bird. Okay, the bird is an object, and this object has property that is wings and fly. So what can we interpret from this is a bird has wings and it can fly. So the bird has wings and travels by flying.

And then we have another object which is Canary, and this Canary is linked to another object Bird, and the relationship is "is a." So we read it as "Canary is a bird." So since a bird has wings and travels by flying, so we assume the same for Canary. So Canary also has wings and flies. Using the network, the system knows not only the objects and their properties but also the hierarchy and the inheritance.

So let's expand this network. Okay, we add Tweety here. Okay, Tweety is a Canary. Okay, and then we also have Animal, whereby Bird is an object from an Animal, and Animal breathes by air. Okay, so try and read this semantic network. Okay, and please look also about the penguin. Okay, whereby penguin travels while walking, not flying. So that's why penguin will have their own travel and walk object.

So how about inheritance in semantic network? Okay, it's like an object-oriented approach whereby you can see the inheritance between the objects, right? So from this network, okay, let's look at the first case. Okay, user asks "bird" -- okay, I actually asked the system "how does a bird travel?" So the system will look into the info with the network, the semantic network graph, and you will have "the bird travels by flying."

So if the network has been expanded, okay, we can ask "how does Tweety travel?" So infer again with the graphical representation, and we know that Tweety is a Canary and Canary flies. Okay.

So how about the exception handling? Okay, there are few things -- how do we handle exceptions? Okay, by explaining or introducing an object repeatedly for each object whereby they don't inherit from the superclass. For example, the penguin travels by walking rather than flying. Okay, since the first node looks locally for an answer to a question, and the answer of "walk" is provided to a "travel" question posed to the penguin. So if you ask Canary or Bird, they won't get the answer "by walking." Okay.

So this is an exercise for semantic network. Okay, and this is the advantages and disadvantages of semantic network. Okay.

Advantages: We can use deductive reasoning or inheritance, and show important associations between objects clearly, and follow the hierarchy of relationships easily. And it also provides flexibility in adding new nodes to be defined when needed.

However, disadvantages: It is not a complete knowledge representation, and lacks operational knowledge. We cannot also represent procedures or the importance of steps in semantic networks. Okay.

So look into the exercise I will give you in the open learning. Try to do this before you continue with the third video lecture on object attribute values. Thank you.

---

## 中文翻譯 (Chinese Translation)

大家好，祝大家平安。我將繼續關於知識表示的內容，這次我們要探討的是語意網路。那麼什麼是語意網路呢？語意網路實際上是一種知識表示的方法，它使用由互相連接的節點和弧所構成的圖形。語意網路在支援系統分析、展示變化以及顯示繼承關係方面表現優秀。

讓我們來看一個範例。好的，我們有一個關於鳥的語意網路。鳥是一個物件，這個物件具有「翅膀」和「飛行」的屬性。所以我們可以從中解讀出：鳥有翅膀，而且牠可以飛。也就是說，鳥有翅膀，並且透過飛行來移動。

接著我們有另一個物件是金絲雀（Canary），這個金絲雀連結到另一個物件「鳥」，而它們之間的關係是「is a（是一種）」。所以我們讀作「金絲雀是一種鳥」。既然鳥有翅膀並且透過飛行來移動，那麼我們對金絲雀也做出相同的假設。所以金絲雀也有翅膀並且會飛。透過使用這個網路，系統不僅知道物件和它們的屬性，還知道層級結構和繼承關係。

那麼讓我們來擴展這個網路。好的，我們在這裡加入 Tweety。Tweety 是一隻金絲雀。接著我們也有「動物」這個物件，其中鳥是動物的一個子類物件，而動物透過空氣來呼吸。好的，請嘗試閱讀這個語意網路。也請注意企鵝的部分，企鵝是透過走路來移動的，而不是飛行。所以企鵝會有自己的移動方式和走路的物件。

那麼在語意網路中的繼承是怎麼回事呢？好的，這就像物件導向的方法一樣，你可以看到物件之間的繼承關係，對吧？所以從這個網路來看，讓我們來看第一個案例。使用者詢問關於「鳥」的問題——其實我是問系統「鳥是如何移動的？」系統會在語意網路圖中查找資訊，然後你會得到答案：「鳥透過飛行來移動。」

那麼如果網路已經被擴展了，我們可以問「Tweety 是如何移動的？」系統再次透過圖形化表示進行推論，我們知道 Tweety 是一隻金絲雀，而金絲雀會飛。好的。

那麼例外處理呢？有一些情況——我們如何處理例外？透過為每個不繼承自父類別的物件單獨解釋或引入一個物件。例如，企鵝是透過走路來移動的，而不是飛行。由於第一個節點會在本地尋找問題的答案，而「走路」這個答案被提供給了針對企鵝提出的「移動」問題。所以如果你詢問金絲雀或鳥，它們不會得到「透過走路」的答案。

這是一個語意網路的練習。以下是語意網路的優點和缺點。

優點：我們可以使用演繹推理或繼承，清楚地顯示物件之間的重要關聯，輕鬆地遵循關係的層級結構。它還提供了在需要時新增新節點的靈活性。

然而，缺點是：它不是一個完整的知識表示方式，且缺乏操作性知識。我們也無法在語意網路中表示程序或步驟的重要性。

請查看我在開放學習平台上給你們的練習題。在繼續觀看第三個關於物件屬性值的影片講座之前，請先嘗試完成這個練習。謝謝！

---

## 重點摘要 (Key Summary)

- **語意網路的定義：** 語意網路是一種使用由互相連接的節點和弧所構成的圖形來進行知識表示的方法。
- **核心範例 -- 鳥的語意網路：**
  - 鳥 (Bird) 具有翅膀 (wings) 屬性，移動方式為飛行 (fly)。
  - 金絲雀 (Canary)「is a」鳥，因此繼承了鳥的屬性（有翅膀、會飛）。
- **繼承機制 (Inheritance)：**
  - 類似物件導向程式設計中的繼承概念。
  - Tweety 是金絲雀，金絲雀是鳥，因此 Tweety 繼承了鳥的所有屬性。
  - 動物 (Animal) 透過空氣呼吸，鳥是動物的子類，因此鳥也透過空氣呼吸。
- **例外處理 (Exception Handling)：**
  - 企鵝 (Penguin) 是鳥的一種，但移動方式是走路而非飛行。
  - 透過在本地節點直接定義屬性來覆蓋繼承的屬性，實現例外處理。
  - 系統會優先查找最近的本地節點答案。
- **語意網路的優點：**
  1. 可使用演繹推理和繼承機制。
  2. 能清楚顯示物件之間的重要關聯。
  3. 容易遵循關係的層級結構。
  4. 在需要時可靈活新增新節點。
- **語意網路的缺點：**
  1. 不是完整的知識表示方式。
  2. 缺乏操作性知識的表達能力。
  3. 無法表示程序（procedures）或步驟的重要性。
