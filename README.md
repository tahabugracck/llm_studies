# LLM Çalışmaları

## Genel Bakış
Bu depo, Büyük Dil Modelleri (LLM'ler) ve Doğal Dil İşleme (NLP) ile ilgili teorik açıklamaları ve pratik uygulamaları içermektedir. Özellikle self-attention, transformer mimarisi, tokenizasyon ve vektör temsilleri gibi temel kavramlar ele alınmakta ve Python ile bu kavramları açıklayan kod örnekleri sunulmaktadır.

## İçerik

### 📖 Teori
- **NLP'de Vektör Temsili**: Vektör veritabanları, gömleme (embedding) modelleri ve boyut indirgeme tekniklerine giriş.
- **Self-Attention Mekanizması**: Self-attention hesaplamalarının detaylı açıklaması ve örnekler.
- **Tokenizasyon Yöntemleri**: NLP'de kullanılan farklı tokenizasyon teknikleri ve önemi.
- **Transformer Mimarisi**: Transformer modelinin çalışma prensipleri; konumsal kodlama (positional encoding), çoklu başlı dikkat mekanizması (multi-head attention) ve ileri beslemeli katmanlar (feed-forward layers).

### 💻 Uygulamalar
- **self_attention_demo.py** → NumPy tabanlı self-attention uygulaması.
- **tokenization_example.py** → Düzenli ifadeler (regex) kullanarak basit bir tokenizasyon işlemi.
- **transformer_from_scratch.py** → PyTorch kullanarak sıfırdan inşa edilmiş bir transformer modeli.
- **word_embedding_visualization.py** → t-SNE kullanarak kelime gömlemelerinin görselleştirilmesi.

## 🔧 Kurulum
Kodları çalıştırabilmek için Python 3.x ve aşağıdaki bağımlılıkların kurulu olması gerekmektedir:
```bash
pip install numpy torch matplotlib scikit-learn gensim
```

## 🚀 Kullanım
Farklı NLP konseptlerini çalıştırmak için ilgili Python dosyalarını çalıştırabilirsiniz. Örneğin:
```bash
python self_attention_demo.py
```

## 📌 Notlar
Bu depo, teorik açıklamalar ve küçük ölçekli uygulamalara odaklanmaktadır. Kendi transformer modelimi geliştirmek için ayrı bir depo oluşturulacaktır.


---

Herhangi bir öneriniz veya katkınız varsa, lütfen bir issue açarak veya pull request göndererek paylaşabilirsiniz!

