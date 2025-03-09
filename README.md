# LLM Çalışmaları

## Genel Bakış  
Bu depo, Büyük Dil Modelleri (LLM'ler) ve Doğal Dil İşleme (NLP) ile ilgili teorik açıklamaları ve pratik uygulamaları içermektedir. Kendiliğinden dikkat (self-attention), transformer'lar, tokenizasyon ve vektör temsilleri gibi temel kavramları ele alır ve bu prensipleri göstermek için Python uygulamaları sağlar.

## İçerik

### 📖 Teori
- **NLP'de Vektör Temsili**: Vektör veritabanlarına, embedding modellerine ve boyut indirgeme tekniklerine giriş.
- **Kendiliğinden Dikkat Mekanizması (Self-Attention)**: Kendiliğinden dikkat hesaplamalarının örneklerle açıklanması.
- **Tokenizasyon Yöntemleri**: Farklı tokenizasyon tekniklerinin ve bunların NLP'deki öneminin genel bakışı.
- **Transformer Mimarisi**: Transformer'ların nasıl çalıştığının açıklanması, pozisyonel kodlama, çok başlıklı dikkat (multi-head attention) ve ileri besleme katmanları dahil.

### 💻 Uygulamalar
- **self_attention_demo.py** → Kendiliğinden dikkat için NumPy tabanlı bir uygulama.
- **tokenization_example.py** → Düzenli ifadelerle yapılmış basit bir tokenizer.
- **transformer_from_scratch.py** → PyTorch tabanlı sıfırdan yapılmış bir transformer modeli.
- **word_embedding_visualization.py** → t-SNE kullanarak kelime embedding'lerinin görselleştirilmesi.

## 🔧 Kurulum  
Uygulamaları çalıştırmak için Python 3.x ve aşağıdaki bağımlılıklara ihtiyacınız olacak:
```bash
pip install numpy torch matplotlib scikit-learn gensim
```

## 🚀 Kullanım  
Python script'lerini çalıştırarak farklı NLP kavramlarını uygulamada görebilirsiniz. Örneğin:
```bash
python self_attention_demo.py
```

## 📌 Notlar  
Bu depo, teorik keşif ve küçük ölçekli uygulamalara odaklanmaktadır. Tam ölçekli bir özel transformer modeli geliştirmek için ayrı bir depo oluşturulacaktır.

---

Herhangi bir öneri veya katkı için, bir issue açabilir veya pull request gönderebilirsiniz!#   l l m _ s t u d i e s  
 