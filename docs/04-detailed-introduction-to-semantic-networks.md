# Detailed Introduction to Semantic Networks (語意網路詳細介紹)

**影片連結：** https://www.youtube.com/watch?v=sY0kbo251A4

---

## 英文逐字稿 (English Transcript)

Oh it's my layer of money Rahim assalamu alaikum this is lecture 17 of the artificial intelligence course in order to solve various problems and to draw some conclusions we often have information already stored in our brain that we can utilize but how is that information stored in our brain there are a lot of possibilities today we are focusing one of them which is the semantic semantic Network we will see how what is the meaning of semantic network and we'll also talk about nodes and arts in semantic network with examples in the last lectures we have looked into different knowledge representation scheme namely the propositional logic and first-order logic or predicate logic today we'll start discussing on another mode of representation of knowledge known as semantic nets the word semantics means meaning as a computer science students you are already familiar with two words Centex which is essentially the grammar of a language and semantics is the meaning of any sentence so I may form the sentence correctly which means it may be syntactically correct but it must be meaningful in order to be meaningful it should be semantically correct when do you say a particular sentence or statement is meaningful the sentence is meaningful when we can really understand it and make it to some of the known concepts of the real world in which we live or see or can visualize whatever we look at for example if I look at this room then I will be looking at different chairs tables etc now each of these are different concepts and the chip for example is made above good there can be chairs which are not made of food that may be made of iron steel or some other material so whenever we talk of chair we can think up some other associations related to the chair similarly whenever we use a word say a boy then it got so many other associations a wine will be at most of Si and ten years old he will be having heart we have been weighed and usually maybe going to school so there are so many other associations that come up with a concern so when will we use any particular word we are actually referring to some concept and along with that concept we immediately associate some other related concept and this association of the different concepts builds up our knowledge system our our knowledge base this is another view of looking at knowledge that knowledge can be represented as a network of different concept any collection of facts or information cannot be knowledge unless it is used for inferring some new facts if we consider semantic net as a knowledge representation scheme then it must also have some particular inference mechanism by which it can utilize this representation to infer new things to answer different questions the idea of semantic nets dates back to 1966 in two very important papers that were written by eros Quillin who was one of the early workers of artificial intelligence he tried to represent the organization of human semantic memory or knowledge as a hierarchical Network it is huge for analyzing meanings of words within sentences semantic network is simple representation scheme which chooses a directed graph consisting of nodes which represent concepts and directed arcs to which represents a manipulation between the concepts in this concepts can be represented as hierarchies of interconnected concept nodes for example it is very natural to draw the link between cats and animals to say that cats are animals a concept may form a number of associative attributes at a given level animal has heard an animal can whoa this is one level cat is on another level where there is another Association attached to it cat likes mate this association is not related with on the with all animals this is in this graph it is only associated with the cat you nodes in the semantic network represent objects that may object my name attribute or any attribute value and the arcs are links define binary relations which hold between objects denoted by the nodes on the right side on the right there is a propositional logic in front of which is the equivalent semantic nets where the nodes represents the objects and gear links are the predicates that are in the propositional logic the structure of the network defined its meaning the meanings are merely which help which node has appointed to which other node the network defines a set of binary relations on a set of nodes to begin simply let us introduce two nodes and a link you Kent is a market the Lord on the nightly world can't is linked to the note on the left labeled market and the arrow is labeled is can't is an example of a market the diagram in other words represents the fact that there is a binary relation between a market camp and the concept of a market another node with the label Roger version and is a link from this node to the market node could be aided again representing that browser Bazaar is a Tulpa marquee if a retailer node is added to this figure the structure of the network becomes as markets journey contain retaining entities to an example of a retailer we ate unknown label ethnic garments and rulings one from the retailer and government ferrata was are labeled is and one from the note I'm at garments to the load retailer this illustrates that Anmuth garment is one instance of such a retailer in the Raja Mossad now it is important to note that the node labeled market represents the generic on meta concept of a market it can be thought of as possessing properties common to all markets the node browser bazaar represents a particular market the node retailer until represents the concept of a retailer that is common across all particularly tailors and hammock government is one instance of such a retailer we can distinguish the two types of nodes using boxes and circles semantic Network representation consists of four parts the lexical part includes nodes arts odd links and their labels the structural part shows that how the links and nodes form a directed graph the procedural part specifies the access procedures that is to create modify the nodes and to generate answer questions if constructor is a procedure then it will allow creation of new links and nodes similarly if destructor are modified is a procedure then it will do their actions modify will modify the nodes and the destructor will allow to delete the links and nodes semantics establishes the way our associating the meaning of the loads attached to them attached with the link inheritance is an important property of semantic nets the idea of this is that if an object belongs to a class it inherits all the properties of that class and can represent it in general if concept X has property P then all concepts that are a subset of X should also have property P in this example if we see Robin is a bird and bird is animal and bird has wings then Robin red is a Robin and rusty is a Robin then red and rusty both must have the properties of bird which in this example the property of bird is that has wings so rusty and red must have wings because they inherited this property from their superclass non binary relations we have seen how binary relationships may be represented by arcs in the semantic nets but what about relationships with more than two arguments for example how we can represent the sentence John gave Mary the book in the semantic networks in predicate logic we could have a 3-ary predicate whose first argument is the giver second argument the object that is given and third argument is the person to whom it was given this way this can be resolved is to consider the act of giving a separate object we can represent the generic gift event as a relation involving three things in the semantic network a giver a recipient and an object this is also known as conceptual graph conception graphs are semantic nets representing the meaning of sentences in natural language another example of a conceptual graph can be seen in this graph John goes to New York by bus this is an example of a propositional logic if a farmer owns a donkey then he beats it this can be converted into semantic net and this graph can again be translated to the following predicate logic this is equivalent to graph matching a question network is generated for each question we get an answer when the question network matched to a sub graph of the semantic network if a graph is given and a question is asked then following the links between the nodes one can deduce the answer so this is an example of how answers can be generated using semantic networks just follow the links and nodes and conclude the answer WordNet is an example of a semantic network which is a lexical database of English groups English words into sets of synonyms called synsets provides short general definition and records the various semantic relations between these synonym sets these are some of the advantages of semantic networks they are simple and can be easily implemented and understood the semantic network is more natural than the logical representation it permits using of effective graphical algorithms they are efficient in space requirements as objects are represented once and the relationships are handled by pointers they are easy to translate into Prolog and nowadays in Python some of the applications are semantic networks include document processing question processing query expansion we can use semantic networks in searching it can be used in answer generation and answer selection

---

## 中文翻譯 (Chinese Translation)

奉至仁至慈的真主之名，祝大家平安。這是人工智慧課程的第 17 講。為了解決各種問題並得出一些結論，我們通常會利用已經儲存在大腦中的資訊。但是，這些資訊是如何儲存在我們大腦中的呢？有很多種可能性，今天我們將聚焦其中一種，那就是語意網路。我們將了解語意網路的含義是什麼，並且透過範例來討論語意網路中的節點和弧。

在之前的課程中，我們已經探討了不同的知識表示方案，包括命題邏輯和一階邏輯（又稱謂詞邏輯）。今天我們將開始討論另一種知識表示方式，稱為語意網路。「語意」(semantics) 這個詞的意思是「含義」。作為電腦科學的學生，你們已經熟悉兩個詞：「語法」(syntax)，它本質上是語言的文法規則；以及「語意」(semantics)，它是任何句子的含義。所以我可能正確地構成了一個句子，這意味著它在語法上可能是正確的，但它必須是有意義的。為了有意義，它應該在語意上是正確的。

什麼時候你會說一個特定的句子或陳述是有意義的呢？當我們能夠真正理解它，並將其對應到我們所生活、所見或能想像的現實世界中某些已知的概念時，這個句子就是有意義的。不論我們看什麼，例如，如果我看這個房間，我會看到不同的椅子、桌子等。這些都是不同的概念。例如，椅子是用木頭做的，也可能有些椅子不是用木頭做的，可能是用鐵、鋼或其他材料做的。所以每當我們談到椅子時，我們可以聯想到與椅子相關的其他關聯。

同樣地，每當我們使用一個詞，比如說「男孩」，它就有很多其他的關聯。一個男孩最多大約六到十歲，他會有頭髮，有一定的體重，通常可能會去上學。所以有很多其他的關聯與一個概念一起出現。因此，當我們使用任何特定的詞時，我們實際上是在指稱某個概念，並且伴隨著那個概念，我們會立即聯想到一些其他相關的概念。這些不同概念之間的關聯構建了我們的知識系統，我們的知識庫。

這是看待知識的另一種觀點：知識可以表示為不同概念的網路。任何事實或資訊的集合都不能成為知識，除非它被用於推論一些新的事實。如果我們將語意網路視為一種知識表示方案，那麼它也必須具有某種特定的推論機制，透過這種機制它可以利用這種表示來推論新事物、回答不同的問題。

語意網路的概念可以追溯到 1966 年，由 Ross Quillian 撰寫的兩篇非常重要的論文。他是人工智慧的早期研究者之一，他試圖將人類語意記憶或知識的組織表示為一個層級式網路。這對於分析句子中詞語的含義非常有用。

語意網路是一種簡單的表示方案，它選擇使用有向圖，由代表概念的節點和代表概念之間關係的有向弧組成。在這種方案中，概念可以表示為互相連接的概念節點的層級結構。例如，在貓和動物之間建立連結來表示「貓是動物」是非常自然的。

一個概念在特定層級上可以形成多個關聯屬性。動物有頭髮，動物可以走路——這是一個層級。貓在另一個層級上，那裡有另一個與之相關的關聯：貓喜歡牛奶。這個關聯與所有動物無關，在這個圖中它僅與貓相關。

語意網路中的節點代表物件，物件可以是名稱、屬性或任何屬性值。弧是連結，定義了節點所表示的物件之間的二元關係。在右側是命題邏輯，而其前面是等價的語意網路，其中節點代表物件，而連結就是命題邏輯中的謂詞。

網路的結構定義了它的含義。含義僅僅在於哪個節點指向了哪個其他節點。網路在一組節點上定義了一組二元關係。

為了從簡單開始，讓我們引入兩個節點和一條連結。「坎特」(Cant) 是一個市場。右側節點上的標籤「坎特」連結到左側標籤為「市場」的節點，箭頭標記為「is」。坎特是市場的一個實例。換句話說，這個圖表示的是在「坎特市場」和「市場」概念之間存在一個二元關係。

另一個標籤為「拉賈巴扎」(Raja Bazaar) 的節點，以及從該節點到市場節點的一條連結，同樣表示拉賈巴扎也是一個市場。

如果在這個圖中加入一個「零售商」節點，網路的結構就變成了：市場包含零售實體。作為零售商的一個範例，我們加入一個標籤為「安穆特服裝」(Anmuth Garments) 的未知節點，畫兩條線——一條從零售商到安穆特服裝，標記為「is」，一條從安穆特服裝到零售商節點。這說明了安穆特服裝是拉賈巴扎中這類零售商的一個實例。

現在需要注意的是，標記為「市場」的節點代表市場的通用或元概念，可以認為它擁有所有市場共同的屬性。「拉賈巴扎」節點代表一個特定的市場。「零售商」節點代表所有特定零售商共同的零售商概念，而「安穆特服裝」是這類零售商的一個實例。我們可以使用方框和圓形來區分這兩種類型的節點。

語意網路表示由四個部分組成：

第一，**詞彙部分**包括節點、弧或連結及其標籤。

第二，**結構部分**顯示連結和節點如何形成有向圖。

第三，**程序部分**指定存取程序，即建立、修改節點和生成問題答案的程序。如果建構器是一個程序，那麼它將允許建立新的連結和節點。同樣地，如果解構器或修改器是一個程序，那麼它們將執行各自的操作——修改器將修改節點，而解構器將允許刪除連結和節點。

第四，**語意部分**建立了我們將含義與附加在連結上的標籤相關聯的方式。

繼承是語意網路的一個重要特性。其思想是：如果一個物件屬於一個類別，它就繼承了該類別的所有屬性，並且可以進行表示。一般來說，如果概念 X 具有屬性 P，那麼所有屬於 X 子集的概念也應該具有屬性 P。

在這個範例中，如果我們看到「知更鳥是一種鳥」，「鳥是動物」，「鳥有翅膀」，那麼「Red 是一隻知更鳥」，「Rusty 是一隻知更鳥」，則 Red 和 Rusty 都必須具有鳥的屬性——在這個範例中，鳥的屬性是有翅膀。所以 Rusty 和 Red 必須有翅膀，因為它們從父類別繼承了這個屬性。

關於非二元關係：我們已經看到了二元關係如何在語意網路中用弧來表示。但是，對於具有兩個以上引數的關係呢？例如，我們如何在語意網路中表示「John 把書給了 Mary」這個句子？

在謂詞邏輯中，我們可以使用一個三元謂詞，其第一個引數是給予者，第二個引數是被給予的物件，第三個引數是接收者。解決這個問題的方法是將「給予」的行為視為一個獨立的物件。我們可以在語意網路中將通用的「贈送事件」表示為涉及三個事物的關係：一個給予者、一個接收者和一個物件。

這也稱為概念圖。概念圖是表示自然語言句子含義的語意網路。另一個概念圖的範例可以在這個圖中看到：「John 搭公車去紐約。」

這是一個命題邏輯的範例：「如果一個農夫擁有一頭驢，那麼他會打它。」這可以轉換為語意網路，而這個圖又可以翻譯為以下的謂詞邏輯。

這等同於圖形匹配。對於每個問題會生成一個問題網路。當問題網路匹配到語意網路的一個子圖時，我們就得到了答案。如果給定一個圖並提出一個問題，那麼透過跟隨節點之間的連結，就可以推導出答案。這就是如何使用語意網路來生成答案的範例——只需跟隨連結和節點，然後得出答案。

WordNet 是語意網路的一個範例，它是英語的詞彙資料庫，將英語單詞分組為同義詞集合（稱為 synsets），提供簡短的一般性定義，並記錄這些同義詞集合之間的各種語意關係。

以下是語意網路的一些優點：它們簡單，容易實現和理解。語意網路比邏輯表示更自然。它允許使用有效的圖形演算法。它們在空間需求方面是高效的，因為物件只被表示一次，而關係則由指標處理。它們容易轉換為 Prolog，現在也容易轉換為 Python。

語意網路的一些應用包括：文件處理、問題處理、查詢擴展。我們可以在搜尋中使用語意網路，它還可以用於答案生成和答案選擇。

---

## 重點摘要 (Key Summary)

- **語意網路的定義：** 語意網路是一種使用有向圖來表示知識的方案，由代表概念的節點和代表概念間關係的有向弧組成。
- **歷史背景：** 語意網路的概念可追溯至 1966 年，由 Ross Quillian 提出，他試圖將人類語意記憶組織為層級式網路。
- **語意 vs 語法：**
  - 語法 (Syntax)：語言的文法規則，句子結構是否正確。
  - 語意 (Semantics)：句子的含義，是否有意義。
- **基本結構：**
  - **節點 (Nodes)：** 代表物件、屬性名稱或屬性值。
  - **弧 / 連結 (Arcs / Links)：** 定義節點之間的二元關係。
- **語意網路表示的四個組成部分：**
  1. **詞彙部分 (Lexical)：** 節點、弧及其標籤。
  2. **結構部分 (Structural)：** 連結和節點如何形成有向圖。
  3. **程序部分 (Procedural)：** 建立、修改、刪除節點和連結的存取程序。
  4. **語意部分 (Semantics)：** 將含義與連結標籤相關聯的方式。
- **繼承 (Inheritance)：** 如果物件屬於某個類別，則繼承該類別的所有屬性。例如：知更鳥是鳥，鳥有翅膀，因此知更鳥也有翅膀。
- **非二元關係的處理：** 將多引數關係中的動作視為獨立物件（例如「給予」事件包含給予者、接收者和物件三個角色），形成概念圖 (Conceptual Graph)。
- **圖形匹配與推論：** 對每個問題生成問題網路，當問題網路匹配到語意網路的子圖時，即可推導出答案。
- **WordNet：** 語意網路的實際應用範例，是英語的詞彙資料庫，將單詞分組為同義詞集合 (synsets) 並記錄語意關係。
- **語意網路的優點：**
  1. 簡單，容易實現和理解。
  2. 比邏輯表示更自然。
  3. 允許使用有效的圖形演算法。
  4. 空間效率高，物件只表示一次，關係由指標處理。
  5. 容易轉換為 Prolog 和 Python。
- **語意網路的應用：** 文件處理、問題處理、查詢擴展、搜尋、答案生成與答案選擇。
