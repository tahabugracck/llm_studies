import torch
import torch.nn as nn
import torch.optim as optim
import math

# Pozisyonel Kodlama
class PositionalEncoding(nn.Module):
    def __init__(self, embed_size, max_len=512):
        super(PositionalEncoding, self).__init__()
        position = torch.arange(max_len).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, embed_size, 2) * (-math.log(10000.0) / embed_size))
        pe = torch.zeros(1, max_len, embed_size)
        pe[0, :, 0::2] = torch.sin(position * div_term)
        pe[0, :, 1::2] = torch.cos(position * div_term)
        self.register_buffer('pe', pe)

    def forward(self, x):
        return x + self.pe[:, :x.size(1), :]

# Transformer Modeli
class SimpleTransformer(nn.Module):
    def __init__(self, vocab_size, embed_size, num_heads, num_layers, hidden_size, max_len=512, dropout=0.1):
        super(SimpleTransformer, self).__init__()

        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.positional_encoding = PositionalEncoding(embed_size, max_len)
        
        self.encoder_layer = nn.TransformerEncoderLayer(d_model=embed_size, nhead=num_heads, dim_feedforward=hidden_size, dropout=dropout, batch_first=True)
        self.encoder = nn.TransformerEncoder(self.encoder_layer, num_layers=num_layers)
        
        self.decoder_layer = nn.TransformerDecoderLayer(d_model=embed_size, nhead=num_heads, dim_feedforward=hidden_size, dropout=dropout, batch_first=True)
        self.decoder = nn.TransformerDecoder(self.decoder_layer, num_layers=num_layers)
        
        self.fc_out = nn.Linear(embed_size, vocab_size)
        
    def forward(self, src, tgt, src_mask=None, tgt_mask=None):
        src_embedded = self.positional_encoding(self.embedding(src))
        tgt_embedded = self.positional_encoding(self.embedding(tgt))
        
        encoder_output = self.encoder(src_embedded, src_key_padding_mask=src_mask)
        output = self.decoder(tgt_embedded, encoder_output, tgt_mask=tgt_mask)
        
        return self.fc_out(output)

# Model Parametreleri
vocab_size = 10000
embed_size = 512
num_heads = 8
num_layers = 6
hidden_size = 2048
dropout = 0.1

# Modeli oluşturma
model = SimpleTransformer(vocab_size, embed_size, num_heads, num_layers, hidden_size, dropout=dropout)

# Mask Oluşturma Fonksiyonu
def generate_square_subsequent_mask(sz):
    mask = torch.triu(torch.ones(sz, sz), diagonal=1)
    return mask.masked_fill(mask == 1, float('-inf'))

# Örnek veri
batch_size = 32
seq_len = 50

src = torch.randint(0, vocab_size, (batch_size, seq_len))  # (batch_size, seq_len)
tgt = torch.randint(0, vocab_size, (batch_size, seq_len))  # (batch_size, seq_len)

# Maskeyi oluştur
tgt_mask = generate_square_subsequent_mask(seq_len)  # (seq_len, seq_len)

# Modeli çalıştırma
output = model(src, tgt, tgt_mask=tgt_mask)

print("Çıktı şekli:", output.shape)  # (batch_size, seq_len, vocab_size)
print("Toplam Parametre Sayısı:", sum(p.numel() for p in model.parameters() if p.requires_grad))
