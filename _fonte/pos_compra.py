# Páginas de depois da compra: o acesso de cada produto (a Hotmart não manda o link do app, então a página de obrigado
# de cada produto abre a sua pasta na hora) e a oferta do upsell com o widget de 1 clique do Funil de Vendas.
# O sufixo aleatório no nome é para ninguém adivinhar o endereço do acesso.
#   python _fonte/pos_compra.py
import os

AQUI = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.dirname(AQUI)
APP = 'https://nannasubito.github.io/app/'
DOMINIO = 'https://nannasubito.com/'
CK_CONSULENTE = 'https://pay.hotmart.com/F108290595O?checkoutMode=10'  # checkout do Diario della Nanna (ex Consulente del Sonno) na Hotmart (reserva do widget de 1 clique)

# pasta da página de acesso -> (pasta do app, nome, título, texto)
ACESSOS = {
    'accesso-7t53it': ('p3n8wa', 'Nanna Subito', 'Fatto. Nanna Subito è tua.', "Aprila da qui, dal telefono, e stasera parti dal rituale."),
    'accesso-e09m9e': ('h6s2qe', 'Nanna senza seno', 'Fatto. Nanna senza seno è tuo.', 'Si sblocca dentro Nanna Subito: aprilo dallo stesso telefono.'),
    'accesso-m16gzm': ('r9l4tm', 'Nel lettino', 'Fatto. Nel lettino è tuo.', 'Si sblocca dentro Nanna Subito: aprilo dallo stesso telefono.'),
    'accesso-dsdduo': ('z5o7ck', 'Orologio della Nanna', "Fatto. L'Orologio della Nanna è tuo.", 'Si sblocca dentro Nanna Subito: aprilo dallo stesso telefono.'),
    'accesso-n2icfq': ('k8c3vd', 'Diario della Nanna', 'Fatto. Il Diario della Nanna è tuo.', 'Si sblocca dentro Nanna Subito, insieme a tutta l\'app: aprilo dallo stesso telefono.'),
}
FRONT = 'accesso-7t53it'

ESTILO = (':root{--fundo:#eef6fc;--cartao:#fff;--tinta:#1b2f4a;--suave:#4a6079;--linha:#d5e6f3;--forte:#2a6fae;--azul:#d3eafa;--lua2:#fdf3dc}'
          '*{box-sizing:border-box;margin:0}body{background:var(--fundo);color:var(--tinta);font:17px/1.55 system-ui,-apple-system,"Segoe UI",Roboto,sans-serif}'
          'main{max-width:520px;margin:0 auto;padding:30px 20px 56px}h1{font-size:30px;line-height:1.15;letter-spacing:-.01em}p{margin-top:12px}'
          '.marca{display:flex;align-items:center;gap:9px;font-weight:800;color:#1f5689;margin-bottom:20px}.marca img{width:30px;height:30px;border-radius:8px}'
          '.apri{display:block;text-align:center;text-decoration:none;font-weight:800;font-size:18px;color:#fff;background:var(--forte);border-radius:16px;padding:17px 20px;margin-top:20px;box-shadow:0 12px 26px -12px rgba(42,111,174,.7)}'
          'ol{list-style:none;padding:0;margin-top:22px}li{background:var(--cartao);border:1px solid var(--linha);border-radius:18px;padding:16px 18px;margin-top:12px}'
          'li b{display:block;font-size:17.5px}li span{color:var(--suave);font-size:15.5px}'
          '.pacchetti{margin-top:18px;padding:14px 16px;border:1px dashed #9cc3e6;border-radius:18px;font-size:15.5px;color:var(--suave)}.pacchetti b{color:var(--tinta)}'
          '.nota{color:var(--suave);font-size:15px;margin-top:20px}')


def acesso(pasta, nome, titulo, texto, front):
    pac = ('<p class="pacchetti"><b>Hai aggiunto Nanna senza seno, Nel lettino o l\'Orologio della Nanna?</b> Ogni pacchetto arriva con la sua '
           'email di Hotmart e il suo PDF: apri quel link dallo stesso telefono e il pacchetto si sblocca dentro l\'app.</p>') if front else ''
    return f'''<!doctype html><html lang="it"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="robots" content="noindex, nofollow"><link rel="icon" type="image/png" sizes="32x32" href="../img/favicon-32.png">
<!-- obrigado da Hotmart: ela não manda o link do app, então o acesso abre daqui, na hora -->
<style>{ESTILO}</style>
<title>Il tuo accesso · Nanna Subito</title></head><body><main>
<div class="marca"><img src="../img/apple-touch-180.png" alt="">Nanna Subito</div>
<h1>{titulo}</h1><p>{texto}</p>
<a class="apri" href="{APP}{pasta}/">Apri {nome}</a>
<ol>
<li><b>1. Tocca il pulsante qui sopra.</b><span>L'app si apre nel browser, senza registrazione e senza scaricare niente.</span></li>
<li><b>2. Aggiungila alla schermata Home.</b><span>Su iPhone: Condividi, poi "Aggiungi alla schermata Home". Su Android: i tre puntini, poi "Aggiungi a schermata Home". Così la trovi stasera, al buio, con un tocco.</span></li>
<li><b>3. Il link resta anche nell'email di Hotmart.</b><span>Nella conferma d'acquisto trovi il PDF con lo stesso link, per riaprire l'app quando vuoi.</span></li>
</ol>
{pac}
<p class="nota">Qualcosa non va? Rispondi all'email di conferma di Hotmart o scrivi all'assistenza indicata lì.</p>
</main></body></html>
'''


UPSELL = f'''<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex">
<title>Diario della Nanna · Nanna Subito</title>
<link rel="icon" type="image/png" sizes="32x32" href="../img/favicon-32.png">
<style>
{ESTILO}
.ok{{background:var(--forte);color:#fff;text-align:center;padding:12px 16px;font-size:15.5px}}.ok b{{display:block;font-size:17px}}
.fone{{width:min(240px,64vw);margin:20px auto 4px}}.fone img{{width:100%;height:auto;display:block}}
.lista{{list-style:none;padding:0;margin-top:14px}}.lista li{{position:relative;padding:0 0 0 32px;margin-top:10px;background:none;border:0;border-radius:0}}
.lista li::before{{content:"";position:absolute;left:0;top:3px;width:22px;height:22px;border-radius:50%;background:var(--azul) url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%232a6fae' stroke-width='3' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M6 12.5l4 4L18 8'/%3E%3C/svg%3E") center/14px no-repeat}}
.offerta{{background:var(--cartao);border:2px solid var(--forte);border-radius:22px;padding:20px 18px;margin-top:22px}}
.prezzo{{font-size:15.5px;color:var(--suave);margin-top:12px}}.prezzo b{{display:block;font-size:30px;color:var(--tinta)}}
#hotmart-sales-funnel{{margin-top:16px;min-height:10px}}.reserva[hidden]{{display:none}}
.reserva a{{display:flex;align-items:center;justify-content:center;width:100%;text-decoration:none;border-radius:16px;text-align:center;padding:10px 16px}}
.reserva .si{{margin-top:16px;min-height:58px;background:var(--forte);color:#fff;font-weight:800;font-size:17px}}
.reserva .no{{margin-top:10px;min-height:50px;border:1.5px solid var(--linha);background:var(--cartao);color:var(--tinta);font-weight:600;font-size:16px}}
.nota{{text-align:center;font-size:14px}}
.apoio{{font-size:15.5px;font-weight:700;color:var(--forte)}}.micro{{font-size:14px;color:var(--suave);margin-top:6px}}
</style>
</head>
<body>
<div class="ok"><b>Fatto, il tuo acquisto è confermato.</b>Un attimo ancora e apri Nanna Subito.</div>
<main>
  <h1>Ancora una cosa, prima di stasera</h1>
  <p class="suave">Nei prossimi mesi arrivano i dentini, un salto di crescita, la regressione dei 4 mesi, un raffreddore, e non sai più se cambiare qualcosa o aspettare. Il Diario della Nanna serve a questo: ogni mattina segni com'è andata la notte con due tocchi, e ti dice cosa cambiare stasera. Dentro c'è anche l'SOS per regressioni (4 mesi, 8-10 mesi, 18 mesi), dentini, salti, viaggi, malattie e cambio dell'ora, fino ai 3 anni.</p>
  <p class="apoio">Ogni mattina, cosa cambiare stasera · SOS fino ai 3 anni</p>
  <div class="fone"><img src="../img/app-consulente.webp" alt="Il Diario della Nanna nell'app" width="560" height="1078"></div>
  <div class="offerta">
    <h2 style="font-size:22px">Diario della Nanna</h2>
    <p class="prezzo"><b>19,90 €</b>Una volta sola. Nessun abbonamento.</p>
    <p class="micro">Rimborso entro 15 giorni.</p>
    <div id="hotmart-sales-funnel"></div>
    <div class="reserva" id="reserva" hidden>
      <a class="si" href="{CK_CONSULENTE}">Sì, aggiungi il Diario della Nanna</a>
      <a class="no" href="{DOMINIO}{FRONT}/">No grazie, apro Nanna Subito</a>
    </div>
  </div>
</main>
<script src="https://checkout.hotmart.com/lib/hotmart-checkout-elements.js"></script>
<script>
/* Widget do Funil de Vendas da Hotmart (1 clique). Sem compra em andamento ele abre "pay.hotmart.com/funnel?undefined"
   com erro: quem chega sem a query da Hotmart vê os botões de reserva, e se o widget não carregar em 8 s também. */
(function () {{
  const reserva = document.getElementById('reserva'); let carregou = false;
  const mostraReserva = esconde => {{ reserva.hidden = false; if (esconde) document.getElementById('hotmart-sales-funnel').style.display = 'none'; }};
  if (!location.search) {{ mostraReserva(true); return; }}
  try {{
    checkoutElements.init('salesFunnel', {{ onLoad: () => {{ carregou = true; }}, onLoadDataError: () => mostraReserva(true) }}).mount('#hotmart-sales-funnel');
  }} catch (e) {{ mostraReserva(true); return; }}
  setTimeout(() => {{ if (!carregou) mostraReserva(false); }}, 8000);
}})();
</script>
</body>
</html>
'''

for pasta, (app, nome, titulo, texto) in ACESSOS.items():
    os.makedirs(os.path.join(SITE, pasta), exist_ok=True)
    open(os.path.join(SITE, pasta, 'index.html'), 'w', encoding='utf-8', newline='\n').write(acesso(app, nome, titulo, texto, pasta == FRONT))
os.makedirs(os.path.join(SITE, 'offerta-consulente'), exist_ok=True)
open(os.path.join(SITE, 'offerta-consulente', 'index.html'), 'w', encoding='utf-8', newline='\n').write(UPSELL)
print('ok:', len(ACESSOS), 'acessos + offerta-consulente | checkout do Diario della Nanna:', CK_CONSULENTE)
