import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from gensim.models import Word2Vec

# Örnek kelime veri seti
documents = [
    ["hello", "world", "deep", "learning", "AI"],
    ["machine", "learning", "is", "fun"],
    ["natural", "language", "processing", "NLP"],
    ["transformer", "attention", "mechanism"],
    ["embedding", "vector", "dimensionality", "reduction"]
]

# Word2Vec modeli eğitme
model = Word2Vec(documents, vector_size=10, window=3, min_count=1, workers=4)
words = list(model.wv.index_to_key)
embeddings = np.array([model.wv[word] for word in words])

# T-SNE ile 2D indirgeme
tsne_2d = TSNE(n_components=2, perplexity=3, random_state=42)
embeddings_2d = tsne_2d.fit_transform(embeddings)

# 2D görselleştirme
plt.figure(figsize=(6, 6))
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1])
for i, word in enumerate(words):
    plt.annotate(word, (embeddings_2d[i, 0], embeddings_2d[i, 1]))
plt.title("Word Embeddings in 2D Space")
plt.show()

# T-SNE ile 3D indirgeme
tsne_3d = TSNE(n_components=3, perplexity=3, random_state=42)
embeddings_3d = tsne_3d.fit_transform(embeddings)

# 3D görselleştirme
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(embeddings_3d[:, 0], embeddings_3d[:, 1], embeddings_3d[:, 2])
for i, word in enumerate(words):
    ax.text(embeddings_3d[i, 0], embeddings_3d[i, 1], embeddings_3d[i, 2], word)
ax.set_title("Word Embeddings in 3D Space")
plt.show()