# Catalogo componenti

Classi di `assets/oe-components.css` (prefisso `.oe-`), più la chrome del sito
(`.nav` in `nav.css`, `.footer` in `footer.css`). Ogni blocco qui sotto è
markup minimo da copiare; la resa di tutti i componenti insieme è in
`esempi/anteprima.html`. Non inventare classi nuove se ne esiste una adatta;
se serve un componente che manca, costruiscilo con i soli token `--oe-*` e le
stesse regole (spigolo vivo, fuga 2px, Hedvig solo per titoli/numeri).

## Indice

| componente | classe | quando |
|---|---|---|
| Sezione | `.oe-section` (+ `--grey` `--tint` `--dark` `--accent` `--rule`) | ogni blocco di pagina |
| Intestazione di sezione | `.oe-section-head` | apre ogni sezione |
| Chip | `.oe-chip` (`--sm`) | categoria sopra un titolo |
| Sottotitolo | `.oe-subhead` | titolo di un sotto-blocco |
| Hero | `.oe-hero` (`--text`) | apertura della pagina, una sola |
| Bottoni | `.oe-btn` (`--ghost` `--pop` `--on-dark`) | azioni |
| Griglia a tessere | `.oe-tiles--2/3/4/6` | card, KPI affiancati |
| Due colonne | `.oe-split` (`--even`) | testo + figura |
| Card | `.oe-card` (`--media`, `--hover`) | un fatto con etichetta, valore, titolo |
| KPI | `.oe-kpi` (`--dark`) | un grande numero |
| Statistiche | `.oe-stats > .oe-stat` | 3–5 numeri piccoli in riga |
| Parametri | `.oe-params > .oe-param` | ipotesi, impostazioni, metadati |
| Elenco per peso | `.oe-rank` | voci ordinate con quota e valore |
| Riquadro lime | `.oe-callout` | la frase che chiude un ragionamento |
| Verdetto | `.oe-verdict` (`--negative`) | esito sintetico |
| Passi | `.oe-steps > .oe-step` | processo, metodologia |
| Testo lungo | `.oe-prose` | paragrafi, elenchi |
| Figura | `.oe-figure` | grafico con numero, titolo, testo, fonte |
| Tabella | `.oe-table-wrap > .oe-table` | dati tabellari |

## Struttura della pagina

```html
<body>
  <a class="oe-skip" href="#main">Vai al contenuto</a>
  <header><nav class="nav">…</nav></header>
  <main id="main">
    <section class="oe-hero" id="top">…</section>
    <section class="oe-section oe-section--grey" id="…" aria-labelledby="t-…">
      <div class="oe-section__inner">…</div>
    </section>
  </main>
  <footer class="footer">…</footer>
</body>
```

`.oe-section__inner` limita la larghezza a 1440px e mette 48px tra i figli
diretti: non servono spaziatori (`<div class="sp48">`) né margini inline.

## Nav

```html
<nav class="nav" aria-label="Principale">
  <a href="#top" class="nav__logo-link" aria-label="OpenEconomics — inizio pagina">
    <img src="assets/logo/logo-black.svg" alt="OpenEconomics" class="nav__logo-img" width="142" height="18">
    <span class="nav__badge">Studies</span>            <!-- facoltativo -->
  </a>
  <ul class="nav__links">
    <li><a href="#sintesi">Sintesi</a></li>             <!-- sempre href="#id", mai onclick -->
  </ul>
  <a class="nav__cta" href="…"><span>Scarica</span></a> <!-- facoltativo, una sola CTA -->
  <!-- in alternativa: .nav__login (bordato) o .nav__download (solo icona, con aria-label) -->
  <button class="nav__toggle" type="button" aria-expanded="false" aria-label="Apri il menu">
    <svg class="nav__icon-open" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 6h16M4 12h16M4 18h16"/></svg>
    <svg class="nav__icon-close" viewBox="0 0 24 24" aria-hidden="true"><path d="M18 6 6 18M6 6l12 12"/></svg>
  </button>
</nav>
```

`oe-page.js` gestisce il menu mobile (sotto 960px) e segna la voce attiva
(`.nav-active` + `aria-current`) mentre si scorre. Tieni le voci entro 5–6.

## Hero

```html
<section class="oe-hero" id="top">
  <div class="oe-hero__body">
    <div class="oe-hero__top">
      <span class="oe-chip oe-chip--sm">Categoria</span>
      <p class="oe-hero__kicker">Contesto · ente · anno</p>
    </div>
    <div>
      <h1 class="oe-hero__title">Titolo su due righe<br><em>parte in lime</em></h1>
      <p class="oe-hero__lead">Lead di 2–3 righe.</p>
      <dl class="oe-hero__meta">
        <div class="oe-hero__meta-item"><dt class="oe-hero__meta-label">Livello</dt><dd class="oe-hero__meta-value">Regionale</dd></div>
      </dl>
      <div class="oe-hero__actions"><a class="oe-btn oe-btn--pop" href="#…">Azione</a></div>
    </div>
  </div>
  <div class="oe-hero__media" style="--hero-img:url('media/hero.webp')" role="img" aria-label="Descrizione della foto">
    <p class="oe-hero__caption"><span>Didascalia</span><strong>Crediti</strong></p>
  </div>
</section>
```

Senza foto: togliere `style` (resta il gradiente) oppure usare
`.oe-hero oe-hero--text` ed eliminare `.oe-hero__media`.

## Intestazione di sezione

```html
<header class="oe-section-head">
  <span class="oe-chip">Sezione 01</span>
  <h2 class="oe-section-head__title" id="t-sintesi">Sintesi</h2>
  <p class="oe-section-head__lead">Sottotitolo in una frase.</p>
</header>
```

Su `.oe-section--dark` titolo bianco e lead lime in automatico.
Sotto-blocchi: `<h3 class="oe-subhead">…</h3>`.

## Bottoni

```html
<a class="oe-btn" href="…">Primario</a>                   <!-- Bluette pieno, su chiaro -->
<a class="oe-btn oe-btn--ghost" href="…">Secondario</a>   <!-- bordato, su chiaro -->
<a class="oe-btn oe-btn--pop" href="…">Primario</a>       <!-- lime, su scuro -->
<a class="oe-btn oe-btn--on-dark" href="…">Secondario</a> <!-- bordo bianco, su scuro -->
```

`<a>` per andare da qualche parte, `<button type="button">` per fare qualcosa.
Un solo bottone primario per vista. Icona dopo il testo: `<i data-lucide="arrow-right"></i>`.

## Card

```html
<div class="oe-tiles oe-tiles--3">
  <article class="oe-card">
    <span class="oe-card__icon"><i data-lucide="users"></i></span>
    <p class="oe-card__label">Partecipanti</p>
    <p class="oe-card__value">12.480</p>
    <h3 class="oe-card__title">Persone raggiunte</h3>
    <p class="oe-card__text">Una frase.</p>
  </article>
</div>
```

Card cliccabile: `<a class="oe-card" href="…">` (solleva al passaggio). Card con
foto: `.oe-card.oe-card--media` con `<img>` e poi `<div class="oe-card__content">`.
Tutti i figli sono facoltativi: tieni solo quelli che hanno contenuto.

## KPI

```html
<div class="oe-kpi">
  <span class="oe-kpi__icon"><img src="assets/icons/icon-pil.png" alt=""></span> <!-- o <i data-lucide> -->
  <p class="oe-kpi__label">Valore aggiunto</p>
  <p class="oe-kpi__value">4,80</p>
  <p class="oe-kpi__unit">mln € attivati</p>
  <p class="oe-kpi__text">Una o due frasi di lettura.</p>
</div>
```

`.oe-kpi--dark` = numero-chiave della pagina (Bluette 900, barra lime in alto):
una o due per pagina, non di più.

## Statistiche, parametri

```html
<div class="oe-stats">
  <div class="oe-stat"><p class="oe-stat__label">Durata</p><p class="oe-stat__value">36 mesi</p><p class="oe-stat__sub">da gennaio 2024</p></div>
</div>

<div class="oe-params">
  <div class="oe-param"><p class="oe-param__label">Orizzonte</p><p class="oe-param__value">20 anni</p><p class="oe-param__text">Nota breve.</p></div>
</div>
```

## Elenco per peso

```html
<ol class="oe-rank">
  <li class="oe-rank__item" style="--bar:var(--oe-bluette-900)">
    <span class="oe-rank__bar" aria-hidden="true"></span>
    <div class="oe-rank__main"><p class="oe-rank__title">Voce</p><p class="oe-rank__text">Dettaglio.</p></div>
    <div class="oe-rank__meta"><p class="oe-rank__pct">52,0%</p><p class="oe-rank__value">2,60 mln €</p></div>
  </li>
</ol>
```

Ordina dalla voce più pesante; `--bar` segue la rampa dei grafici
(900 → 500 → 300, residuo `--oe-gray-400`).

## Riquadro lime, verdetto

```html
<div class="oe-callout"><p><strong>Frase chiave.</strong> Una o due frasi.</p></div>

<div class="oe-verdict">                       <!-- .oe-verdict--negative per l'esito negativo -->
  <span class="oe-verdict__flag">Esito positivo</span>
  <p class="oe-verdict__text"><strong>Verdetto</strong> con il numero che lo giustifica.</p>
</div>
```

## Passi

```html
<ol class="oe-steps">
  <li class="oe-step"><div><h3>Titolo del passo</h3><p>Descrizione.</p></div></li>
</ol>
```

La numerazione 01, 02… è automatica (contatore CSS). Tessere scure: stanno bene
anche su sezioni chiare.

## Testo lungo

```html
<div class="oe-prose"><p>…</p><h3>…</h3><ul><li>…</li></ul></div>
```

Larghezza massima 72 caratteri; `<strong>` diventa Bluette (lime su scuro).

## Figura (grafico)

```html
<figure class="oe-figure">
  <figcaption>
    <p class="oe-figure__label">Grafico 1</p>
    <h3 class="oe-figure__title">Titolo</h3>
    <p class="oe-figure__text">Cosa mostra, in una frase.</p>
  </figcaption>
  <div class="oe-figure__chart" style="--h:320px"><canvas id="g-1"></canvas></div>
  <p class="oe-figure__source">Fonte: …</p>
</figure>
```

Numerazione progressiva senza salti. Come disegnare il grafico: `references/grafici.md`.

## Tabella

```html
<div class="oe-table-wrap">
  <table class="oe-table">
    <caption>Tabella 1 · Titolo</caption>
    <thead><tr><th scope="col">Voce</th><th scope="col" class="num">Valore</th></tr></thead>
    <tbody><tr><td>Lavori</td><td class="num">2.145,0</td></tr></tbody>
    <tfoot><tr><td>Totale</td><td class="num">3.575,0</td></tr></tfoot>
  </table>
</div>
<p class="oe-table-note">Fonte: …</p>
```

Numeri in colonne `.num` (a destra, cifre tabulari). Il wrapper scorre in
orizzontale su mobile invece di rompere la pagina.

## Footer

Copiare il blocco `<footer class="footer">` da `esempi/anteprima.html`
(sedi e tagline in `references/brand.md` § 7). Non cambiarne la struttura.

## Icone

`<i data-lucide="nome"></i>` → `lucide-inline.js` lo sostituisce con un `<svg>`
decorativo (`aria-hidden`). Se l'icona porta un significato da sola (bottone
senza testo), metti `aria-label` sull'elemento interattivo.

Nomi disponibili nel bundle: `alert-circle` `anchor` `arrow-left` `arrow-right`
`bar-chart` `bar-chart-2` `building` `calendar` `check` `chevron-right` `coin`
`cpu` `download` `external-link` `factory` `file-text` `flame` `globe`
`heart-pulse` `home` `info` `landmark` `layers` `log-in` `mail` `map` `map-pin`
`menu` `minus-circle` `pie-chart` `scatter-chart` `search` `shield`
`trending-down` `trending-up` `users` `x` `zap`.

Un nome fuori elenco non disegna nulla e scrive un avviso in console. Per
aggiungerne uno: copia i `<path>` dal sorgente ufficiale Lucide dentro l'oggetto
`icons` di `lucide-inline.js`.
