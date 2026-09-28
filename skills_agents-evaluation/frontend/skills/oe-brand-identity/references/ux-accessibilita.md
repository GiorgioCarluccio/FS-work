# UI/UX e accessibilità

Come mettere insieme i componenti perché la pagina sia chiara, usabile e
accessibile (obiettivo: WCAG 2.1 AA). I componenti del kit rispettano già
queste regole: il rischio sta nel modo in cui si combinano e nel markup.

## 1. Gerarchia e ritmo della pagina

- **Un solo `<h1>`** (nel hero). Ogni sezione ha un `<h2>`, i sotto-blocchi `<h3>`.
  Non saltare livelli per ottenere una dimensione: la dimensione la dà la classe.
- Ordine fisso in ogni sezione: **chip → titolo → lead → contenuto**.
- **Alternare i fondi** delle sezioni (bianco / `--grey`) per separare i blocchi
  senza linee. Al massimo **una o due sezioni scure** per pagina, mai due di
  seguito. **L'ultima sezione prima del footer è chiara**: il footer è già Bluette 900.
- Il **lime** compare in pochi punti per schermata: chip, una parola in `<em>`
  nel titolo hero, un solo `.oe-callout` per sezione.
- Un **solo bottone primario** per vista; le altre azioni sono `--ghost`.
- Numeri importanti in alto (hero meta, KPI), dettagli e metodo in fondo.
- Densità: righe di testo entro 72 caratteri (`.oe-prose`), lead di 3–4 righe,
  card di una frase. Se una card ha bisogno di un paragrafo, non è una card.

## 2. Layout e responsive

| breakpoint | cosa cambia |
|---|---|
| ≥ 1200px | griglie a 4 e 6 colonne piene |
| < 1200px | `.oe-tiles--4` e `--6` passano a 2 colonne |
| ≤ 960px | nav → menu a scomparsa; hero, `.oe-split` e tessere in colonna; padding sezione 56px/24px |
| < 768px | `.oe-container` e `.oe-grid` con margini da mobile |
| ≤ 600px | `.oe-tiles--6` a una colonna; badge della nav nascosto |

- **Mai** `min-width` fisso sul `body` o larghezze in px su contenitori: la
  pagina non deve scorrere in orizzontale a 360px.
- Tabelle larghe: dentro `.oe-table-wrap` (scorre solo la tabella).
- Controllare la pagina almeno a **390px, 768px, 1440px**.
- Contenuto massimo 1440px (`.oe-section__inner`); il fondo della sezione resta
  a tutta larghezza.

## 3. Interazione

- **Link veri**: navigazione interna con `<a href="#id">`, mai `onclick` su
  `<a>` senza `href` né `<div>` cliccabili. Azioni con `<button type="button">`.
- **Focus sempre visibile**: `oe-base.css` mette un anello Bluette 500 (lime su
  scuro). Non togliere `outline` senza un sostituto equivalente.
- **Target** di almeno 44×44px per bottoni e voci di menu su mobile (il kit
  usa `min-height: 44px`).
- **L'hover non porta informazioni**: tutto ciò che appare al passaggio
  (colore, sollevamento) è decorativo. Contenuti nascosti vanno aperti con un
  `<button aria-expanded>` o con `<details><summary>`.
- La sezione sotto la nav fissa non deve finire coperta: lo gestisce
  `scroll-padding-top` in `oe-base.css`; non servono script di offset.
- Stato attivo della nav: lo imposta `oe-page.js` (`aria-current`).
- Link esterni: `target="_blank" rel="noopener"` e un'indicazione visiva
  (icona `external-link` o ↗ con `aria-hidden`).

## 4. Colore e contrasto

- Usare solo le coppie ✅ della tabella in `references/brand.md` § 1.
- **Il colore non è mai l'unico segnale**: esiti, categorie di un grafico e
  stati di errore hanno sempre anche un testo o un'etichetta.
- Testo su foto: solo sopra la velatura Bluette dell'hero, mai direttamente
  sull'immagine.
- `--oe-fg-muted` (gray-500) non basta per il testo: solo elementi decorativi.

## 5. Movimento

- Transizioni brevi con i token: `--oe-dur-fast` 140ms (colore), `--oe-dur-base`
  220ms (hover), `--oe-dur-slow` 420ms (aperture). Curva `--oe-ease`.
- Niente animazioni all'ingresso di ogni blocco, parallasse o autoplay: il brand
  è sobrio, i numeri devono essere leggibili subito.
- `prefers-reduced-motion: reduce` azzera transizioni e scroll morbido (già in
  `oe-base.css`).

## 6. Markup accessibile

- `<html lang="it">` (o `en`); `<title>` nella forma `Titolo | OpenEconomics`.
- Primo elemento del body: link "Vai al contenuto" (`.oe-skip`) verso `<main id="main">`.
- Landmark: `<header>` con `<nav aria-label>`, `<main>`, `<footer>`; ogni
  `<section>` con `aria-labelledby` verso il suo `<h2>`.
- Immagini: `alt` descrittivo se informano, `alt=""` se decorative (le icone
  PNG accanto a un'etichetta sono decorative). Hero con foto: `role="img"` e
  `aria-label` sul contenitore.
- Grafici: `role="img"` + `aria-label` sul canvas (lo fa `oe-charts.js`) e il
  dato chiave anche nel testo.
- Tabelle: `<caption>`, `<th scope="col">`, numeri in `.num`.
- Coppie etichetta/valore (meta dell'hero): `<dl>`, `<dt>`, `<dd>`.

## 7. Moduli

Il kit non ha stili dedicati ai moduli. Se servono: etichetta visibile sopra il
campo (mai solo placeholder), testo 16px (evita lo zoom su iOS), bordo
1px `--oe-gray-400`, spigolo vivo, focus con `--oe-focus-ring`, bottone
`.oe-btn`. Errori: testo esplicito sotto il campo, icona `alert-circle`,
`aria-invalid="true"` e `aria-describedby`; non introdurre il rosso, che non
è un colore del brand.

## 8. Prestazioni

- Font self-hosted in `assets/fonts/`. Quando la pagina è servita via HTTP(S)
  si possono precaricare Atkinson Next e Hedvig con
  `<link rel="preload" href="assets/fonts/…" as="font" type="font/ttf" crossorigin>`;
  non metterlo nelle pagine aperte da file locale (`file://`), dove il
  preload fallisce con un errore CORS in console. Su un sito con molto
  traffico, convertire i TTF in WOFF2.
- Immagini hero in WebP/AVIF, ~1600px di lato lungo; `loading="lazy"` per le
  immagini sotto la piega.
- Script con `defer`; Chart.js solo nelle pagine che hanno grafici.
- Asset con cache lunga: se si modifica un CSS già pubblicato, cambiare la
  query di versione (`oe-components.css?v=2`).

## 9. Pagina nuova o sito esistente

| caso | cosa caricare |
|---|---|
| **pagina o sito nuovo** | `oe-tokens.css` → `oe-base.css` → `nav.css` → `footer.css` → `oe-components.css` |
| **dentro un sito esistente** con la sua tipografia | solo `oe-tokens.css` + `oe-components.css` (e nav/footer se si sostituisce la chrome). **Non** `oe-base.css`, che cambierebbe tutte le pagine. |
| **artifact / file unico** | incollare il contenuto dei CSS in `<style>` nello stesso ordine; i font vanno serviti come file o incorporati, altrimenti si vede il fallback |
