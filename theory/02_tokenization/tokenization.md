### Tokenization Nedir?
Tokenizasyon, metin işleme sürecinde ilk ve en önemli adımlardan biridir. Dil modellerinin metni anlayabilmesi ve işleyebilmesi için metnin sayısal bir temsile dönüştürülmesi gerekir. Tokenizasyon işlemi, metni belirli parçalara (tokenlara) ayırarak her birine sayısal bir değer atar.

Doğal Dil İşleme (NLP) süreçlerinde kullanılan birkaç temel tokenizasyon yöntemi şunlardır:
- **Kelime Düzeyi Tokenizasyon (Word-Level Tokenization)**
- **Alt Kelime Düzeyi Tokenizasyon (Subword Tokenization)**
- **Karakter Düzeyi Tokenizasyon (Character-Level Tokenization)**
- **Byte-Pair Encoding (BPE)**
- **WordPiece ve SentencePiece Tokenizasyonu**

---

## Tokenizasyon Süreci

Gerçek zamanlı tokenizasyon işlemi üç temel adımdan oluşur:
1. **Metnin tokenlara ayrılması**: Metin, modelin eğitiminde kullanılan kelime dağarcığında bulunan tokenlara bölünür.
2. **Tokenlerin kimliklerle eşleştirilmesi**: Her token, önceden belirlenen kelime dağarcığında tanımlanan bir kimlikle eşleştirilir.
3. **Özel belirteçlerin eklenmesi**: Modelin işleyebilmesi için gerekli olan özel tokenlar (örneğin, başlangıç [CLS], bitiş [SEP] gibi) eklenir.

Tokenizasyon işlemi, modelin performansını doğrudan etkileyen kritik bir süreçtir.

---

## Word-Level, Subword ve Character-Level Tokenization

### **1. Kelime Düzeyi Tokenizasyon (Word-Level Tokenization)**
Kelime düzeyinde tokenizasyon, metni tek tek kelimelere ayırarak her kelimeyi tek bir token olarak işler.

**Avantajları:**
- Basit ve sezgiseldir.
- Yaygın kelimelerle iyi çalışır.
- Uygulaması hızlıdır.

**Dezavantajları:**
- Nadir kelimeleri işleyemez (Örneğin, "Tokenizasyon" kelimesi modelin kelime dağarcığında yoksa işlenemez).
- Morfolojik olarak zengin diller için uygun değildir.
- Büyük kelime dağarcıkları gerektirir, bu da belleği verimsiz kullanabilir.

**Örnek:**
```
Metin: "Tokenization helps models understand language."
Tokenlar: ["Tokenization", "helps", "models", "understand", "language"]
```

---

### **2. Alt Kelime Düzeyi Tokenizasyon (Subword Tokenization)**
Alt kelime tokenizasyonu, kelime düzeyi ve karakter düzeyi tokenizasyonun arasında bir denge kurar. Kelimeleri tam olarak veya daha küçük anlamlı birimlere bölerek işler.

**Ne Zaman Kullanılır?**
- Nadir veya bileşik kelimeleri ele almak için.
- Kelimelerin farklı formlarını (çoğul, çekim vb.) modellemek için.
- Büyük kelime dağarcıklarını yönetmek için.

**Örnek:**
```
Metin: "Tokenization helps models understand language."
Alt kelime tokenları: ["Token", "ization", "helps", "model", "s", "understand", "language"]
```

---

### **3. Karakter Düzeyi Tokenizasyon (Character-Level Tokenization)**
Karakter düzeyi tokenizasyon, metni tek tek karakterlere böler.

**Avantajları:**
- Yeni kelimeleri doğal olarak öğrenebilir.
- Kelime dağarcığı küçüktür.

**Dezavantajları:**
- Daha uzun diziler üretir ve işlem süresini uzatır.
- Dilbilgisel yapıyı anlamakta zorlanabilir.

**Örnek:**
```
Metin: "Token"
Tokenlar: ["T", "o", "k", "e", "n"]
```

---

## Byte-Pair Encoding (BPE)
BPE, kelimeleri sık kullanılan alt birimlere bölerek hem kelime hem de karakter düzeyi tokenizasyonun avantajlarını birleştirir.

**BPE’nin Avantajları:**
- Yeni kelimeleri anlamlandırabilir.
- Morfolojik farklılıkları yakalayabilir.
- Dilden bağımsızdır.
- Hafıza açısından verimlidir.

**Örnek:**
```
Örnek Korpus: ["bayat", "bayrak", "kayak", "kıyak"]
İlk Tokenizasyon: ["b", "a", "y", "a", "t"], ["b", "a", "y", "r", "a", "k"], ...
BPE İşlemi: ["bay", "a", "t"], ["bay", "r", "a", "k"], ...
```

---

## WordPiece ve SentencePiece Tokenizasyonu

### **WordPiece Tokenizasyonu**
WordPiece, BPE’ye benzer ancak frekans yerine olasılıksal bir yaklaşım kullanır. Çoğunlukla BERT gibi modellerde kullanılır.

**Özellikleri:**
- En sık görülen token çiftlerini birleştirir.
- Büyük veri kümelerinde daha verimli çalışır.
- Modelin yeni kelimeleri daha iyi öğrenmesine olanak tanır.

**Örnek:**
```
Metin: "unhappiness"
Tokenlar: ["un", "##happiness"]
```
(Burada ## işareti, tokenin önceki bir token ile birleştiğini gösterir.)

### **SentencePiece Tokenizasyonu**
SentencePiece, veri ön işlemesine ihtiyaç duymadan doğrudan ham metin üzerinde çalışabilen bir tokenizasyon yöntemidir. Özellikle GPT ve T5 gibi modellerde kullanılır.

**Özellikleri:**
- Noktalama işaretleri ve boşlukları da token olarak görebilir.
- Dil bağımsızdır ve her tür metin için kullanılabilir.
- Model eğitimini kolaylaştırır.

**Örnek:**
```
Metin: "Hello world!"
Tokenlar: ["▁Hello", "▁world", "!"]
```
(Burada "▁" işareti, tokenin kelimenin başında olduğunu gösterir.)

---

## Sonuç
Tokenizasyon, büyük dil modellerinin metni anlaması ve işlemesi için kritik bir adımdır. Farklı tokenizasyon yöntemleri, modelin doğruluğunu ve verimliliğini artırmada önemli bir rol oynar. Kullanılacak yöntemin seçimi, modelin amacı ve kullanım senaryosuna bağlıdır.

---

### **Kaynakça:**
- https://docs.mistral.ai/guides/tokenization/
- https://christophergs.com/blog/understanding-llm-tokenization
- https://airbyte.com/data-engineering-resources/llm-tokenization
- https://medium.com/@sahin.samia/decoding-tokenization-strategies-for-large-language-models-llms-ffc3fa51aff6
- https://oguzhanyenen.medium.com/bpe-byte-pear-encoding-tokenizasyon-algoritmas%C4%B1-54932e88b2f6
- https://www.geeksforgeeks.org/byte-pair-encoding-bpe-in-nlp/
- https://medium.com/@atharv6f_47401/wordpiece-tokenization-a-bpe-variant-73cc48865cbf