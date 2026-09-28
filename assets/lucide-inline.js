/* Sottoinsieme di Lucide (ISC) inline, senza CDN. <i data-lucide="nome"></i>
   diventa un <svg> monoline (stroke 1.5, currentColor). Decorativa di default
   (aria-hidden); con aria-label diventa role="img". Elenco nomi: references/componenti.md */
(function(){
  var icons = {
    "menu":"<line x1='4' x2='20' y1='6' y2='6'/><line x1='4' x2='20' y1='12' y2='12'/><line x1='4' x2='20' y1='18' y2='18'/>",
    "x":"<path d='M18 6 6 18'/><path d='m6 6 12 12'/>",
    "check":"<path d='M20 6 9 17l-5-5'/>",
    "chevron-right":"<path d='m9 18 6-6-6-6'/>",
    "external-link":"<path d='M15 3h6v6'/><path d='M10 14 21 3'/><path d='M18 13v6a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h6'/>",
    "mail":"<rect width='20' height='16' x='2' y='4' rx='2'/><path d='m22 7-8.97 5.7a1.94 1.94 0 0 1-2.06 0L2 7'/>",
    "file-text":"<path d='M15 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7Z'/><path d='M14 2v4a2 2 0 0 0 2 2h4'/><path d='M10 9H8'/><path d='M16 13H8'/><path d='M16 17H8'/>",
    "search":"<circle cx='11' cy='11' r='8'/><path d='m21 21-4.3-4.3'/>",
    "calendar":"<rect width='18' height='18' x='3' y='4' rx='2'/><path d='M16 2v4'/><path d='M8 2v4'/><path d='M3 10h18'/>",
    "info":"<circle cx='12' cy='12' r='10'/><path d='M12 16v-4'/><path d='M12 8h.01'/>",
    "log-in":"<path d='M15 3h4a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2h-4'/><polyline points='10 17 15 12 10 7'/><line x1='15' x2='3' y1='12' y2='12'/>",
    "alert-circle":"<circle cx='12' cy='12' r='10'/><line x1='12' y1='8' x2='12' y2='12'/><line x1='12' y1='16' x2='12.01' y2='16'/>",
    "bar-chart-2":"<line x1='18' y1='20' x2='18' y2='10'/><line x1='12' y1='20' x2='12' y2='4'/><line x1='6' y1='20' x2='6' y2='14'/>",
    "bar-chart":"<line x1='12' y1='20' x2='12' y2='10'/><line x1='18' y1='20' x2='18' y2='4'/><line x1='6' y1='20' x2='6' y2='16'/>",
    "factory":"<path d='M2 20a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V8l-7 5V8l-7 5V4a2 2 0 0 0-2-2H4a2 2 0 0 0-2 2Z'/><path d='M17 18h1'/><path d='M12 18h1'/><path d='M7 18h1'/>",
    "globe":"<circle cx='12' cy='12' r='10'/><line x1='2' y1='12' x2='22' y2='12'/><path d='M12 2a15.3 15.3 0 0 1 4 10 15.3 15.3 0 0 1-4 10 15.3 15.3 0 0 1-4-10 15.3 15.3 0 0 1 4-10z'/>",
    "map":"<polygon points='1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6'/><line x1='8' y1='2' x2='8' y2='18'/><line x1='16' y1='6' x2='16' y2='22'/>",
    "pie-chart":"<path d='M21.21 15.89A10 10 0 1 1 8 2.83'/><path d='M22 12A10 10 0 0 0 12 2v10z'/>",
    "scatter-chart":"<circle cx='7.5' cy='7.5' r='1.5'/><circle cx='18.5' cy='5.5' r='1.5'/><circle cx='11.5' cy='11.5' r='1.5'/><circle cx='7.5' cy='16.5' r='1.5'/><circle cx='17.5' cy='14.5' r='1.5'/><circle cx='6.5' cy='20.5' r='1.5'/><circle cx='18.5' cy='20.5' r='1.5'/>",
    "trending-up":"<polyline points='23 6 13.5 15.5 8.5 10.5 1 18'/><polyline points='17 6 23 6 23 12'/>",
    "trending-down":"<polyline points='23 18 13.5 8.5 8.5 13.5 1 6'/><polyline points='17 18 23 18 23 12'/>",
    "users":"<path d='M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2'/><circle cx='9' cy='7' r='4'/><path d='M23 21v-2a4 4 0 0 0-3-3.87'/><path d='M16 3.13a4 4 0 0 1 0 7.75'/>",
    "zap":"<polygon points='13 2 3 14 12 14 11 22 21 10 12 10 13 2'/>",
    "shield":"<path d='M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z'/>",
    "anchor":"<circle cx='12' cy='5' r='3'/><line x1='12' y1='22' x2='12' y2='8'/><path d='M5 12H2a10 10 0 0 0 20 0h-3'/>",
    "flame":"<path d='M8.5 14.5A2.5 2.5 0 0 0 11 12c0-1.38-.5-2-1-3-1.072-2.143-.224-4.054 2-6 .5 2.5 2 4.9 4 6.5 2 1.6 3 3.5 3 5.5a7 7 0 1 1-14 0c0-1.153.433-2.294 1-3a2.5 2.5 0 0 0 2.5 2.5z'/>",
    "download":"<path d='M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4'/><polyline points='7 10 12 15 17 10'/><line x1='12' y1='15' x2='12' y2='3'/>",
    "minus-circle":"<circle cx='12' cy='12' r='10'/><line x1='8' y1='12' x2='16' y2='12'/>",
    "building":"<rect x='4' y='2' width='16' height='20' rx='0'/><path d='M9 22V12h6v10'/><path d='M8 7h.01M12 7h.01M16 7h.01M8 11h.01M12 11h.01M16 11h.01'/>",
    "landmark":"<line x1='3' y1='22' x2='21' y2='22'/><line x1='6' y1='18' x2='6' y2='11'/><line x1='10' y1='18' x2='10' y2='11'/><line x1='14' y1='18' x2='14' y2='11'/><line x1='18' y1='18' x2='18' y2='11'/><polygon points='12 2 20 7 4 7'/>",
    "coin":"<circle cx='12' cy='12' r='10'/><path d='M14.31 8l5.74 9.94M9.69 8h11.48M7.38 12l5.74-9.94M9.69 16 3.95 6.06M14.31 16H2.83M16.62 12 10.88 21.94'/>",
    "cpu":"<rect x='4' y='4' width='16' height='16' rx='0'/><rect x='9' y='9' width='6' height='6'/><path d='M15 2v2M9 2v2M15 20v2M9 20v2M2 15h2M2 9h2M20 15h2M20 9h2'/>",
    "heart-pulse":"<path d='M19 14c1.49-1.46 3-3.21 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.76 0-3 .5-4.5 2-1.5-1.5-2.74-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4.05 3 5.5l7 7Z'/><path d='M3.22 12H9.5l1.5-1.5 2 2.5 1.5-2 2 2.5 2-2.5h3.78'/>",
    "layers":"<path d='m12.83 2.18a2 2 0 0 0-1.66 0L2.6 6.08a1 1 0 0 0 0 1.83l8.58 3.91a2 2 0 0 0 1.66 0l8.58-3.9a1 1 0 0 0 0-1.83Z'/><path d='m22 17.65-9.17 4.16a2 2 0 0 1-1.66 0L2 17.65'/><path d='m22 12.65-9.17 4.16a2 2 0 0 1-1.66 0L2 12.65'/>",
    "home":"<path d='m3 9 9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z'/><polyline points='9 22 9 12 15 12 15 22'/>",
    "map-pin":"<path d='M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z'/><circle cx='12' cy='10' r='3'/>",
    "arrow-right":"<line x1='5' y1='12' x2='19' y2='12'/><polyline points='12 5 19 12 12 19'/>",
    "arrow-left":"<line x1='5' y1='12' x2='19' y2='12'/><polyline points='12 19 5 12 12 5'/>"
  };
  function createIcons(){
    document.querySelectorAll('[data-lucide]').forEach(function(el){
      var name=el.getAttribute('data-lucide'),paths=icons[name];
      if(!paths){if(window.console)console.warn('lucide-inline: icona "'+name+'" non presente nel bundle');return;}
      var svg=document.createElementNS('http://www.w3.org/2000/svg','svg');
      svg.setAttribute('xmlns','http://www.w3.org/2000/svg');
      svg.setAttribute('width','24');svg.setAttribute('height','24');
      svg.setAttribute('viewBox','0 0 24 24');svg.setAttribute('fill','none');
      svg.setAttribute('stroke','currentColor');svg.setAttribute('stroke-width','1.5');
      svg.setAttribute('stroke-linecap','round');svg.setAttribute('stroke-linejoin','round');
      svg.setAttribute('class','lucide lucide-'+name+(el.className?' '+el.className:''));
      var lbl=el.getAttribute('aria-label');if(lbl){svg.setAttribute('role','img');svg.setAttribute('aria-label',lbl);}else{svg.setAttribute('aria-hidden','true');}
      if(el.getAttribute('style'))svg.setAttribute('style',el.getAttribute('style'));
      svg.innerHTML=paths;el.parentNode.replaceChild(svg,el);
    });
  }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',createIcons);}
  else{createIcons();}
  window.lucide={createIcons:createIcons};
})();
