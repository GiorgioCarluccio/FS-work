# Grafici

Tutti i grafici passano da `assets/oe-charts.js` (preset per Chart.js 4.x): le
funzioni `OE.*` applicano già colori, font, formato numerico e tooltip del
brand. Non scrivere palette a mano e non chiamare `new Chart()` direttamente
se una funzione `OE.*` copre il caso.

## Dipendenza

Chart.js 4.x va caricato **prima** di `oe-charts.js`:

```html
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js" defer></script>
<script src="assets/oe-charts.js" defer></script>
```

Senza rete (consegna offline): scaricare `chart.umd.min.js` in
`assets/vendor/` e cambiare `src`. Se Chart.js manca, le funzioni `OE.*` non
disegnano niente: il blocco `if (typeof Chart === 'undefined') return;` evita
errori, ma la figura resta vuota, quindi va controllata nel browser.

## Regole di colore (non negoziabili)

1. Serie **sempre sulla rampa Bluette**: la categoria principale (diretto,
   territorio dell'intervento, prima voce) è il viola più scuro, le altre
   scalano verso il chiaro.
2. La categoria **residua o aggregata** ("Altro", "Resto d'Italia", "Other EU")
   è **grigia** `#AFAFAF` → opzione `residuo: true`.
3. **Il lime non è mai un colore di serie**: è solo UI (chip, accenti).
4. Mai verde/rosso per positivo/negativo: positivo Bluette, negativo grigio
   (è già così in `waterfall` e `flussiACB`).
5. Mappe coropletiche: rampa Bluette 050 → 900.

Rampe pronte (`OE.rampe`):

| nome | colori | uso |
|---|---|---|
| `componenti` | 700 · 500 · 300 | diretto / indiretto / indotto |
| `fasi` | 700 · 300 | CAPEX / OPEX, prima / dopo |
| `territori` | 900 · 500 · 200 · grigio | area / spillover / resto regione / resto Paese |
| `scala5` | 900 · 700 · 500 · 300 · 200 | fino a 5 categorie ordinate |

`OE.serie(n, residuo)` restituisce `n` colori dal più scuro (al massimo 6
tonalità distinguibili; oltre, raggruppa in "Altro"). `OE.colori` espone i
singoli valori (`b900` … `b050`, `grey`), allineati ai token `--oe-bluette-*`.

## Funzioni

| funzione | grafico | argomenti |
|---|---|---|
| `OE.graduatoria(id, etichette, valori, opt)` | barre orizzontali ordinate | `residuo`, `unita`, `dec`, `colori` |
| `OE.componenti(id, categorie, serie[], opt)` | barre impilate | `nomi` (default Diretto/Indiretto/Indotto), `orizzontale`, `unita`, `dec`, `colori` |
| `OE.doughnut(id, etichette, valori, opt)` | ciambella di composizione | `residuo`, `unita`, `dec`, `legenda` (`'bottom'`/`'right'`), `colori` |
| `OE.waterfall(id, voci, opt)` | cascata | `voci = [{label, valore, tipo: 'positivo' o 'negativo' o 'totale'}]`, `unita`, `dec` |
| `OE.flussiACB(id, anni, netti, cumulati, opt)` | barre annue + linea cumulata | `unita`, `dec` |

Opzione comune: `descrizione` — testo per `aria-label` del canvas (se manca si
usa il titolo della `.oe-figure`). `id` può essere l'id del `<canvas>` o
l'elemento stesso.

Formato numeri: `OE.fmt(v, dec, unita)` → `2.072,10 mln €`; `OE.pct(v, dec)` →
`27,5%`. Per una pagina in inglese impostare `OE.lingua = 'en-GB'` subito dopo
aver caricato lo script (vale per tooltip e assi).

```js
document.addEventListener('DOMContentLoaded', function () {
  if (typeof OE === 'undefined' || typeof Chart === 'undefined') return;
  OE.graduatoria('g-territori',
    ['Area di intervento', 'Resto della regione', 'Resto del Paese'],
    [2.60, 1.65, 0.75], { residuo: true, unita: 'mln €' });
});
```

## Come si presenta un grafico

- Sempre dentro `.oe-figure`: **numero** ("Grafico 1", progressivo senza
  salti), **titolo**, **una frase** su cosa mostra, **fonte** sotto.
- Altezza fissata sul contenitore (`style="--h:320px"`), non sul canvas:
  Chart.js è impostato con `maintainAspectRatio: false`.
- Un solo messaggio per grafico. Se servono due confronti, due grafici.
- Il testo accanto deve riportare gli stessi numeri del grafico, arrotondati
  allo stesso modo.
- Un grafico non è l'unico posto dove sta un dato importante: il numero chiave
  va anche nel testo o in una tabella (serve a chi usa uno screen reader e a
  chi stampa).

## Scegliere il tipo

| domanda | grafico |
|---|---|
| chi pesa di più? (categorie non ordinate) | `graduatoria` |
| com'è fatto un totale? (≤ 5 parti) | `doughnut`, oppure `graduatoria` se le parti sono di più |
| come si scompone ogni categoria? | `componenti` |
| come si arriva da A a B? | `waterfall` |
| come evolve nel tempo? | `flussiACB` (flussi + cumulato) o una linea Chart.js con `OE.colori.b900` |

Grafici di terze parti (Flourish, Datawrapper): stessi colori della rampa,
stesso font, embed dentro `.oe-figure__chart` con numero, titolo e fonte.
