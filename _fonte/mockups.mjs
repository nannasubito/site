// Fotografa as telas do app (telas.html enquanto o app não existe) e põe cada uma num celular realista
// (aro de metal, borda preta, ilha dinâmica, barra de status, botões laterais, reflexo e sombra).
// Sai PNG em _fonte/png/; o mockups.py converte em WebP.
//   node _fonte/mockups.mjs
import { createRequire } from 'module';
import { mkdirSync, writeFileSync } from 'fs';
import { dirname, join } from 'path';
import { fileURLToPath } from 'url';

const require = createRequire('C:/dev/ofertas/.claude/skills/construcao/scripts/package.json');
const { chromium } = require('playwright');
const AQUI = dirname(fileURLToPath(import.meta.url));
const SAIDA = join(AQUI, 'png');
mkdirSync(SAIDA, { recursive: true });
// telas reais do app (pasta de teste com tudo liberado), com um estado salvo e o que clicar depois de abrir
const URL_APP = process.argv[2] || 'http://127.0.0.1:8792/t2x9aa/';
const ESTADO = { nome: 'Luca', mesi: 6, quando: new Date().toISOString().slice(0, 10), partenza: 'seno', stanza: ['buio', 'fresca', 'culla', 'pancia', 'telefono', 'silenzio'], notte: 3, suono: 'pancia' };
const TELAS = {
  home: [],
  rituale: ['[data-a="rituale"]', '[data-a="avanti"]'],
  suoni: ['[data-a="ir"][data-t="suoni"]', '[data-a="play"][data-s="pancia"]'],
  sos: ['[data-a="ir"][data-t="sos"]'],
  piano: ['[data-a="ir"][data-t="piano"]'],
  stanza: ['[data-a="ir"][data-t="stanza"]'],
  notte: ['[data-a="notte"]'],
};

const navegador = await chromium.launch({ headless: true, args: ['--mute-audio'] });
const ctx = await navegador.newContext({ viewport: { width: 390, height: 789 }, deviceScaleFactor: 2, locale: 'it-IT' });
await ctx.addInitScript(() => { HTMLMediaElement.prototype.play = function () { this.muted = true; return Promise.resolve(); }; });
const telas = {};
for (const [nome, cliques] of Object.entries(TELAS)) {
  const p = await ctx.newPage();
  await p.goto(URL_APP);
  await p.evaluate(e => localStorage.setItem('ns_stato', JSON.stringify(e)), ESTADO);
  await p.reload();
  await p.addStyleTag({ content: '.inst{display:none!important}*{animation:none!important}' });
  for (const c of cliques) { await p.click(c); await p.waitForTimeout(150); }
  await p.waitForTimeout(300);
  telas[nome] = (await p.screenshot({ type: 'png' })).toString('base64');
  await p.close();
}

const moldura = (img, escuro) => `<!doctype html><html><head><style>
*{box-sizing:border-box;margin:0}body{background:transparent;padding:40px 46px 70px}
.fone{position:relative;width:418px;height:872px;border-radius:66px;padding:12px;
 background:linear-gradient(145deg,#d9dde0 0%,#8e959b 18%,#eef1f3 36%,#7c838a 60%,#c9ced2 82%,#6f767c 100%);
 box-shadow:0 40px 70px -24px rgba(20,26,51,.5),0 18px 30px -18px rgba(0,0,0,.35),inset 0 0 0 1.5px rgba(255,255,255,.55)}
.bot{position:absolute;width:5px;border-radius:3px;background:linear-gradient(90deg,#6f767c,#c9ced2)}
.b1{left:-4px;top:160px;height:32px}.b2{left:-4px;top:220px;height:62px}.b3{left:-4px;top:296px;height:62px}.b4{right:-4px;top:250px;height:96px}
.tela{position:relative;width:100%;height:100%;border-radius:55px;background:#000;padding:6px;overflow:hidden}
.vidro{position:relative;width:100%;height:100%;border-radius:49px;overflow:hidden;background:${escuro ? '#121a30' : '#d3eafa'}}
.status{height:47px;display:flex;align-items:center;justify-content:space-between;padding:0 30px 0 38px;font:600 16px -apple-system,"Segoe UI",sans-serif;color:${escuro ? '#e8eefa' : '#1b2f4a'}}
.ilha{position:absolute;top:11px;left:50%;transform:translateX(-50%);width:122px;height:35px;border-radius:20px;background:#000}
.ic{display:flex;gap:6px;align-items:center}
.app{display:block;width:100%}
.brilho{position:absolute;inset:0;border-radius:49px;background:linear-gradient(115deg,rgba(255,255,255,.16) 0%,rgba(255,255,255,0) 32%);pointer-events:none}
</style></head><body><div class="fone"><i class="bot b1"></i><i class="bot b2"></i><i class="bot b3"></i><i class="bot b4"></i>
<div class="tela"><div class="vidro"><div class="status"><span>21:04</span><span class="ic">
<svg width="18" height="12" viewBox="0 0 18 12"><rect x="0" y="8" width="3" height="4" rx="1" fill="currentColor"/><rect x="5" y="5.5" width="3" height="6.5" rx="1" fill="currentColor"/><rect x="10" y="3" width="3" height="9" rx="1" fill="currentColor"/><rect x="15" y="0" width="3" height="12" rx="1" fill="currentColor"/></svg>
<svg width="16" height="12" viewBox="0 0 16 12"><path d="M8 11.5l2.4-3a3.4 3.4 0 0 0-4.8 0zM3.3 6.3a6.6 6.6 0 0 1 9.4 0l1.6-1.9a9.1 9.1 0 0 0-12.6 0zM.3 2.9a11 11 0 0 1 15.4 0" fill="currentColor"/></svg>
<svg width="27" height="13" viewBox="0 0 27 13"><rect x=".5" y=".5" width="23" height="12" rx="3.5" fill="none" stroke="currentColor" opacity=".5"/><rect x="2" y="2" width="14" height="9" rx="2" fill="currentColor"/><rect x="24.5" y="4.5" width="2" height="4" rx="1" fill="currentColor" opacity=".5"/></svg>
</span></div><div class="ilha"></div><img class="app" src="data:image/png;base64,${img}"><div class="brilho"></div></div></div></div></body></html>`;

const pm = await ctx.newPage();
await pm.setViewportSize({ width: 510, height: 982 });
for (const [nome, img] of Object.entries(telas)) {
  await pm.setContent(moldura(img, nome === 'notte'));
  await pm.waitForTimeout(150);
  writeFileSync(join(SAIDA, nome + '.png'), await pm.screenshot({ type: 'png', omitBackground: true }));
}
await navegador.close();
console.log('ok:', Object.keys(telas).join(', '), '->', SAIDA);
