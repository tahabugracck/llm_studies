# Gerekli kütüphaneyi içe aktaralım
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

# nltk'nin veritabanını indiriyoruz
nltk.download('punkt')

# Örnek bir metin
metin = "Merhaba! Benim adım ChatGPT. NLP (Doğal Dil İşleme) hakkında size bilgi verebilirim."

# Cümle bazında tokenization
cumle_tokenlari = sent_tokenize(metin)
print("Cümle Bazında Tokenization:")
print(cumle_tokenlari)

# Kelime bazında tokenization
kelime_tokenlari = word_tokenize(metin)
print("\nKelime Bazında Tokenization:")
print(kelime_tokenlari)
