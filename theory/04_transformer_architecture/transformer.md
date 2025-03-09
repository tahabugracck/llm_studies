### Transformer Modelinin Genel Yapısı
Transformer, NLP alanında sıkça kullanılan bir transduction modelidir. Transduction, bir sekansı girdi olarak alıp, başka bir sekansı çıktı olarak veren modellere verilen isimdir.

Transformer modelleri, temel olarak iki ana bileşenden oluşur: **Encoder** ve **Decoder**. Her biri, birden fazla katmandan (layer) oluşan bu bileşenler, farklı ama birbiriyle ilişkili görevleri yerine getirirler.

- **Encoder:** Metni alır ve her bir kelime veya token için bir temsil (representation) oluşturur. Bu temsiller, metnin anlamını ve kelimeler arasındaki ilişkileri içerir. Encoder, metnin anlamını bir dizi vektör olarak kodlar.
- **Attention Mekanizması:** Hem encoder hem de decoder içinde bulunan, modelin metnin hangi bölümlerine “dikkat etmesi” gerektiğini belirleyen bir mekanizmadır. Bu sayede model, metnin belirli bölümleri arasındaki bağlantıları daha etkin bir şekilde kurabilir.
- **Decoder:** Encoder tarafından oluşturulan temsilleri kullanarak, hedef dili veya metni üretir. Decoder, bir çıktı üretmek için hem encoder'dan gelen bilgileri hem de kendi ürettiği önceki çıktıları kullanır.

Bu bileşenlerin her biri, **self-attention** ve **feed-forward neural networks** gibi yapıları içerir. Self-attention mekanizması, modelin bir cümle içindeki her kelimenin diğer kelimelerle olan ilişkisini değerlendirmesine olanak tanır. Bu, dilin doğasındaki karmaşık bağlamları ve anlamları daha iyi anlamasını sağlar.

---

### Self-Attention Mekanizması
Self-attention mekanizması, modelin girdi içindeki her kelimenin diğer kelimelerle olan ilişkisini anlamasını sağlayan bir yapıdır. Bu mekanizma şu bileşenleri içerir:

- **Query (Sorgu), Key (Anahtar) ve Value (Değer):** Model, her kelime için bu üç değişkeni hesaplar. Bu bileşenler, bir kelimenin diğer kelimelerle olan ilişkisini belirlemek için kullanılır.
- **Scaled Dot-Product Attention:** Query ve Key vektörleri arasındaki benzerlik hesaplanarak bir skorlama yapılır. Daha sonra softmax fonksiyonu uygulanarak dikkat dağılımı belirlenir.
- **Multi-Head Attention:** Self-attention mekanizmasının bir genişlemesidir. Modelin farklı “başlıklar” (“heads”) üzerinden veriyi paralel olarak işlemesine olanak tanır. Her baş, verinin farklı temsillerine odaklanır, böylece model aynı anda birden fazla bağlamı ve ilişkiyi değerlendirebilir.

---

### Positional Encoding
Transformer modelleri kelime sırasını doğrudan algılayamaz. Bu nedenle **Positional Encoding (Konumsal Kodlama)** kullanılır. Pozisyon bilgileri, sinüs ve kosinüs fonksiyonları kullanılarak kelimelerin vektör temsillerine eklenir.

---

### Encoder-Decoder Yapısı

#### Encoder Bloğu
Encoder, girdi cümlesini alır ve anlamlı bir çıktı vektörüne dönüştürür. Her encoder katmanı şu bileşenlerden oluşur:

- **Word Embedding:** Kelimeleri vektörel forma dönüştürür.
- **Positional Encoding:** Kelimelerin konum bilgisini modele ekler.
- **Multi-Head Self-Attention:** Girdi kelimelerinin birbirleriyle ilişkisini anlamasını sağlar.
- **Feed-Forward Network:** Kelimelerin daha soyut temsillerini oluşturur.
- **Layer Normalization & Residual Connections:** Modelin daha stabil çalışmasını sağlar.

#### Decoder Bloğu
Decoder, encoder'dan gelen bilgiyi kullanarak hedef dizi (output sequence) oluşturur. Encoder ile benzer katmanlara sahiptir ancak ekstra olarak **Masked Self-Attention** mekanizması içerir. Bu mekanizma, decoder'in sadece daha önceden üretilmiş token'lara bakmasını sağlar.

---

### Transformer Modellerinin Kullanım Alanları
Transformer modelleri NLP alanında devrim yaratmıştır ve aşağıdaki alanlarda yaygın olarak kullanılmaktadır:

- Makine çevirisi (Google Translate, DeepL)
- Metin üretme (ChatGPT, Bard, Claude)
- Konuşma tanıma
- Metinden özet çıkarma
- Soru-cevap sistemleri

---

### Kaynakça
- https://machinelearningmastery.com/the-transformer-model/
- https://huggingface.co/learn/nlp-course/chapter1/1?fw=pt
- https://www.geeksforgeeks.org/positional-encoding-in-transformers/
- https://www.linkedin.com/pulse/self-attention-mekanizmas%C4%B1-yusuf-deni%CC%87z/


