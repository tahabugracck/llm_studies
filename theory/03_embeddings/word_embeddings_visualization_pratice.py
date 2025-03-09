import gensim
from gensim.models import Word2Vec
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import numpy as np

# Örnek metin verisi 
metin = [
    "doğa çok güzeldir",
    "güneş doğar ve batır",
    "ağaçlar çok uzun ve güçlüdür",
    "hayvanlar ormanda yaşar",
    "orman doğal bir ortamdır"
]

# Kelimeleri token'lara ayırma
tokenized_corpus = [sentence.split() for sentence in metin]

# Word2Vec modelini eğitme
model = Word2Vec(sentences=tokenized_corpus, vector_size=100, window=5, min_count=1, workers=4)

# Kelime vektörlerini alma
kelimeler = list(model.wv.index_to_key)  # Modeldeki tüm kelimeleri al
kelime_vektorleri = np.array([model.wv[kelime] for kelime in kelimeler])  # NumPy dizisine çevirme

# t-SNE ile boyut indirgeme (2D'ye indiriyoruz)
perplexity_value = min(5, len(kelimeler) - 1)  # Perplexity değeri veri sayısından küçük olmalı
tsne = TSNE(n_components=2, random_state=0, perplexity=perplexity_value)
kelime_vektorleri_2d = tsne.fit_transform(kelime_vektorleri)

# Kelimeleri ve vektörlerini görselleştirme
plt.figure(figsize=(10, 8))

for i, kelime in enumerate(kelimeler):
    plt.scatter(kelime_vektorleri_2d[i, 0], kelime_vektorleri_2d[i, 1])
    plt.text(kelime_vektorleri_2d[i, 0] + 0.05, kelime_vektorleri_2d[i, 1] + 0.05, kelime, fontsize=12)

plt.title("Kelime Vektörlerinin Görselleştirilmesi")
plt.xlabel("t-SNE 1. bileşen")
plt.ylabel("t-SNE 2. bileşen")
plt.show()