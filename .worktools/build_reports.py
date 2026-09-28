from pathlib import Path
import re, json, shutil
from html import escape
from urllib.parse import quote

ROOT = Path(__file__).resolve().parent.parent
DOC = {
'jonica': '2025.06.10 Elettrificazione Jonica - Opzioni Reali (1).pdf',
'napoli': 'OE_RFI_Impatto Napoli Porto-Traccia_25012024_rev.pdf',
'roma': 'OE_RFI_Impatto Roma Pompei_30012024.pdf',
'udine': '2025.06.13 Benefici e OR Udine Cividale - Report.docx',
'parere': 'parere-csllpp-2-2025.pdf',
'trasmissione': 'trasmissione-parere-csllpp-2025.pdf'}
for pattern, target in [('CSLLPP Parere*.pdf',DOC['parere']),('25-08-05*.pdf',DOC['trasmissione'])]:
    shutil.copy2(next(ROOT.glob(pattern)), ROOT/'documenti'/target)

def url(key, page=None):
    return 'documenti/'+quote(DOC[key])+(f'#page={page}' if page else '')
def source(key, text, page=None):
    return f'<p class="oe-table-note report-source">Fonte: <a href="{url(key,page)}" target="_blank" rel="noopener">{text}</a>.</p>'
def prose(*items):
    return '<div class="oe-prose">' + ''.join('<p>'+s+'</p>' for s in items) + '</div>'
def section(id, chip, title, lead, body, tone=''):
    return f'<section class="oe-section {tone}" id="{id}" aria-labelledby="t-{id}"><div class="oe-section__inner report-body"><header class="oe-section-head"><span class="oe-chip">{chip}</span><h2 class="oe-section-head__title" id="t-{id}">{title}</h2><p class="oe-section-head__lead">{lead}</p></header>{body}</div></section>'
def table(caption, headers, rows, src):
    return '<div class="oe-table-wrap"><table class="oe-table"><caption>'+caption+'</caption><thead><tr>'+''.join(f'<th scope="col">{h}</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr><th scope="row">'+r[0]+'</th>'+''.join('<td>'+x+'</td>' for x in r[1:])+'</tr>' for r in rows)+'</tbody></table></div>'+src
def benefits(items):
    return '<div class="benefit-grid">'+''.join(f'<article class="benefit"><p class="benefit__value">{value}</p><h3>{title}</h3><p>{text}</p></article>' for title,value,text in items)+'</div>'
def takeaways(items):
    return '<ol class="takeaways">'+''.join(f'<li><h3>{title}</h3><p>{body}</p></li>' for title,body in items)+'</ol>'
def flow(label, items, caption):
    return '<figure class="report-flow"><figcaption>'+label+'</figcaption><ol>'+''.join(f'<li><span>{i+1:02}</span><h3>{title}</h3><p>{text}</p></li>' for i,(title,text) in enumerate(items))+'</ol><p class="flow-caption">'+caption+'</p></figure>'
def note(title, body):
    return f'<details class="method-note"><summary>{title}</summary><div class="oe-prose"><p>{body}</p></div></details>'
charts = []
def chart(id, num, title, lead, labels, values, unit, decimals, src, kind='graduatoria', signed=False):
    charts.append(dict(id=id,kind=kind,labels=labels,values=values,unit=unit,dec=decimals,signed=signed))
    return f'<figure class="oe-figure report-chart"><figcaption><p class="oe-figure__label">Grafico {num}</p><h3 class="oe-figure__title">{title}</h3><p class="oe-figure__text">{lead}</p></figcaption><div class="oe-figure__chart" style="--h:350px" hidden><canvas id="{id}" role="img" aria-label="{escape(title)}"></canvas></div><p class="chart-fallback">I valori del grafico sono consultabili anche nelle tabelle e nel testo della sezione.</p>{src}</figure>'
def hero(title, eyebrow, lead, meta):
    return f'<section class="report-hero" id="top"><a class="report-hero__back" href="index.html#studi"><i data-lucide="arrow-left"></i>Tutti gli studi</a><p class="report-hero__eyebrow">{eyebrow}</p><h1>{title}</h1><p class="report-hero__lead">{lead}</p><dl class="report-meta">'+''.join(f'<div><dt>{k}</dt><dd>{v}</dd></div>' for k,v in meta)+'</dl></section>'
def downloads(key, extras=[]):
    return section('fonti','Fonti e approfondimenti','Documenti completi','Il report online presenta il ragionamento, i risultati e le principali ipotesi. Gli originali consentono di approfondire i passaggi tecnici.',
        '<div class="report-downloads">'+''.join(f'<a class="oe-btn oe-btn--ghost source-link" href="{url(k)}" download><i data-lucide="download"></i>{name}</a>' for k,name in [(key,'Scarica lo studio completo ('+('DOCX' if key=='udine' else 'PDF')+')')]+extras)+'</div>')
def save(filename, body, nav):
    global charts
    p=ROOT/filename
    old=p.read_text(encoding='utf-8')
    head=old.split('<main id="main">')[0]
    head=re.sub(r'<link rel="stylesheet" href="assets/report-detail.css[^\"]*">|<script src="assets/(?:vendor/chart.umd|oe-charts|report-charts).js" defer></script>', '', head)
    footer=old[old.index('<footer class="footer">'):]
    head=re.sub(r'<ul class="nav__links">.*?</ul>', '<ul class="nav__links">'+''.join(f'<li><a href="#{id}">{label}</a></li>' for id,label in nav)+'</ul>',head,flags=re.S)
    head=head.replace('</head>','<link rel="stylesheet" href="assets/report-detail.css?v=1"><script src="assets/vendor/chart.umd.js" defer></script><script src="assets/oe-charts.js" defer></script><script src="assets/report-charts.js" defer></script></head>')
    p.write_text(head+'<main id="main">\n'+body+'\n</main><script type="application/json" id="report-chart-data">'+json.dumps(charts,ensure_ascii=False)+'</script>'+footer,encoding='utf-8')
    charts=[]

# JONICA
body=hero('Linea Jonica: il valore di una rete che si completa',
'Calabria · Giugno 2025 · Esito istruttorio luglio 2025',
'Per valutare il Lotto 4 occorre misurare anche ciò che rende possibile: completare l’elettrificazione e integrare i servizi sulle due coste. L’analisi delle opzioni reali ha avuto un ruolo determinante nel percorso verso il parere favorevole del CSLLPP.',
[('Intervento','Catanzaro Lido–Roccella Jonica'),('Valore economico esteso','11,41 mln €'),('Esito','Parere n. 2/2025 · con prescrizioni')])
body+=section('sintesi','Main takeaways','Tre elementi per leggere il risultato','Dalla valutazione del singolo lotto al valore delle decisioni successive.',
takeaways([
('La rete cambia il perimetro della valutazione','Il Lotto 4 isolato ha un VANE di −38,12 mln €. Il completamento e l’integrazione dei servizi abilitano opportunità ulteriori, che l’analisi valuta esplicitamente.'),
('La flessibilità ha un valore economico','Espansione e sviluppo valgono 69,08 e 20,17 mln €. Sottraendo l’opzione di attesa di 39,72 mln €, il valore esteso risulta positivo per 11,41 mln €.'),
('Il contributo all’istruttoria è documentato','Il Consiglio riconosce l’adeguatezza dell’integrazione ACB–AOR e considera soddisfatta la richiesta. Il 25 luglio 2025 esprime all’unanimità parere per la prosecuzione dell’iter, con prescrizioni.')
])+source('jonica','Studio Jonica, pp. 26–35',26)+source('parere','Parere CSLLPP n. 2/2025, pp. 16–17 e 90',16))
body+=section('razionale','La domanda di valutazione','Perché un lotto isolato non racconta tutto','Il problema nasce dalla differenza tra l’oggetto del PFTE e il perimetro della prima analisi economica.',
prose(
'Il PFTE riguarda il <strong>Lotto 4, Catanzaro Lido–Roccella Jonica</strong>. La prima analisi costi-benefici considerava invece il <em>Global Project</em>, composto dai lotti 4 e 5, fino a Melito Porto Salvo. Il Consiglio ha chiesto un’ACB del Lotto 4 o elementi utili a valutarlo autonomamente: serviva rendere esplicito quanto del valore dipendesse dal tratto in esame e quanto dalle fasi successive.',
'L’ACB del solo Lotto 4 mantiene un’impostazione prudenziale: valuta il cambio di trazione sui servizi regionali esistenti, senza ipotizzare nuovi passeggeri o diversione modale. Il volume convertito è di circa <strong>0,367 milioni di treni·km annui</strong>, contro 1,089 milioni per i due lotti. La minore intensità dei servizi sul Lotto 4 limita i risparmi monetizzabili a fronte dell’investimento.',
'Arrestare il programma a Roccella Jonica lascerebbe inoltre una discontinuità tra trazione elettrica e diesel. La domanda strategica diventa quindi: quale valore attribuire oggi alla possibilità di proseguire il programma, quando saranno disponibili maggiori informazioni? L’AOR misura questa flessibilità e rende visibili le dipendenze tra le decisioni.'
)+flow('Schema 1 · La sequenza delle decisioni',[
('Lotto 4','Elettrificare Catanzaro Lido–Roccella Jonica.'),
('Opzione di espansione','Valutare il completamento del Lotto 5 fino a Melito Porto Salvo.'),
('Opzione di sviluppo','Integrare i servizi Jonica–Tirrenica e ridurre le rotture di viaggio.')
],'Schema concettuale della valutazione; le fasi successive costituiscono opportunità, non risultati già realizzati.')+source('jonica','Studio Jonica, pp. 26–33',26),'oe-section--grey')
body+=section('benefici','Come si genera valore','Dai costi di esercizio alla continuità del viaggio','Lo studio distingue i benefici già inclusi nell’ACB dalle opportunità aggiuntive valutate con le opzioni reali.',
benefits([
('Costi operativi','ACB di base','La trazione elettrica riduce il costo di produzione del servizio rispetto a quella termica. Il beneficio è commisurato ai treni·km regionali effettivamente convertiti, mantenendo costante l’offerta.'),
('Esternalità ambientali','ACB di base','Il nuovo materiale rotabile modifica emissioni climalteranti, inquinanti e rumore. I parametri tecnico-economici restano coerenti con l’ACB del progetto complessivo.'),
('Completamento della direttrice','Espansione · 69,08 mln €','Realizzare il Lotto 5 permette di estendere la trazione elettrica lungo la costa e di monetizzare le esternalità del completamento. Il valore è quello dell’opportunità di investire successivamente, confrontata con il relativo costo.'),
('Viaggi senza discontinuità','Sviluppo · 20,17 mln €','L’integrazione tra Jonica e Tirrenica e la riduzione dei cambi di treno generano risparmi di tempo. Lo scenario assume 20 minuti per il 30% dei passeggeri della Jonica e il 15% di quelli della Tirrenica, senza crescita futura della domanda.'),
('Informazione e rinvio','Attesa · 39,72 mln €','Attendere può consentire di acquisire informazioni e ridurre l’incertezza. Impegnarsi oggi comporta la rinuncia a questa facoltà: per questo l’opzione di attesa viene sottratta nel bilancio esteso.'),
('Effetti qualitativi','Benefici non tutti monetizzati','Continuità di trazione, eliminazione dei rifornimenti diesel, turni del materiale rotabile e attrattività dei servizi descrivono ulteriori meccanismi di valore. Non sono aggiunti come importi autonomi al totale.')
])+source('jonica','Studio Jonica, pp. 26–28 e 31–35',31))
body+=section('risultati','Risultati e sensibilità','Come si arriva a 11,41 milioni di euro','Il valore esteso combina il risultato del Lotto 4 con le opzioni create e quella sacrificata.',
chart('jonica-bilancio',1,'Le componenti del valore economico esteso','I contributi positivi sono in Bluette; quelli sottratti sono in grigio. Valori in mln €.',
['ACB Lotto 4','Espansione','Sviluppo','Attesa'],[-38.12,69.08,20.17,-39.72],'mln €',2,source('jonica','Studio Jonica, p. 35',35),signed=True)+
table('Bilancio del valore esteso',['Componente','Valore (mln €)'],[
['A · VANE dell’ACB del Lotto 4','−38,12'],['B · Opzione di espansione','+69,08'],['C · Opzione di sviluppo','+20,17'],['D · Opzione di attesa da sottrarre','−39,72'],['A + B + C − D · Valore esteso','11,41']
],source('jonica','Studio Jonica, p. 35',35))+
prose('Le opzioni sono valutate su <strong>cinque anni</strong> con un tasso del <strong>3%</strong>. Per l’espansione, il sottostante è di 148,26 mln €, il costo di esercizio dell’opzione è di 92,52 mln € e la volatilità iniziale del 15%. Per lo sviluppo, i valori sono rispettivamente 35,20 mln €, 17,60 mln € e 20%. Questi parametri descrivono scenari di valutazione, non finanziamenti già assegnati.')+
table('Sensibilità delle opzioni',['Opzione','Caso base','Intervallo degli scenari analizzati'],[['Espansione','69,08 mln €','53,88–88,84 mln €'],['Sviluppo','20,17 mln €','6,68–34,65 mln €']],source('jonica','Studio Jonica, pp. 31–33',31))+
note('Come interpretare scenari e sensibilità','Gli intervalli derivano dalle combinazioni di ipotesi analizzate nel report e non sono intervalli di confidenza statistica. Il VANE di 17,62 mln € del Global Project, l’ACB isolata del Lotto 4 e il valore esteso di 11,41 mln € hanno perimetri diversi: non vanno sommati. Il Consiglio richiama il ruolo del completamento del Lotto 5 nel breve periodo, nell’orizzonte di cinque anni considerato dall’AOR.'),'oe-section--grey')
body+=section('parere','Esito documentato','Il ruolo determinante delle opzioni reali nell’istruttoria','Il parere consente di seguire il passaggio dalla richiesta di integrazione alla valutazione favorevole.',
flow('Schema 2 · Dalla richiesta all’esito',[
('Richiesta del Consiglio','Valutare il Lotto 4 separatamente dal Global Project: parere, p. 14.'),
('Integrazione ACB–AOR','Quantificare la flessibilità e il valore delle fasi successive: pp. 15–16.'),
('Riscontro favorevole','Richiesta soddisfatta sul piano economico; prosecuzione dell’iter con prescrizioni: pp. 17 e 90.')
],'Adunanza del 25 luglio 2025; parere trasmesso a RFI il 5 agosto 2025.')+
prose(
'<strong>L’analisi sviluppata da OpenEconomics per RFI è stata determinante nel rispondere al nodo economico dell’istruttoria.</strong> A p. 16 il Consiglio riporta il valore positivo di 11,41 mln € e riconosce la congruenza dell’ACB integrata dall’AOR con l’impostazione UE/2014 e con le linee guida PFTE richiamate nel documento.',
'A p. 17 il parere conclude: <q>Si ritiene pertanto che quanto prodotto dal proponente risponda alle richieste di integrazioni.</q> Questa formulazione documenta l’accoglimento del riscontro sul tema economico. Il parere richiama anche la dipendenza del risultato positivo dall’avvio del Lotto 5 e dalle prospettive di integrazione.',
'Il dispositivo finale, adottato all’unanimità, esprime parere affinché il PFTE <strong>possa proseguire nell’iter</strong>. Restano da ottemperare le prescrizioni, secondo le tempistiche indicate, e da considerare osservazioni e raccomandazioni. L’esito favorevole va dunque letto come un passaggio istruttorio qualificante, con condizioni da recepire nelle fasi successive.'
)+source('parere','Parere n. 2/2025, pp. 16–17',16)+source('parere','Dispositivo finale, p. 90',90)+source('trasmissione','Nota di trasmissione, protocollo 9832 del 5 agosto 2025'))
body+=downloads('jonica',[('parere','Scarica il parere CSLLPP (PDF)'),('trasmissione','Scarica la nota di trasmissione (PDF)')])
save('report-elettrificazione-jonica.html',body,[('razionale','Razionale'),('benefici','Benefici'),('risultati','Risultati'),('parere','Parere CSLLPP')])

# NAPOLI
body=hero('Napoli Porto–Traccia: scegliere come riconnettere il porto',
'Campania · Gennaio 2024 · Collegamento ferroviario merci',
'Confrontare due soluzioni tecniche significa leggere insieme costi, benefici per la collettività e ricadute della spesa. Lo studio fornisce a RFI una base economica per scegliere tra binario a raso e binario interrato.',
[('Alternativa preferita','Binario a raso'),('Benefici/costi economici','6,6 contro 4,9'),('Metodo','SAM e validazione dell’ACB RFI')])
body+=section('sintesi','Main takeaways','Tre risultati per la decisione','Le due alternative ripristinano lo stesso collegamento, con costi diversi.',
takeaways([
('La soluzione a raso usa meno risorse','I benefici economici sono quasi equivalenti: 559,9 contro 561,1 mln €. I costi economici scendono da 114,4 a 84,7 mln € nella variante a raso.'),
('Il beneficio pubblico supera il ritorno finanziario','Entrambe le varianti hanno rapporti economici maggiori di 1, ma rapporti finanziari inferiori a 1. Una parte del valore ricade su utenti e collettività.'),
('Un impatto sul PIL maggiore non decide da solo','La soluzione interrata attiva più spesa e più valore aggiunto, ma presenta minore efficienza economica. La scelta richiede il confronto tra benefici e costi.')
])+source('napoli','Studio Napoli Porto–Traccia, pp. 7–10',7))
body+=section('razionale','Razionale e alternative','Due modi di risolvere l’interferenza con la strada','Il riferimento è lo scenario privo del collegamento ferroviario.',
prose(
'Il progetto ripristina la connessione tra il <strong>Porto di Napoli e il fascio basso di Napoli Traccia</strong>. Il nodo tecnico è l’interferenza del binario con via Galileo Ferraris: il collegamento deve essere ripristinato tenendo conto della viabilità urbana.',
'La <strong>soluzione interrata</strong> abbassa il binario e mantiene la viabilità comunale attuale. La <strong>soluzione a raso</strong> mantiene il binario al livello esistente e prevede l’interramento della strada, con sistemazione degli svincoli di adduzione. La distinzione riguarda quindi quale infrastruttura interrare.',
'Lo studio risponde a due domande complementari. L’ACB valuta il cambiamento di benessere rispetto all’assenza del servizio ferroviario. Il modello SAM stima come la spesa di costruzione ed esercizio si propaga nell’economia. OpenEconomics realizza l’analisi di impatto e valida l’ACB prodotta da RFI.'
)+table('Risorse previste nei due scenari',['Voce','Binario a raso','Binario interrato'],[
['Spesa capitale 2024–2027, valore attuale','34,63 mln €','74,45 mln €'],
['Costi di esercizio 2028–2053','206,43 mln €','206,63 mln €']
],source('napoli','Studio Napoli Porto–Traccia, p. 7',7)),'oe-section--grey')
body+=section('benefici','Benefici per la collettività','Che cosa cambia grazie al collegamento','Il valore sociale comprende costi evitati e minori esternalità.',
benefits([
('Manutenzione veicolare','340,5 mln € · a raso','Il ripristino ferroviario modifica l’impiego del trasporto su strada e i costi di manutenzione dei veicoli. È la componente prevalente del beneficio economico: una riduzione del consumo di risorse del sistema di trasporto.'),
('Ambiente','183,9 mln € · a raso','La valutazione monetizza la riduzione dei costi esterni ambientali associati al trasporto. Questi effetti riguardano la collettività e non si traducono necessariamente in ricavi del gestore. Il report li presenta come aggregato ambientale.'),
('Tempo','34,5 mln € · a raso','Il tempo risparmiato ha un valore economico anche quando non genera un pagamento. La voce esprime il beneficio temporale attribuito al cambiamento del sistema di trasporto nello scenario con progetto.'),
('Sicurezza','1,0 mln € · a raso','La variazione dell’incidentalità riduce i costi sociali legati agli incidenti. Il beneficio completa la valutazione insieme a manutenzione, ambiente e tempo.')
])+chart('napoli-benefici',1,'La composizione dei benefici della variante a raso','Manutenzione veicolare e ambiente costituiscono le componenti principali.',
['Manutenzione veicolare','Ambiente','Tempo','Incidentalità'],[340.5,183.9,34.5,1.0],'mln €',1,source('napoli','ACB RFI validata da OpenEconomics, p. 10',10),kind='doughnut')+
table('Benefici economici per componente',['Componente','A raso · mln €','Interrata · mln €'],[
['Manutenzione veicolare','340,5','341,2'],['Ambiente','183,9','184,4'],['Tempo','34,5','34,5'],['Incidentalità','1,0','1,0'],['Totale riportato nel documento','559,9','561,1']
],source('napoli','Studio Napoli Porto–Traccia, p. 10; valori arrotondati',10)))
body+=section('risultati','Confronto economico','Perché la variante a raso è preferibile','La scelta emerge dal valore generato in rapporto alle risorse impiegate.',
chart('napoli-bc',2,'Benefici per euro di costo economico','Entrambe le alternative superano la soglia di convenienza di 1; la variante a raso presenta il rapporto più alto.',
['A raso','Interrata'],[6.6,4.9],'',1,source('napoli','Studio Napoli Porto–Traccia, p. 9',9))+
table('Indicatori di sostenibilità',['Indicatore','A raso','Interrata'],[
['Costi economici','84,7 mln €','114,4 mln €'],['Benefici economici','559,9 mln €','561,1 mln €'],
['VAN economico riportato','475,1 mln €','446,7 mln €'],['Rapporto B/C economico','6,6','4,9'],
['Rapporto B/C finanziario','0,7','0,5'],['VAN finanziario','−31,3 mln €','−69,4 mln €']
],source('napoli','Studio Napoli Porto–Traccia, p. 9',9))+
prose('L’analisi economica considera l’interesse della società; quella finanziaria considera i flussi monetari del progetto. I rapporti finanziari inferiori a 1 indicano che i benefici monetari non coprono i costi finanziari nelle ipotesi esaminate. I benefici sociali, invece, sono ampiamente superiori ai costi economici. Il risultato sostiene la preferenza per la soluzione a raso, mantenendo distinta la questione del finanziamento.'),
'oe-section--grey')
body+=section('impatto','Metodo e impatti','Come la spesa si trasmette all’economia','Il modello SAM ricostruisce le interdipendenze tra attività produttive, famiglie e settore pubblico.',
flow('Schema 1 · I canali della Matrice di Contabilità Sociale',[
('Diretto','Acquisti e attività nei settori cui è attribuita la spesa del progetto.'),
('Indiretto','Forniture intermedie e domanda attivata lungo le catene produttive.'),
('Indotto','Reimpiego dei redditi delle famiglie e delle entrate fiscali nel circuito economico.')
],'Le voci di spesa sono attribuite ai settori ATECO. Il modello utilizza dati statistici ISTAT, Eurostat e OECD, con disaggregazione regionale.')+
table('Impatti socioeconomici nazionali',['Indicatore','A raso','Interrata'],[
['PIL / valore aggiunto','375 mln €','465 mln €'],['Occupati stabili equivalenti a tempo pieno','242 ETP','281 ETP'],
['Redditi delle famiglie','369 mln €','458 mln €'],['Entrate fiscali','168 mln €','208 mln €']
],source('napoli','Studio Napoli Porto–Traccia, pp. 4–7',4))+
prose('L’alternativa interrata attiva un impatto maggiore anche perché richiede più spesa. Il risultato SAM descrive la propagazione di quella domanda, mentre l’ACB stabilisce se il cambiamento di benessere giustifica le risorse assorbite. Per la decisione le due letture vanno usate insieme.'),
note('Come leggere gli indicatori senza doppi conteggi','PIL, redditi e gettito sono prospettive diverse dello stesso processo economico: non vanno sommati tra loro né aggiunti ai benefici dell’ACB. Gli ETP esprimono occupazione equivalente a tempo pieno secondo il report, non un numero di assunzioni nominative. Le tabelle conservano gli arrotondamenti del documento; possono quindi emergere piccoli scarti tra somme e totali.'))
body+=downloads('napoli')
save('report-napoli-porto-traccia.html',body,[('razionale','Razionale'),('benefici','Benefici'),('risultati','Confronto'),('impatto','Impatto')])

# ROMA
body=hero('Roma–Pompei: accessibilità, cultura e valore economico',
'Lazio e Campania · Gennaio 2024 · Valutazione del servizio 2023',
'Un collegamento diretto può rendere possibile una visita che altrimenti non avverrebbe. La valutazione misura il valore dell’esperienza per gli utenti, gli effetti sui trasporti e le ricadute della spesa turistica.',
[('Servizio osservato','23 corse · circa 7.000 viaggiatori'),('Benefici economici','930.770 €'),('Benefici/costi','14,8 · scenario ferroviario')])
body+=section('sintesi','Main takeaways','Il valore della connessione diretta','La fruizione culturale è il principale meccanismo di beneficio.',
takeaways([
('L’esperienza di visita pesa più delle sole emissioni','Il valore del tempo libero è stimato in 828.000 €. Insieme alla minore congestione, spiega la maggior parte dei benefici economici.'),
('Il confronto modale favorisce il treno','Il rapporto benefici/costi è 14,8 per il servizio ferroviario e 7,5 per l’autobus ipotetico. Le due opzioni producono effetti diversi anche sulla congestione.'),
('Il turismo genera ricadute ulteriori da leggere separatamente','Una spesa turistica di circa 642 mila € attiva 1,7 mln € di valore aggiunto nazionale e 20,8 ETP secondo il modello SAM.')
])+source('roma','Studio Roma–Pompei, pp. 3–7',3))
body+=section('razionale','Razionale e metodo','Valutare un servizio che rende accessibile la visita','Il confronto è con ciò che sarebbe accaduto in assenza del collegamento.',
prose(
'Nel 2023 il collegamento diretto <strong>Roma Termini–Pompei</strong> ha effettuato 23 corse, portando circa 7.000 persone a visitare il parco archeologico. Lo studio aggiornato al 30 gennaio 2024 valuta il beneficio del servizio per gli utenti e la collettività e, separatamente, l’impatto economico della spesa dei visitatori.',
'L’ipotesi centrale è l’<strong>addizionalità della visita</strong>: in assenza del servizio, solo il 20% degli utenti avrebbe effettuato l’esperienza di viaggio e visita. Questa assunzione attribuisce al collegamento un ruolo abilitante e influenza in modo decisivo il valore del tempo libero. È un’ipotesi del modello, non una proprietà automatica di ogni passeggero trasportato.',
'L’ACB utilizza le linee guida per la valutazione degli investimenti ferroviari e include la fruizione culturale. I costi di gestione ferroviari indicati sono 70.000 €, trasformati in <strong>63.000 € di costi economici</strong> tramite un fattore di conversione. Le grandezze finanziarie e quelle economiche sono quindi distinte.'
)+flow('Schema 1 · Dall’accessibilità ai due percorsi di valore',[
('Collegamento diretto','Rende più accessibile il viaggio e la visita al parco.'),
('Benefici sociali · ACB','Esperienza culturale, congestione, sicurezza ed esternalità del trasporto.'),
('Spesa turistica · SAM','Domanda di beni e servizi e ricadute su produzione, redditi e lavoro.')
],'ACB e SAM rispondono a domande diverse; i relativi risultati non vengono sommati.')+source('roma','Studio Roma–Pompei, pp. 3–6',3),'oe-section--grey')
body+=section('benefici','I singoli benefici','Che cosa è incluso nel risultato economico','La valutazione mantiene anche le componenti negative.',
benefits([
('Tempo libero e fruizione del sito','+828.000 €','Il beneficio principale riguarda il valore dell’esperienza di viaggio e visita resa possibile dal servizio. È collegato all’ipotesi sui visitatori aggiuntivi; non va interpretato come fatturato del parco o come solo risparmio di minuti in treno.'),
('Congestione stradale','+101.821 €','Il trasferimento della mobilità dal sistema stradale al collegamento ferroviario riduce il costo esterno della congestione nello scenario valutato. È una delle voci che differenzia maggiormente il treno dall’autobus.'),
('Gas climalteranti','+2.618 €','La differenza di emissioni è valorizzata economicamente. Il saldo climatico contribuisce positivamente al beneficio totale, con un peso inferiore a quello del tempo libero e della congestione.'),
('Incidentalità','+533 €','La voce monetizza la variazione dei costi sociali degli incidenti associata al diverso assetto degli spostamenti. Nel caso ferroviario il saldo riportato è positivo.'),
('Inquinanti atmosferici','−2.134 €','Il saldo locale degli inquinanti è negativo. Il report conserva questo costo nell’aggregato: il risultato complessivo favorevole non implica un miglioramento di ogni componente ambientale.'),
('Rumore','−68 €','Le emissioni acustiche determinano una piccola componente negativa. Il suo peso è marginale sul totale, ma resta incluso per completezza del bilancio.')
])+table('Bilancio dei benefici ferroviari',['Voce','Valore'],[
['Tempo libero','828.000 €'],['Congestione','101.821 €'],['Gas climalteranti','2.618 €'],['Incidentalità','533 €'],['Inquinanti','−2.134 €'],['Rumore','−68 €'],['Totale benefici economici','930.770 €'],['Costi economici','63.000 €'],['Rapporto benefici/costi','14,8']
],source('roma','Studio Roma–Pompei, p. 4',4))+
chart('roma-benefici',1,'Il contributo delle sei componenti','Tempo libero e congestione dominano il risultato; le componenti negative, piccole su questa scala, sono leggibili nella tabella.',
['Tempo libero','Congestione','Gas climalteranti','Incidentalità','Inquinanti','Rumore'],[828000,101821,2618,533,-2134,-68],'€',0,source('roma','Studio Roma–Pompei, p. 4',4),signed=True))
body+=section('confronto','Alternativa di servizio','Perché l’autobus produce un risultato diverso','Lo scenario su gomma mantiene le ipotesi di flusso turistico usate per il treno.',
prose('L’alternativa autobus è uno scenario ipotetico sulla stessa relazione, introdotto per confrontare il valore delle due modalità. Il costo di gestione è più basso, ma anche i benefici sono inferiori. La voce congestione passa da un beneficio nel caso ferroviario a un costo nello scenario autobus: questo effetto assorbe una parte consistente del valore del tempo libero.')+
chart('roma-bc',2,'Confronto dei rapporti benefici/costi','Il servizio ferroviario presenta il rapporto più elevato nelle ipotesi del report.',
['Treno','Autobus'],[14.8,7.5],'',1,source('roma','Studio Roma–Pompei, pp. 4–5',4))+
table('Confronto tra le due modalità',['Indicatore','Treno','Autobus'],[
['Valore del tempo libero','828.000 €','662.400 €'],['Congestione stradale','101.821 €','−427.647 €'],
['Benefici economici totali','930.770 €','234.048 €'],['Costi economici','63.000 €','31.050 €'],
['Beneficio per utente riportato','circa 135 €','circa 34 €'],['Rapporto benefici/costi','14,8','7,5']
],source('roma','Studio Roma–Pompei, pp. 4–5',4)),'oe-section--grey')
body+=section('impatto','Ricadute sul territorio','Come la visita diventa domanda economica','Il modello SAM segue la spesa turistica nell’economia provinciale e nazionale.',
prose('La seconda analisi assume una spesa media giornaliera di <strong>93 € per turista</strong>, al netto di viaggio e alloggio, sulla base del dato ISNART 2023 richiamato nello studio. Applicata ai 6.900 visitatori utilizzati nel modello, produce una spesa di circa 642 mila €. La SAM rappresenta gli scambi fra settori e istituzioni e stima gli effetti diretti, indiretti e indotti.')+
table('Impatti della spesa turistica',['Indicatore','Provincia di Napoli','Italia, inclusa la provincia'],[
['PIL / valore aggiunto','462 mila €','1,7 mln €'],['Occupazione equivalente a tempo pieno','6,3 ETP','20,8 ETP'],['Redditi delle famiglie','480 mila €','1,7 mln €']
],source('roma','Studio Roma–Pompei, pp. 6–7',6))+
prose('Il report indica inoltre <strong>467 mila € di entrate fiscali</strong>. I valori locali sono compresi in quelli nazionali. Il valore aggiunto descrive l’attività economica attivata dalla spesa; i benefici dell’ACB esprimono invece un cambiamento di benessere. Non costituiscono componenti di un unico totale.')+
note('Nota sulle ipotesi di domanda del documento','Il documento riporta circa 7.000 viaggiatori e indica 6.900 come incrementali con etichetta “80%”. Queste due quantità non sono aritmeticamente coerenti: l’80% di 7.000 è 5.600. Il report online conserva i risultati pubblicati, senza ricalcolarli: 6.900 è la base indicata per la spesa turistica. Anche i valori per utente sono quelli della fonte. L’assunzione di addizionalità e la sua base numerica vanno considerate quando si riutilizzano le stime.'))
body+=downloads('roma')
save('report-roma-pompei.html',body,[('razionale','Razionale'),('benefici','Benefici'),('confronto','Confronto'),('impatto','Impatto')])

# UDINE
body=hero('Udine–Cividale: dal ripristino al valore dell’integrazione',
'Friuli-Venezia Giulia · Giugno 2025 · Benefici e opzioni reali',
'Il subentro di RFI offre l’occasione di leggere insieme riapertura, prestazioni della linea ed elettrificazione. Lo studio valorizza i benefici per la collettività e le opportunità di servizi più frequenti e meglio connessi.',
[('Orizzonte di valutazione','30 anni'),('Benefici attualizzati','37,58 mln € · tasso 3%'),('Opzioni reali','6,09 mln € complessivi')])
body+=section('sintesi','Main takeaways','Tre leve per il valore della linea','Il tempo risparmiato, la tecnologia di trazione e le connessioni future hanno ruoli distinti.',
takeaways([
('La riapertura recupera accessibilità','Il servizio ferroviario potenziato è stimato in 20 minuti: 15 minuti in meno del bus sostitutivo e 9 in meno dell’auto.'),
('L’elettrificazione modifica il bilancio ambientale','Il periodo iniziale diesel presenta criticità per rumore e inquinanti. Il passaggio all’elettrico, previsto dal 2028 nello studio, migliora queste componenti.'),
('L’integrazione rende possibili servizi ulteriori','Le opzioni di sviluppo e integrazione valgono rispettivamente 3,89 e 2,20 mln €. Sono opportunità future, condizionate a nuove scelte di offerta.')
])+source('udine','Studio Udine–Cividale, sintesi esecutiva e §§ 4–6'))
body+=section('razionale','Razionale e scenario','Che cosa cambia con il subentro di RFI','Il confronto parte dalla situazione descritta nel giugno 2025, con il servizio ferroviario sospeso.',
prose(
'La linea regionale, lunga circa <strong>15 km</strong>, era chiusa all’esercizio ferroviario da maggio 2024; il trasporto pubblico era assicurato da autobus sostitutivi. Prima della chiusura, limitazioni legate ai sistemi di sicurezza imponevano velocità massima di 50 km/h e vincoli alla circolazione contemporanea dei treni.',
'Il programma combina adeguamento infrastrutturale e tecnologico, riapertura, miglioramento delle prestazioni ed elettrificazione. Nel modello, il ripristino avviene nel 2026, con un biennio iniziale diesel e passaggio alla trazione elettrica dal 2028. Sono le <strong>ipotesi temporali del report del 2025</strong>, non un aggiornamento dello stato dei lavori.',
'La decisione di investimento per il ripristino era già assunta dalla Regione. La metodologia dell’ACB è quindi applicata alla <strong>valorizzazione dei benefici</strong> del nuovo assetto rispetto all’assenza del servizio ferroviario. I 37,58 mln € rappresentano benefici attualizzati: non sono un VAN al netto di tutti i costi del progetto né un rapporto benefici/costi.'
)+flow('Schema 1 · Le fasi considerate nella valutazione',[
('Scenario di riferimento','Assenza del servizio ferroviario; mobilità su strada.'),
('2026–2027 · ripristino','Treni diesel, migliori prestazioni e trasferimento di utenti dalla strada.'),
('Dal 2028 · elettrificazione','Trazione elettrica e opportunità di integrazione nella rete nazionale.')
],'La valorizzazione dei benefici si estende su 30 anni; le opzioni successive sono valutate separatamente.')+source('udine','Studio Udine–Cividale, §§ 1–3'),'oe-section--grey')
body+=section('benefici','I singoli benefici','Come si costruisce il beneficio sociale','Le quantità di traffico e i tempi vengono trasformati in valori economici tramite parametri unitari.',
benefits([
('Risparmio di tempo','889.079 € all’anno','Il tempo evitato è moltiplicato per gli utenti e per il valore dell’ora-passeggero. Il report attribuisce 829.559 € agli utenti provenienti dall’auto e 59.520 € a quelli del bus. Le tariffe temporali considerate sono 18,91 e 10,41 €/passeggero-ora.'),
('Congestione stradale','220.403 € all’anno','La riduzione di circa 3,38 milioni di veicoli·km e 198 mila bus·km annui libera capacità sulla rete stradale. I chilometri evitati sono valorizzati con i costi unitari di congestione utilizzati nello studio.'),
('Incidentalità','circa 68.200 € all’anno','Il minore traffico di veicoli leggeri riduce l’esposizione al rischio stradale. La stima applica un costo marginale ai veicoli·km evitati; il contributo dei bus non è valorizzato separatamente.'),
('Rumore','Una transizione in due fasi','Nel biennio diesel il report stima un saldo acustico di circa −780.242 €/anno. Dal 2028 valorizza la minore rumorosità dell’elettrico rispetto al diesel e il minor traffico su strada, riportando 431.999 €/anno secondo il proprio schema di calcolo.'),
('Emissioni climalteranti','CO₂ e produzione elettrica','La valutazione considera le emissioni stradali evitate, quelle dei treni diesel e le emissioni indirette associate all’elettricità. La trazione elettrica non equivale quindi ad assenza di emissioni lungo l’intera catena energetica.'),
('Qualità dell’aria','NOₓ · SO₂ · NMVOC · PM₂,₅','I flussi emissivi sono monetizzati attraverso costi di danno per sostanza. Il diesel iniziale penalizza il saldo degli inquinanti; l’elettrificazione elimina le emissioni dirette locali della trazione e migliora il risultato di lungo periodo.')
])+source('udine','Studio Udine–Cividale, §§ 4.2.1–4.2.5')+
chart('udine-tempi',1,'Tempi di percorrenza utilizzati nel modello','Il treno potenziato è confrontato con le modalità su strada nello scenario di riferimento.',
['Bus sostitutivo','Auto','Treno potenziato'],[35,29,20],'minuti',0,source('udine','Studio Udine–Cividale, § 4.2.1'))+
table('Tempi e benefici ricorrenti',['Voce','Valore'],[
['Tempo medio bus / auto / treno potenziato','35 / 29 / 20 minuti'],['Risparmio rispetto al bus / all’auto','15 / 9 minuti per tratta'],
['Beneficio annuo di tempo','889.079 €'],['Beneficio annuo di congestione','220.403 €'],['Beneficio annuo di incidentalità','circa 68.200 €']
],source('udine','Studio Udine–Cividale, §§ 4.2.1–4.2.3'))+
note('Lettura delle componenti ambientali','Le valorizzazioni di rumore e CO₂ dal 2028 includono il miglioramento rispetto alla trazione diesel e lo shift modale, come definiti nel report. Questo riferimento va esplicitato quando si confrontano le fasi: non si ricostruisce qui un nuovo saldo rispetto all’assenza della ferrovia. I valori annui di alcune componenti non costituiscono una scomposizione completa del totale trentennale.'))
body+=section('opzioni','Il valore delle scelte future','Servizi più frequenti e meglio connessi','Il subentro crea possibilità che vanno oltre gli interventi già programmati.',
prose(
'Considerare immutato il servizio per 30 anni trascurerebbe parte del potenziale della nuova gestione. L’analisi delle opzioni reali valuta il diritto di sviluppare ulteriormente i servizi quando le condizioni lo renderanno conveniente, tenendo conto dei costi dell’offerta aggiuntiva.',
'<strong>Opzione di sviluppo.</strong> Lo scenario assume un cadenzamento alla mezz’ora, un aumento del 27% della mobilità sistematica e del 10% della componente turistica. La maggiore frequenza rende il treno utilizzabile in più fasce orarie e può favorire il trasferimento dalla strada. L’opzione ha durata di cinque anni e tasso del 3%.',
'<strong>Opzione di integrazione.</strong> Un migliore coordinamento degli orari a Udine e servizi estesi oltre la sola tratta possono rendere più accessibili le connessioni con la rete nazionale. Il report rileva che, nell’orario 2024 analizzato, solo l’11% dei servizi in arrivo a Udine consentiva una coincidenza per Cividale. Lo scenario ipotizza fino a circa 500.000 passeggeri annui, con volatilità del 10% e durata di cinque anni.'
)+chart('udine-opzioni',2,'Il valore delle due opportunità','Le opzioni di sviluppo e integrazione totalizzano 6,09 mln €.',
['Sviluppo','Integrazione'],[3.89,2.20],'mln €',2,source('udine','Studio Udine–Cividale, § 5'))+
table('Valori e sensibilità delle opzioni',['Opzione','Caso base','Intervallo negli scenari analizzati'],[
['Sviluppo','3,89 mln €','1,86–6,02 mln €'],['Integrazione','2,20 mln €','1,18–3,44 mln €'],['Totale dei casi base','6,09 mln €','Non è riportato un intervallo congiunto']
],source('udine','Studio Udine–Cividale, § 5'))+
prose('Gli intervalli esprimono la sensibilità ai parametri di domanda e volatilità, non probabilità di realizzazione. Le opzioni non sono servizi già attivati: il loro esercizio richiede programmazione, risorse e verifica della domanda.'),
'oe-section--grey')
body+=section('risultati','Risultati e implicazioni','Distinguere i benefici dal rendimento dell’investimento','L’analisi fornisce una misura del valore sociale e delle opportunità di sviluppo.',
table('Indicatori sintetici dello studio',['Indicatore','Valore','Interpretazione'],[
['Benefici complessivi','61,36 mln €','Somma nell’orizzonte di 30 anni'],
['Benefici attualizzati','37,58 mln €','Valore dei benefici scontato al 3%'],
['Opzioni reali','6,09 mln €','Valore delle due opportunità future']
],source('udine','Studio Udine–Cividale, sintesi esecutiva e § 6'))+
prose('Il risultato indica tre priorità gestionali: conseguire i tempi di percorrenza ipotizzati, completare la transizione tecnologica e programmare servizi capaci di utilizzare l’integrazione nella rete nazionale. La lettura economica mette in relazione queste scelte con i benefici per utenti e territorio.',
'I benefici nominali e quelli attualizzati rappresentano due letture dello stesso flusso e <strong>non vanno sommati</strong>. Le opzioni descrivono ulteriori opportunità secondo il modello. Per esprimere un giudizio di redditività complessiva occorrerebbe confrontare tutti i benefici con l’intero profilo dei costi: i soli valori di beneficio non forniscono tale indicatore.'))
body+=downloads('udine')
save('report-udine-cividale.html',body,[('razionale','Razionale'),('benefici','Benefici'),('opzioni','Opzioni reali'),('risultati','Risultati')])
print('Quattro report HTML aggiornati.')
