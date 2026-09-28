# Checklist prima di consegnare

Da fare per intero, aprendo la pagina nel browser, non a memoria.

## Brand

- [ ] Colori solo da token `--oe-*`; nessun hex scritto a mano fuori da `oe-tokens.css`.
- [ ] Lime solo come fondo (chip, callout, bottone pop) o come testo su scuro; mai testo lime su chiaro.
- [ ] Sezioni scure su Bluette 900, mai nero; ultima sezione prima del footer chiara.
- [ ] Hedvig solo per titoli e numeri display; testo, tabelle e grafici in Atkinson; Mono solo per chip ed etichette.
- [ ] Corpo a peso 300; nessun testo sotto 12px; testo da leggere ≥ 16px.
- [ ] Spigoli vivi (eccezioni: chip 2px, card con foto 4px); bordi grigi, non neri.
- [ ] Logo nero su chiaro e bianco su scuro, dal file giusto, non ricolorato né deformato.
- [ ] Icone Lucide monoline, nessuna emoji né glifo unicode; nessuna icona vuota (avvisi `lucide-inline` in console).
- [ ] Favicon chiaro/scuro presenti.
- [ ] Footer istituzionale con tagline, sedi aggiornate e riga legale.

## Testi e numeri

- [ ] Formato italiano: `2.072,1`, anche a quattro cifre; unità `mln €`.
- [ ] Ogni grafico, tabella e riquadro di dati ha la fonte.
- [ ] Grafici numerati in modo progressivo, senza salti, con titolo e frase di lettura.
- [ ] Un numero citato in due punti è identico nei due punti.
- [ ] Somme verificate: parti = totale, quote = 100%.
- [ ] Lead entro 3–4 righe, card di una frase, niente superlativi.

## Grafici

- [ ] Serie su rampa Bluette dal più scuro; residuo grigio; nessun lime nelle serie; niente verde/rosso.
- [ ] Disegnati con le funzioni `OE.*`; canvas con `aria-label`.
- [ ] Chart.js caricato (o vendorizzato in `assets/vendor/` se la consegna è offline).

## UX e accessibilità

- [ ] Un solo `<h1>`; `h2` per sezione; niente livelli saltati.
- [ ] Link "Vai al contenuto", landmark `header/nav/main/footer`, `lang` corretto.
- [ ] Voci di nav = sezioni presenti, tutte con `href="#id"` valido.
- [ ] Tutto raggiungibile e usabile da tastiera; focus visibile ovunque (anche su scuro).
- [ ] Menu mobile che si apre, si chiude con Esc e restituisce il focus.
- [ ] Nessuno scroll orizzontale a 390px; controllata anche a 768px e 1440px.
- [ ] Colore mai unico portatore di significato.
- [ ] Immagini con `alt` sensato (vuoto se decorative).

## Tecnica

- [ ] La pagina si apre da file locale senza errori in console.
- [ ] Font caricati davvero (titoli in Hedvig, testo in Atkinson), non il fallback di sistema.
- [ ] Nessun percorso assoluto verso un altro progetto: tutto sotto `assets/` e `media/`.
- [ ] Ordine dei CSS: tokens → base → nav → footer → components.
- [ ] Su un sito esistente: niente `oe-base.css`, solo token e classi `.oe-*`.
- [ ] URL già condiviso con un cliente: non cambiarlo senza chiedere.
