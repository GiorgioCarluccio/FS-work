# Identità di brand OpenEconomics — regole

Riferimento completo. Il riepilogo operativo è in `SKILL.md`; qui ci sono i
valori, il perché e i casi limite. Tutti i valori esistono come token in
`assets/oe-tokens.css`: nel codice si usano **sempre i token**, mai l'hex.

## 1. Colore

### Ruoli

| ruolo | token | valore | uso |
|---|---|---|---|
| colore di brand | `--oe-bluette-700` / `--oe-accent` | `#4400B3` | link, bottoni primari, etichette, bordi delle card, numeri su chiaro |
| fondo scuro | `--oe-bluette-900` / `--oe-bg-dark` | `#270065` | hero, sezioni scure, footer, header delle tabelle |
| accento "pop" | `--oe-lime-400` / `--oe-pop` | `#B9FF69` | chip sopra i titoli, riquadro in evidenza, testo-accento **su scuro**, focus su scuro |
| fondo tenue | `--oe-bluette-050` / `--oe-bg-tint` | `#EFE5FF` | hover delle card, pannelli morbidi |
| fondo alternato | `--oe-gray-100` / `--oe-bg-elev` | `#F1F1F1` | sezioni alternate, tessere KPI |
| testo | `--oe-black` / `--oe-fg` | `#000000` | titoli e testo su chiaro |
| testo secondario | `--oe-gray-700` / `--oe-fg-soft` | `#545454` | testo corrente lungo, descrizioni |
| bordi | `--oe-gray-200` | `#E7E7E7` | bordi e separatori (mai neri) |

Proporzioni indicative di una pagina: bianco e grigi ~70%, Bluette ~25%
(soprattutto 900 in hero/footer e 700 per gli accenti), lime ~5%. Il lime è
un segnale: se è ovunque non segnala più niente.

La **palette secondaria** (magenta, blu, giallo, verde, ciano in `oe-tokens.css`)
serve solo per illustrazioni o, in casi eccezionali, per dataviz con molte
categorie non ordinabili. Non si usa per UI, testo o fondi.

### Coppie di contrasto (WCAG 2.1, calcolate)

| testo su fondo | rapporto | esito |
|---|---:|---|
| nero su bianco | 21,0 | ✅ tutto |
| gray-700 `#545454` su bianco | 7,6 | ✅ tutto |
| gray-600 `#6E6E6E` su bianco | 5,1 | ✅ testo normale |
| gray-500 `#999999` su bianco | 2,9 | ❌ solo decorazione, mai testo informativo |
| bluette-700 su bianco | 11,1 | ✅ tutto |
| bluette-500 `#6E1AFF` su bianco | 6,5 | ✅ tutto |
| bluette-300 `#A16AFF` su bianco | 3,5 | ⚠️ solo testo ≥24px o elementi grafici |
| **lime su bianco** | **1,2** | ❌ **mai** |
| bianco su bluette-900 | 16,5 | ✅ tutto |
| lime su bluette-900 | 13,8 | ✅ tutto |
| gray-300 `#D2D2D2` su bluette-900 | 10,9 | ✅ testo corrente su scuro |
| bluette-200 `#B991FF` su bluette-900 | 6,7 | ✅ etichette su scuro |
| nero su lime | 17,6 | ✅ chip, bottoni pop |
| bluette-900 su lime | 13,8 | ✅ riquadro in evidenza |
| bianco su bluette-700 | 11,1 | ✅ bottoni primari |
| gray-700 su gray-100 | 6,7 | ✅ testo su sezioni grigie |

Regola pratica: **su chiaro** testo nero, gray-700 o bluette-700; **su scuro**
bianco, gray-300 o lime; **su lime** nero o bluette-900.

### Colori che il brand non ha

Niente verde/rosso semaforico, niente gradienti arcobaleno, niente nero puro
come fondo di sezione. Positivo/negativo si rendono con **Bluette/grigio** più
un'etichetta testuale (vedi `.oe-verdict`).

## 2. Tipografia

| famiglia | token | ruolo |
|---|---|---|
| Hedvig Letters Serif (400) | `--oe-font-serif` | H1–H3, titoli di sezione, lead di sezione, grandi numeri display (KPI, card) |
| Atkinson Hyperlegible Next (200–800) | `--oe-font-sans` | tutto il resto: testo, nav, bottoni, tabelle, numeri nelle tabelle e nei grafici |
| Atkinson Hyperlegible Mono (500) | `--oe-font-mono` | solo chip, etichette in maiuscolo, label di figura (GRAFICO 1), unità |

Scala usata dai componenti:

| livello | dimensione | note |
|---|---|---|
| titolo hero | clamp(36px → 60px) | Hedvig, bianco; la parte in `<em>` diventa lime |
| titolo di sezione | clamp(34px → 50px) | Hedvig, interlinea 1,04 |
| lead di sezione / sottotitolo | 24px | Hedvig con barretta lime a sinistra |
| numero KPI | clamp(40px → 56px), 88px nella variante scura | Hedvig |
| testo corrente | **18px, peso 300**, interlinea 1,6–1,75 | Atkinson |
| testo di card / descrizioni | 16px | Atkinson |
| etichette, chip, label | 12–14px, maiuscolo, spaziatura +0,04/+0,14em | Mono 500 |

Minimi non negoziabili: **12px** per qualunque testo, **16px** per il testo da
leggere (fuori da dashboard e tabelle dense). Peso di default del corpo: **300**;
600 per enfasi, 700 solo per bottoni.

## 3. Logo

File in `assets/logo/`:

- `logo-black.svg` — logotipo completo nero: su bianco e fondi chiari (nav).
- `logo-white.svg` — logotipo completo bianco: su Bluette 900 e fondi scuri (footer, hero).
- `logo-mark-black.svg` — solo il simbolo (cerchio con quadrato): spazi quadrati piccoli.
- `assets/icons/favicon-black.png` / `favicon-white.png` — favicon per tema chiaro/scuro.

Regole: usare il file del colore giusto invece di ricolorarlo con `filter` o
`mix-blend-mode`; mai deformarlo, ruotarlo, metterci ombre o contorni; altezza
minima 18px (quella della nav). Questo kit non contiene le misure dell'area di
rispetto: se servono, vanno chieste a chi gestisce il brand manual, non inventate.

## 4. Forma e superfici

- **Spigolo vivo**: `border-radius: 0` ovunque. Eccezioni: 2px per chip
  (`--oe-radius-chip`), 4px per card con fotografia (`--oe-radius-media`).
  Unica forma tonda: i pallini delle legende dei grafici.
- **Mosaico**: tessere accostate con fuga di 2px (`.oe-tiles`) invece di card
  distanziate con ombra.
- **Bordi** sottili gray-200; il bordo Bluette 700 si usa solo per le card informative.
- **Ombre** quasi assenti: il brand è piatto. `--oe-shadow-2` solo come feedback di hover.
- **Hero**: Bluette 900 con trama a puntini (già in `.oe-hero`), foto a destra
  con velatura sfumata Bluette dal basso; senza foto, gradiente 800 → 900.
- **Sezioni scure** sempre su Bluette 900, **mai** sul nero.

## 5. Icone

- **Lucide monoline**, stroke 1,5–2px, colore `currentColor` (di solito
  bluette-700 su chiaro, lime su scuro). `assets/lucide-inline.js` ne contiene
  un sottoinsieme senza CDN: elenco in `references/componenti.md` § Icone.
- **Mai emoji, mai glifi unicode** (✓ ★ → ecc.) al posto delle icone.
- **Icone illustrative OE** (`assets/icons/icon-*.png`, 1024px, pittogramma
  chiaro su quadrato Bluette 900): per le tessere KPI delle grandezze economiche.

  | file | soggetto | uso |
  |---|---|---|
  | `icon-pil.png` | barre con linea | PIL / valore aggiunto |
  | `icon-produzione.png` | € con freccia in salita | valore della produzione |
  | `icon-occupazione.png` | tre persone | occupazione |
  | `icon-redditi.png` | persona con € e freccia | redditi |
  | `icon-spesa.png` | monete € | spesa / investimento |
  | `icon-gettito.png` | salvadanaio | gettito fiscale |

## 6. Voce e testi

- **Tono asciutto**: lead di 3–4 righe, descrizioni di card in una frase,
  niente superlativi. Alleggerire senza togliere contenuto.
- **Numeri in italiano**: migliaia col punto, decimali con la virgola
  (`2.072,1`), anche per i numeri a quattro cifre. In inglese il contrario.
  In JS: `Intl.NumberFormat('it-IT', { useGrouping: 'always' })` (è già in `OE.fmt`).
- **Unità**: in italiano `mln €`, i miliardi per esteso nel testo; in inglese
  `mln` e `bln` (mai `m`, `bn`). Percentuali senza spazio: `27,5%`.
- Ogni tabella, grafico o riquadro di dati ha la **fonte** sotto.
- Chip sopra i titoli: parola-categoria o "Sezione 0N", in maiuscolo mono.

## 7. Footer istituzionale

Tagline: *Trasformiamo i dati in evidenza, per decisioni a maggiore impatto.*

Sedi (verificare che siano ancora attuali prima di pubblicare):

- Via J. F. Kennedy, 57/59 — 87036 Rende (CS) — +39 0984302539
- Via Vitorchiano, 123 — 00189 Roma (RM) — +39 068414537
- Via Nino Bixio, 7 — 20129 Milano (MI)
- Sede t33 — Via Calatafimi, 1 — 60121 Ancona (AN) — +39 0719715460

Riga legale: `© <anno> OpenEconomics` + link a www.openeconomics.eu + disclaimer
di pagina. Il markup completo è in `esempi/anteprima.html`.

## 8. Fuori perimetro

Il kit vale solo per il brand OpenEconomics (Bluette + lime). **Civiqa** e gli
altri brand hanno un design system proprio: non mescolarli.
