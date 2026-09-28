/* =========================================================================
   OE — preset Chart.js con i colori e il formato numerico del brand
   Richiede Chart.js 4.x caricato prima di questo file.
   Convenzione colori (non negoziabile): serie SEMPRE su rampa Bluette,
   categoria principale = viola piu scuro, residuo/aggregato = grigio.
   Il lime e colore di UI (chip, accenti), MAI colore di serie.
   Le chiavi bNNN corrispondono ai token --oe-bluette-NNN.
   ========================================================================= */
(function (global) {
  'use strict';

  var C = {
    b900: '#270065', // principale / diretto / territorio dell'intervento
    b800: '#340088',
    b700: '#4400B3', // seconda categoria
    b500: '#6E1AFF', // indiretto / spillover
    b300: '#A16AFF', // indotto
    b200: '#B991FF',
    b100: '#D9C1FF',
    b050: '#EFE5FF', // solo fondi, mai come serie
    grey: '#AFAFAF', // residuo: "Resto d'Italia", "Other EU", "Altro"
    greyLight: '#E7E7E7',
    ink: '#000000',
    text: '#545454',
    white: '#FFFFFF'
  };

  // rampe pronte all'uso
  var RAMPS = {
    componenti: [C.b700, C.b500, C.b300],        // diretto / indiretto / indotto
    fasi: [C.b700, C.b300],                      // CAPEX / OPEX
    territori: [C.b900, C.b500, C.b200, C.grey], // area / spillover / resto regione / resto Paese
    scala5: [C.b900, C.b700, C.b500, C.b300, C.b200]
  };

  // n colori: rampa viola dal piu scuro, ultimo grigio se residuo = true
  function serie(n, residuo) {
    var base = [C.b900, C.b700, C.b500, C.b300, C.b200, C.b100];
    var out = [];
    var k = residuo ? n - 1 : n;
    for (var i = 0; i < k; i++) out.push(base[Math.min(i, base.length - 1)]);
    if (residuo) out.push(C.grey);
    return out;
  }

  // ---- numeri in italiano: migliaia ".", decimale "," -------------------
  // useGrouping 'always': con 'it-IT' e true i numeri a 4 cifre (2072)
  // non verrebbero raggruppati. Lingua diversa: OE.lingua = 'en-GB'.
  function nf(dec) {
    return new Intl.NumberFormat(global.OE && global.OE.lingua || 'it-IT', {
      minimumFractionDigits: dec, maximumFractionDigits: dec, useGrouping: 'always'
    });
  }
  function fmt(v, dec, unita) {
    var s = nf(dec == null ? 2 : dec).format(v);
    return unita ? s + ' ' + unita : s;
  }
  function pct(v, dec) { return nf(dec == null ? 1 : dec).format(v) + '%'; }

  var FONT = (function () {
    var f = getComputedStyle(document.documentElement).getPropertyValue('--oe-font-sans').trim();
    return f || 'Atkinson Hyperlegible Next, system-ui, sans-serif';
  })();

  function defaults() {
    if (typeof Chart === 'undefined') return;
    Chart.defaults.locale = global.OE && global.OE.lingua || 'it-IT'; // tick degli assi
    Chart.defaults.font.family = FONT;
    Chart.defaults.font.size = 12;
    Chart.defaults.color = C.text;
    Chart.defaults.plugins.legend.labels.usePointStyle = true;
    Chart.defaults.plugins.legend.labels.pointStyle = 'circle';
    Chart.defaults.plugins.legend.labels.boxWidth = 12;
    Chart.defaults.plugins.legend.labels.padding = 14;
    Chart.defaults.plugins.tooltip.backgroundColor = C.b900;
    Chart.defaults.plugins.tooltip.padding = 10;
    Chart.defaults.plugins.tooltip.cornerRadius = 0;
    Chart.defaults.maintainAspectRatio = false;
  }

  function grid() { return { color: 'rgba(0,0,0,.06)', drawTicks: false }; }

  // Un canvas e invisibile agli screen reader: gli si da role="img" e,
  // se manca, un aria-label (opt.descrizione o il titolo della figura).
  function el2ctx(el, opt) {
    var n = typeof el === 'string' ? document.getElementById(el) : el;
    if (!n) return null;
    if (!n.hasAttribute('role')) n.setAttribute('role', 'img');
    if (!n.hasAttribute('aria-label')) {
      var fig = n.closest && n.closest('.oe-figure');
      var t = fig && fig.querySelector('.oe-figure__title');
      var label = (opt && opt.descrizione) || (t && t.textContent.trim());
      if (label) n.setAttribute('aria-label', label);
    }
    return n.getContext('2d');
  }

  // ---- ciambella composizione (benefici SROI, composizione spesa) -------
  function doughnut(el, labels, dati, opt) {
    opt = opt || {};
    var ctx = el2ctx(el, opt);
    if (!ctx) return null;
    return new Chart(ctx, {
      type: 'doughnut',
      data: {
        labels: labels,
        datasets: [{
          data: dati,
          backgroundColor: opt.colori || serie(dati.length, opt.residuo),
          borderColor: C.white, borderWidth: 3, hoverOffset: 10
        }]
      },
      options: {
        cutout: '58%',
        plugins: {
          legend: { position: opt.legenda || 'bottom' },
          tooltip: {
            callbacks: {
              label: function (c) {
                var tot = c.dataset.data.reduce(function (a, b) { return a + b; }, 0);
                return ' ' + c.label + ': ' + fmt(c.parsed, opt.dec == null ? 2 : opt.dec, opt.unita) +
                  ' (' + pct(c.parsed / tot * 100) + ')';
              }
            }
          }
        }
      }
    });
  }

  // ---- barre impilate per componente (diretto/indiretto/indotto) --------
  function componenti(el, categorie, serieDati, opt) {
    opt = opt || {};
    var ctx = el2ctx(el, opt);
    if (!ctx) return null;
    var nomi = opt.nomi || ['Diretto', 'Indiretto', 'Indotto'];
    var orizz = !!opt.orizzontale;
    return new Chart(ctx, {
      type: 'bar',
      data: {
        labels: categorie,
        datasets: serieDati.map(function (d, i) {
          return {
            label: nomi[i], data: d,
            backgroundColor: (opt.colori || RAMPS.componenti)[i],
            borderWidth: 0, barPercentage: 0.7, categoryPercentage: 0.7
          };
        })
      },
      options: {
        indexAxis: orizz ? 'y' : 'x',
        plugins: {
          legend: { position: 'bottom' },
          tooltip: {
            callbacks: {
              label: function (c) {
                return ' ' + c.dataset.label + ': ' + fmt(orizz ? c.parsed.x : c.parsed.y, opt.dec, opt.unita);
              }
            }
          }
        },
        scales: {
          x: { stacked: true, grid: orizz ? grid() : { display: false } },
          y: { stacked: true, grid: orizz ? { display: false } : grid() }
        }
      }
    });
  }

  // ---- graduatoria orizzontale (settori, territori) ---------------------
  function graduatoria(el, labels, dati, opt) {
    opt = opt || {};
    var ctx = el2ctx(el, opt);
    if (!ctx) return null;
    return new Chart(ctx, {
      type: 'bar',
      data: {
        labels: labels,
        datasets: [{
          data: dati,
          backgroundColor: opt.colori || serie(dati.length, opt.residuo),
          borderWidth: 0, barPercentage: 0.78, categoryPercentage: 0.78
        }]
      },
      options: {
        indexAxis: 'y',
        plugins: {
          legend: { display: false },
          tooltip: { callbacks: { label: function (c) { return ' ' + fmt(c.parsed.x, opt.dec, opt.unita); } } }
        },
        scales: {
          x: { grid: grid() },
          y: { grid: { display: false } }
        }
      }
    });
  }

  // ---- waterfall benefici -> costo -> valore netto (SROI / ACB) ---------
  // voci: [{label: '...', valore: 5.00, tipo: 'positivo' | 'negativo' | 'totale'}]
  function waterfall(el, voci, opt) {
    opt = opt || {};
    var ctx = el2ctx(el, opt);
    if (!ctx) return null;
    var base = [], vis = [], col = [], cum = 0;
    voci.forEach(function (v) {
      if (v.tipo === 'totale') { base.push(0); vis.push(v.valore); col.push(C.b900); }
      else if (v.tipo === 'negativo') { cum -= Math.abs(v.valore); base.push(cum); vis.push(Math.abs(v.valore)); col.push(C.grey); }
      else { base.push(cum); vis.push(v.valore); col.push(C.b700); cum += v.valore; }
    });
    return new Chart(ctx, {
      type: 'bar',
      data: {
        labels: voci.map(function (v) { return v.label; }),
        datasets: [
          { data: base, backgroundColor: 'rgba(0,0,0,0)', stack: 'w', borderWidth: 0 },
          { data: vis, backgroundColor: col, stack: 'w', borderWidth: 0, barPercentage: 0.62, categoryPercentage: 0.62 }
        ]
      },
      options: {
        plugins: {
          legend: { display: false },
          tooltip: {
            filter: function (c) { return c.datasetIndex === 1; },
            callbacks: { label: function (c) { return ' ' + fmt(c.parsed.y, opt.dec, opt.unita); } }
          }
        },
        scales: {
          x: { stacked: true, grid: { display: false }, ticks: { maxRotation: 0, font: { weight: '600' } } },
          y: { stacked: true, beginAtZero: true, grid: grid() }
        }
      }
    });
  }

  // ---- flusso economico attualizzato + cumulato (ACB) ------------------
  function flussiACB(el, anni, netto, cumulato, opt) {
    opt = opt || {};
    var ctx = el2ctx(el, opt);
    if (!ctx) return null;
    return new Chart(ctx, {
      data: {
        labels: anni,
        datasets: [
          {
            type: 'bar', label: 'Flusso netto attualizzato', data: netto,
            backgroundColor: netto.map(function (v) { return v >= 0 ? C.b500 : C.grey; }),
            borderWidth: 0, order: 2
          },
          {
            type: 'line', label: 'Cumulato (VANE progressivo)', data: cumulato,
            borderColor: C.b900, backgroundColor: C.b900, borderWidth: 2,
            pointRadius: 0, tension: 0.25, order: 1
          }
        ]
      },
      options: {
        plugins: {
          legend: { position: 'bottom' },
          tooltip: { callbacks: { label: function (c) { return ' ' + c.dataset.label + ': ' + fmt(c.parsed.y, opt.dec, opt.unita); } } }
        },
        scales: {
          x: { grid: { display: false } },
          y: { grid: grid() }
        }
      }
    });
  }

  global.OE = {
    colori: C, rampe: RAMPS, serie: serie,
    fmt: fmt, pct: pct, nf: nf,
    defaults: defaults,
    doughnut: doughnut, componenti: componenti, graduatoria: graduatoria,
    waterfall: waterfall, flussiACB: flussiACB
  };

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', defaults);
  else defaults();
})(window);
