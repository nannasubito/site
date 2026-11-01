# Converte os PNG do mockups.mjs em WebP no tamanho em que aparecem na página (~280 px, 2x para tela retina).
#   python _fonte/mockups.py
import os
from PIL import Image

AQUI = os.path.dirname(os.path.abspath(__file__))
ORIGEM = os.path.join(AQUI, 'png')
SAIDA = os.path.join(os.path.dirname(AQUI), 'img')
os.makedirs(SAIDA, exist_ok=True)
LARGURA = 560

for n in sorted(os.listdir(ORIGEM)):
    if not n.endswith('.png'):
        continue
    im = Image.open(os.path.join(ORIGEM, n)).convert('RGBA')
    alto = round(im.height * LARGURA / im.width)
    im = im.resize((LARGURA, alto), Image.LANCZOS)
    destino = os.path.join(SAIDA, 'app-' + n.replace('.png', '.webp'))
    im.save(destino, 'WEBP', quality=78, method=6)
    print(n, '->', os.path.basename(destino), os.path.getsize(destino) // 1024, 'KB', im.size)
