---
name: oe-brand-identity
description: Use when building, restyling or reviewing any web page, site, landing page, HTML report, dashboard or HTML artifact for OpenEconomics (OE). Applies the OE brand identity and a ready-made frontend kit — Bluette/lime palette tokens, Atkinson Hyperlegible + Hedvig Letters Serif fonts, logos, sharp-corner components, shared nav and footer, Lucide icons, Chart.js presets — plus UI/UX and accessibility rules. Trigger su "OpenEconomics", "OE", "brand OE", "stile OpenEconomics", "identità visiva", "design system OE", "pagina/sito/landing OE", "report HTML OE", "colori OE", "font OE", "logo OE". Not for other brands (e.g. Civiqa) and not for the analytical content of a study (methodology, numbers).
---

# OpenEconomics — identità di brand e frontend

Kit per fare pagine web che sembrano OpenEconomics al primo sguardo e che
funzionano bene: brand coerente, componenti pronti, UX chiara, accessibili.
Tutto quello che serve è dentro questa cartella; nessuna build, nessun npm.

## Quando si applica

- Pagina, sito, landing, report HTML, dashboard o artifact con il marchio OE.
- Restyling di una pagina esistente sul brand OE, o review di una pagina OE.
- Domande su colori, font, logo, icone, grafici o componenti OE.

Non si applica a Civiqa o altri brand, né a documenti Word/PowerPoint. Il
contenuto analitico di uno studio (metodologia, numeri) non è compito di
questa skill: qui si decide **come appare**, non **cosa dice**.

## Procedura

1. **Capire il caso** (vedi `references/ux-accessibilita.md` § 9):
   pagina nuova, pagina dentro un sito esistente, o artifact in un file unico.
2. **Copiare gli asset** nel progetto: la cartella `assets/` di questa skill
   accanto alla pagina (font, logo, icone, CSS, JS). Nei file unici incollare
   i CSS in `<style>` nell'ordine indicato.
3. **Partire da `templates/pagina-base.html`**: ha già head, nav, hero,
   sezioni, figura, footer e script. Sostituire i `{{PLACEHOLDER}}` ed
   eliminare ciò che non serve.
4. **Comporre con i componenti** di `references/componenti.md`
   (`.oe-section`, `.oe-card`, `.oe-kpi`, `.oe-figure`, `.oe-table`, …).
   Guardare `esempi/anteprima.html` per la resa di ciascuno. Se manca un
   componente, costruirlo solo con i token `--oe-*` e le regole qui sotto.
5. **Grafici** solo con le funzioni `OE.*` di `assets/oe-charts.js`
   (`references/grafici.md`).
6. **Verificare** con `references/checklist.md`, aprendo la pagina nel
   browser a 390px, 768px e 1440px e guardando la console.

## Regole che non si rompono mai

**Colore**
- Solo token `--oe-*`, mai hex scritti a mano.
- Bluette 700 `#4400B3` è il colore di brand; Bluette 900 `#270065` per hero,
  sezioni scure e footer. **Mai nero puro** come fondo.
- **Lime `#B9FF69` mai come testo su chiaro** (contrasto 1,2:1): solo come fondo
  (chip, callout, bottone pop, con testo nero) o come testo su scuro.
- Niente verde/rosso: positivo = Bluette, negativo = grigio, più un'etichetta.

**Tipografia**
- Hedvig Letters Serif solo per titoli e grandi numeri; Atkinson Hyperlegible
  Next per tutto il resto (anche tabelle e grafici); Mono solo per chip ed etichette.
- Corpo 18px peso 300. **Minimo 12px** per qualunque testo, **16px** per il testo da leggere.

**Forma**
- Spigolo vivo (`border-radius: 0`); eccezioni solo chip 2px, card con foto 4px.
- Tessere accostate con fuga 2px; bordi grigi sottili, mai neri; ombre quasi mai.
- Chip lime sopra ogni titolo di sezione.

**Logo e icone**
- `logo-black.svg` su chiaro, `logo-white.svg` su scuro: mai ricolorare con `filter`.
- Icone Lucide monoline (stroke 1,5–2); **mai emoji o glifi unicode**.

**Grafici**
- Serie sulla rampa Bluette dal più scuro; residuo grigio `#AFAFAF`; lime mai nelle serie.
- Ogni grafico: numero progressivo, titolo, frase di lettura, fonte.

**UX e accessibilità**
- Un `<h1>`; link veri `<a href="#id">`, mai `onclick` al posto di `href`.
- Focus visibile, target ≥ 44px, niente scroll orizzontale a 360px.
- Numeri in formato italiano (`2.072,1`) e fonte sotto ogni dato.
- Su un sito esistente non caricare `oe-base.css`: cambierebbe tutte le pagine.

## File

| percorso | contenuto |
|---|---|
| `assets/oe-tokens.css` | font-face, token colore/tipo/spazi/griglia, utility `.oe-container` `.oe-grid` |
| `assets/oe-base.css` | stili dei tag nudi, focus, skip link, reduced motion (solo pagine nuove) |
| `assets/nav.css`, `assets/footer.css` | header e footer condivisi del sito |
| `assets/oe-components.css` | libreria di componenti `.oe-*` |
| `assets/oe-charts.js` | preset Chart.js (`OE.*`): colori, numeri italiani, a11y |
| `assets/oe-page.js` | menu mobile e voce di nav attiva |
| `assets/lucide-inline.js` | sottoinsieme di icone Lucide senza CDN |
| `assets/fonts/`, `assets/logo/`, `assets/icons/` | font self-hosted, logo, favicon e icone illustrative |
| `templates/pagina-base.html` | scheletro da copiare |
| `esempi/anteprima.html` | tutti i componenti con dati fittizi: riferimento visivo e test del kit |

## Riferimenti (caricare solo quando serve)

- `references/brand.md` — palette con ruoli e **tabella dei contrasti**, scala
  tipografica, logo, forme, icone, voce e testi, footer istituzionale.
- `references/componenti.md` — catalogo con markup di ogni componente, nav,
  hero, footer, elenco delle icone disponibili.
- `references/grafici.md` — regole di colore dei grafici e API `OE.*`.
- `references/ux-accessibilita.md` — gerarchia, ritmo delle sezioni,
  responsive, interazione, movimento, markup accessibile, prestazioni,
  integrazione in un sito esistente.
- `references/checklist.md` — controlli prima della consegna.

## Dipendenze

- Nessuna build. Basta un browser.
- **Chart.js 4.x** solo se la pagina ha grafici: caricato da CDN
  (`cdn.jsdelivr.net`). Senza rete scaricarlo in `assets/vendor/` e cambiare
  `src`; se manca del tutto, i grafici restano vuoti ma la pagina funziona.
- I font sono TTF self-hosted: se la pagina finisce in un sito che carica già
  Atkinson/Hedvig, togliere i `@font-face` da `oe-tokens.css`.
