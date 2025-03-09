# (Self-Attention hesaplaması)
import numpy as np

# Örnek olarak 3 kelimelik bir input dizisi
X = np.array([[1, 0, 1],   # Kelime 1
              [0, 1, 0],   # Kelime 2
              [1, 1, 0]])  # Kelime 3

# Sorgu (Q), anahtar (K) ve değer (V) matrislerini öğrenelim (bu örnekte rastgele belirliyoruz)
W_q = np.random.rand(3, 3)
W_k = np.random.rand(3, 3)
W_v = np.random.rand(3, 3)

Q = X.dot(W_q)
K = X.dot(W_k)
V = X.dot(W_v)

# Self-Attention Hesaplaması

# 1. Adım: Query ve Key arasında skaler çarpım (dot product)
scores = np.matmul(Q, K.T)

# 2. Adım: Softmax ile normalizasyon
attention_weights = np.exp(scores) / np.sum(np.exp(scores), axis=1, keepdims=True)

# 3. Adım: Değerler (V) ile ağırlıklı toplamı hesapla
output = np.matmul(attention_weights, V)

# Sonuçları yazdırma
print("Query Matrisleri:\n", Q)
print("Key Matrisleri:\n", K)
print("Value Matrisleri:\n", V)
print("Attention Weights:\n", attention_weights)
print("Output (Sonuç):\n", output)
