(function () {
  'use strict';
  async function render() {
    var data = document.getElementById('report-chart-data');
    if (!data || typeof OE === 'undefined' || typeof Chart === 'undefined') return;
    if (document.fonts && document.fonts.ready) await document.fonts.ready;
    OE.defaults();
    JSON.parse(data.textContent).forEach(function (item) {
      var canvas = document.getElementById(item.id);
      if (!canvas) return;
      var box = canvas.closest('.oe-figure__chart');
      box.hidden = false;
      var opts = {unita:item.unit,dec:item.dec};
      if (item.signed) opts.colori = item.values.map(function(v){return v < 0 ? OE.colori.grey : OE.colori.b700;});
      try {
        OE[item.kind](item.id, item.labels, item.values, opts);
        canvas.closest('figure').querySelector('.chart-fallback').hidden = true;
      } catch (error) {
        box.hidden = true;
        console.error('Grafico non disponibile: ' + item.id, error);
      }
    });
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', render);
  else render();
})();
