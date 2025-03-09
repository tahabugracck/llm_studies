import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
import numpy as np

# Örnek kelimeler
words = ["apple", "banana", "cherry", "dog", "cat", "tiger", "car", "bike", "plane", "train"]

# Örnek embedding'ler (gerçekte Word2Vec veya başka bir modelden alınır)
embeddings = np.random.rand(10, 50)  # 10 kelime, her biri 50 boyutlu vektör

# t-SNE ile 2D'ye indirgeme
tsne = TSNE(n_components=2, perplexity=5, random_state=42)
reduced_embeddings = tsne.fit_transform(embeddings)

# Görselleştirme
plt.figure(figsize=(8, 6))
plt.scatter(reduced_embeddings[:, 0], reduced_embeddings[:, 1], c=np.arange(len(words)), cmap='coolwarm', s=100, edgecolors='black')

# Kelimeleri noktaların yanına ekleyelim
for i, word in enumerate(words):
    plt.annotate(word, (reduced_embeddings[i, 0] + 0.1, reduced_embeddings[i, 1] + 0.1), fontsize=12)

plt.title("Embedding'lerin 2D Görselleştirmesi")
plt.xlabel('t-SNE 1. Bileşen')
plt.ylabel('t-SNE 2. Bileşen')
plt.grid(True)
plt.show()
