# Monta a página de vendas (index.html) a partir de _fonte/pagina.html: põe o link do checkout e o pixel.
# Rodar de novo a cada mudança no modelo.
#   python _fonte/gerar.py
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(AQUI)

CHECKOUT = '#offerta'  # front na Hotmart em euro, com ?checkoutMode=10 (sem ele somem banner e bumps); ainda não criado
PIXEL_ID = ''  # dataset do Meta da oferta; ainda não criado
PAINEL = ''  # script de visitas do painel (instalacao.script do diagnostico-rastreio)

pixel = ''
if PIXEL_ID:
    pixel = ("<script>!function(f,b,e,v,n,t,s){if(f.fbq)return;n=f.fbq=function(){n.callMethod?n.callMethod.apply(n,arguments):n.queue.push(arguments)};"
             "if(!f._fbq)f._fbq=n;n.push=n;n.loaded=!0;n.version='2.0';n.queue=[];t=b.createElement(e);t.async=!0;t.src=v;s=b.getElementsByTagName(e)[0];"
             "s.parentNode.insertBefore(t,s)}(window,document,'script','https://connect.facebook.net/en_US/fbevents.js');"
             f"fbq('init','{PIXEL_ID}');fbq('track','PageView');</script>"
             f'<noscript><img height="1" width="1" style="display:none" src="https://www.facebook.com/tr?id={PIXEL_ID}&ev=PageView&noscript=1"/></noscript>')
if PAINEL:
    pixel = (pixel + '\n' + PAINEL).strip()

s = open(os.path.join(AQUI, 'pagina.html'), encoding='utf-8').read()
s = s.replace('__PIXEL__', pixel).replace('__CHECKOUT__', CHECKOUT)
open(os.path.join(SITE, 'index.html'), 'w', encoding='utf-8', newline='\n').write(s)
print('index.html', len(s.encode()) // 1024, 'KB')
