### Embedding Nedir?
Embedding, kelimelerin veya diğer verilerin yüksek boyutlu uzayda, daha kompakt ve anlamlı gerçek değerli vektörler olarak temsil edilmesidir. Doğal Dil İşleme (NLP) ve makine öğrenimi alanlarında, verilerin sayısal olarak ifade edilmesini sağlamak için embedding yöntemleri yaygın olarak kullanılır.

En temel yöntemlerden biri **One-Hot Encoding**'dir. Bu yöntemde, kelimeler toplam kelime sayısı kadar boyuta sahip vektörler şeklinde temsil edilir. Bir kelimenin bulunduğu konuma `1`, diğer tüm konumlara `0` değeri atanır. Ancak, bu yöntem büyük kelime dağarcıklarında oldukça verimsiz hale gelir ve anlamsal ilişkileri yakalayamaz. 

Bunu aşmak için daha gelişmiş embedding teknikleri geliştirilmiştir.

---

### Word2Vec, GloVe, FastText
#### **Word2Vec**
Word2Vec, bir kelimenin bağlamını analiz ederek kelime vektörlerini oluşturan bir yöntemdir. Kelimelerin birbirleriyle hangi sıklıkta geçtiğini analiz ederek, anlam bakımından benzer olan kelimeleri matematiksel olarak yakın konumlara yerleştirir.

Word2Vec iki temel yaklaşımla çalışır:
- **CBOW (Continuous Bag of Words)**: Çevredeki kelimelerden hareketle eksik kelimeyi tahmin etmeye çalışır.
- **Skip-gram**: Bir kelime verildiğinde, çevresindeki kelimeleri tahmin etmeye çalışır.

Örneğin, “kuş ağaçta oturdu” cümlesinde, Word2Vec "kuş" ve "ağaç" kelimelerinin sıklıkla benzer bağlamlarda geçtiğini öğrenebilir.

#### **GloVe (Global Vectors for Word Representation)**
GloVe, kelimeler arasındaki ilişkileri matris faktörizasyonu ile modelleyen bir yöntemdir. Büyük metin koleksiyonlarında kelimelerin birlikte bulunma olasılıklarını analiz ederek, daha geniş ilişkileri keşfetmek için kullanılır.

Örneğin, GloVe modeli, “peynir” ve “mayo”nun sıklıkla “sandviç” ile birlikte geçtiğini tespit edebilir. Bu, semantik arama ve kelime gruplama işlemlerinde avantaj sağlar.

#### **FastText**
FastText, Facebook tarafından geliştirilen ve Word2Vec'in bir uzantısı olan bir tekniktir. Kelimeleri karakter n-gramları (alt kelime parçaları) şeklinde temsil eder. Böylece, nadir kelimeleri veya yazım hatalarını daha iyi anlayabilir.

Örneğin, “koşu” ve “koşucu” kelimelerinin ortak alt kelime yapıları taşıdığını tespit ederek, kelimeler arasındaki benzerlikleri daha hassas şekilde yakalayabilir.

---

### Transformer Tabanlı Embeddings (BERT, GPT)
Günümüzde, transformer tabanlı modeller kelime anlamlarını bağlama dayalı olarak daha etkili şekilde öğrenmektedir. Bu modeller, büyük veri kümelerinde önceden eğitilmiş embedding katmanlarını içerir ve doğrudan kullanılabilir. 

#### **BERT (Bidirectional Encoder Representations from Transformers)**
BERT, kelimelerin bağlamlarını her iki yönden de (öncesi ve sonrası) dikkate alarak anlamlarını çıkaran çift yönlü bir modeldir. Örneğin:

- “Para yatırmak için bankaya gitti.” cümlesinde, BERT hem "para yatırmak" hem de "banka" kelimelerini değerlendirerek, "banka" kelimesinin finansal bir kuruluşu ifade ettiğini anlar.

#### **GPT (Generative Pre-trained Transformer)**
GPT, otoregresif bir modeldir, yani bir kelimeyi tahmin ederken yalnızca sol taraftaki bağlamı kullanır. Örneğin:

- “Bugün hava çok ...” cümlesinde, GPT “güzel” veya “bulutlu” gibi uygun kelimeleri tahmin edebilir.

BERT ve GPT arasındaki en büyük farklardan biri, bağlamı işleme biçimleridir:
- **BERT** çift yönlüdür ve bağlamın hem öncesini hem de sonrasını dikkate alır. Bu yüzden, duygu analizi veya metin anlama gibi görevlerde daha başarılıdır.
- **GPT** tek yönlü çalışır ve metin üretimi konusunda daha etkilidir.

Ayrıca, **GPT-4 yaklaşık 45TB veri üzerinde eğitilmişken, BERT 3TB veri üzerinde eğitilmiştir.** Bu nedenle, GPT-4, daha büyük veri kümesi nedeniyle özellikle özetleme ve çeviri gibi görevlerde avantajlıdır.

---

### Vektörel Uzayda Anlam Benzerliği
Kelimeleri temsil eden vektörler, yüksek boyutlu bir uzayda birbirlerine olan yakınlıklarına göre konumlandırılır. Bu sayede kelimeler arasındaki anlam benzerlikleri matematiksel olarak ölçülebilir.

**Kosinüs benzerliği**, iki kelime vektörünün arasındaki açıyı ölçerek benzerliği hesaplamak için yaygın olarak kullanılır. İki vektör arasındaki açı ne kadar küçükse, kelimeler o kadar benzerdir.

Örneğin:
- "Kral" ve "Kraliçe" kelimeleri, anlamca yakın oldukları için vektör uzayında da birbirlerine yakın konumda yer alır.
- "Elma" ve "Masa" gibi anlamsal ilişkisi düşük olan kelimeler ise birbirlerinden uzak olur.

Bu yöntemler, arama motorlarından otomatik metin tamamlama sistemlerine kadar birçok alanda kullanılmaktadır.

---

### Kaynakça
- https://medium.com/machine-learning-t%C3%BCrkiye/nlp-ve-embedding-kullan%C4%B1m%C4%B1-tensorflow-hub-nas%C4%B1l-kullan%C4%B1l%C4%B1r-70cab0d0562d
- https://medium.com/bili%C5%9Fim-hareketi/word-embedding-teknikleri-word2vec-nedir-tf-idf-nedir-e2f826dd9178
- https://www.iguazio.com/glossary/llm-embeddings/
- https://blog-invgate-com.translate.goog/gpt-3-vs-bert
- https://blog-marketmuse-com.translate.goog/glossary/vector-space-model-definition

