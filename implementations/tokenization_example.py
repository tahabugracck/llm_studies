import re

# Gelişmiş tokenization fonksiyonu
def tokenize(text):
    # Küçük harfe çevir, kelimeleri ve noktalama işaretlerini ayır
    tokens = re.findall(r"\w+(?:'\w+)?|[.,!?]", text.lower())
    return tokens

# Örnek metin
text = "Merhaba! Benim adım Buğra. Hazırladığım repoyu beğendin mi?"

# Tokenize etme
tokens = tokenize(text)

# Sonuçları yazdırma
print("Tokenler: ", ", ".join(tokens))
