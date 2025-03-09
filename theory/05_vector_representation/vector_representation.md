### Vektör Uzayında Veri Temsili
Vektör veritabanı, metin, resim veya ses gibi yapılandırılmamış verileri yüksek boyutlu vektörlerde depolayan ve yöneten bir veritabanı türüdür. Bu sayede benzer nesnelerin hızlı bir şekilde bulunup alınması kolaylaşır.

Vektör yerleştirmelerini indekslemek ve sorgulamak için **vektör benzerliği arama algoritmaları** kullanılır. ChatGPT gibi Büyük Dil Modelleri (LLM) ile temel etkileşim aşağıdaki adımları içerir:

1. Kullanıcı, bir sorgu veya ifade girer.
2. Bu girdi, bir **embedding modeli** tarafından işlenerek vektör temsiline dönüştürülür.
3. Oluşan vektör, vektör veritabanındaki kayıtlarla **benzerlik metriği** (kosinüs benzerliği, Öklid mesafesi veya nokta çarpımı) kullanılarak karşılaştırılır.
4. Vektör veritabanı, semantik olarak en yakın sonuçları getirerek kullanıcıya sunar.

### Geleneksel Veritabanları Neden Yetersiz?
Geleneksel ilişkisel veritabanları (örn. MySQL, PostgreSQL) veri saklama ve yönetimi için kullanılsa da, vektör verileri için uygun değildir. Çünkü:
- Geleneksel veritabanları **tam eşleşme ve ilişkisel sorgular** için optimize edilmiştir.
- **Yüksek boyutlu vektör aramaları** kNN gibi algoritmalar gerektirir ve geleneksel indeksleme yöntemleri (B-ağaçları, hash tabanlı indeksleme vb.) bu tür aramalar için verimsizdir.
- Vektör veritabanları, **FAISS, Annoy, HNSW** gibi özel indeksleme algoritmalarını kullanarak büyük veri kümesi içinde hızlı aramalar yapabilir.

### Kelime Vektörleri Nasıl Görselleştirilir?
Vektörler, makinelerin **anlamsal ilişkileri** kavrayabilmesini sağlar. Bunu başlıca iki nedenle kullanırız:

1. **Anlamsal Zenginlik:**
   - Benzer kavramlar, vektör uzayında birbirine yakın olur. Bu sayede makineler **semantik benzerlikleri** algılayabilir.

2. **Basit Ama Gücülü:**
   - Vektörler, karmaşık veri türlerini (metin, görsel, ses vb.) basit **sayi dizilerine** dönüştürerek analiz edilmesini kolaylaştırır.

Bir kullanıcı arama yaptığında, sorgunun vektörü ile en yakın eşleşen **k-en yakın komşu (kNN) vektörleri** getirilir. Ancak, büyük veri kümesiyle çalışıldığında **yaklaşık kNN (ANN - Approximate Nearest Neighbor)** algoritmaları tercih edilir.

### PCA ve t-SNE Kullanımı
Boyut azaltma teknikleri, vektörlerin görselleştirilmesinde kullanılır:

- **PCA (Temel Bileşen Analizi):**
  - Veriler arasındaki **çizgisel korelasyonu** analiz eder.
  - En fazla varyansı koruyan **en az sayıda boyutu** bulur.

- **t-SNE (t-dağıtımlı Komşu Yerleştirme):**
  - Çizgisel olmayan bir tekniktir ve **veriyi anlamlı bir şekilde görselleştirmek için** kullanılır.
  - Özellikle **veri kümeleme (clustering)** için uygundur.

### Kaynakça
- https://research-aimultiple.com/vector-database-llm/
- https://medium.com/@EjiroOnose/vector-database-what-is-it-and-why-you-should-know-it-ae7e7dca82a4
- https://www.xomnia.com/post/an-introduction-to-vector-databases-for-beginners/
- https://thedataquarry.com/blog/vector-db-2/