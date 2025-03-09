import torch
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, embed_size, heads):
        super(MultiHeadAttention, self).__init__()
        self.embed_size = embed_size  # Embedding boyutu
        self.heads = heads  # Başlık sayısı
        self.head_dim = embed_size // heads  # Her başlık için boyut
        
        # Başlık sayısının, embedding boyutuyla uyumlu olduğundan emin ol
        assert (
            self.head_dim * heads == embed_size
        ), "Embedding boyutu başlık sayısı ile bölünebilir olmalı"
        
        # Değerler, anahtarlar ve sorgular için doğrusal katmanlar
        self.values = nn.Linear(self.head_dim, self.head_dim, bias=False)  # Değerler için doğrusal katman
        self.keys = nn.Linear(self.head_dim, self.head_dim, bias=False)  # Anahtarlar için doğrusal katman
        self.queries = nn.Linear(self.head_dim, self.head_dim, bias=False)  # Sorgular için doğrusal katman
        self.fc_out = nn.Linear(heads * self.head_dim, embed_size)  # Çıktı için doğrusal katman
    
    def forward(self, values, keys, query, mask):
        N = query.shape[0]  # Batch boyutu
        value_len, key_len, query_len = values.shape[1], keys.shape[1], query.shape[1]  # Değer, anahtar ve sorgu uzunlukları
        
        # Verileri başlıklar halinde yeniden şekillendir
        values = values.reshape(N, value_len, self.heads, self.head_dim)
        keys = keys.reshape(N, key_len, self.heads, self.head_dim)
        queries = query.reshape(N, query_len, self.heads, self.head_dim)
        
        # Değer, anahtar ve sorguları doğrusal katmanlardan geçirme
        values = self.values(values)
        keys = self.keys(keys)
        queries = self.queries(queries)
        
        # Enerji hesaplaması: queries ve keys arasında iç çarpım
        energy = torch.einsum("nqhd,nkhd->nhqk", [queries, keys])
        
        # Mask varsa, enerjiyi maskele
        if mask is not None:
            energy = energy.masked_fill(mask == 0, float("-1e20"))
        
        # Dikkat katsayılarını hesapla (Softmax ile)
        attention = torch.softmax(energy / (self.embed_size ** (1 / 2)), dim=3)
        
        # Değerlerle dikkat katsayılarını çarp ve çıktıyı yeniden şekillendir
        out = torch.einsum("nhql,nlhd->nqhd", [attention, values]).reshape(
            N, query_len, self.heads * self.head_dim
        )
        
        # Çıktıyı son doğrusal katmandan geçir
        out = self.fc_out(out)
        return out

# Örnek kullanım
embed_size = 512  # Embedding boyutu
heads = 8  # Başlık sayısı
values = torch.rand((64, 10, embed_size))  # 64 örnek, 10 uzunluk, embedding boyutu kadar değerler
keys = torch.rand((64, 10, embed_size))  # Anahtarlar için benzer şekilde
query = torch.rand((64, 10, embed_size))  # Sorgular için benzer şekilde
mask = None  # Maske yok

multihead_attention = MultiHeadAttention(embed_size, heads)  # Modeli oluştur
output = multihead_attention(values, keys, query, mask)  # Çıktıyı al
print(output.shape)  # Beklenen çıktı şekli: (64, 10, 512)
