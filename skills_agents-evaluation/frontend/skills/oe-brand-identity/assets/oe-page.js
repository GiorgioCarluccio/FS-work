/* =========================================================================
   OE — comportamenti di pagina (senza dipendenze)
   1. Menu mobile: il bottone .nav__toggle apre/chiude .nav__links.
   2. Scroll-spy: la voce di nav il cui href="#id" corrisponde alla sezione
      visibile riceve .nav-active e aria-current="true".
   Lo scorrimento morbido e l'offset sotto la nav sono gestiti in CSS
   (scroll-behavior + scroll-padding-top in oe-base.css): i link restano
   normali <a href="#id">, quindi funzionano anche senza JS e da tastiera.
   ========================================================================= */
(function () {
  'use strict';

  function init() {
    var nav = document.querySelector('.nav');
    if (!nav) return;
    var toggle = nav.querySelector('.nav__toggle');
    var list = nav.querySelector('.nav__links');
    var links = list ? [].slice.call(list.querySelectorAll('a[href^="#"]')) : [];

    // ---- 1. menu mobile ---------------------------------------------------
    function setOpen(open) {
      nav.classList.toggle('is-open', open);
      if (toggle) {
        toggle.setAttribute('aria-expanded', String(open));
        toggle.setAttribute('aria-label', open ? 'Chiudi il menu' : 'Apri il menu');
      }
    }
    if (toggle && list) {
      if (!list.id) list.id = 'oe-nav-links';
      toggle.setAttribute('aria-controls', list.id);
      setOpen(false);
      toggle.addEventListener('click', function () {
        setOpen(!nav.classList.contains('is-open'));
      });
      list.addEventListener('click', function (e) {
        if (e.target.closest('a')) setOpen(false);
      });
      document.addEventListener('keydown', function (e) {
        if (e.key === 'Escape' && nav.classList.contains('is-open')) {
          setOpen(false);
          toggle.focus();
        }
      });
    }

    // ---- 2. scroll-spy ----------------------------------------------------
    if (!links.length || !('IntersectionObserver' in window)) return;
    var byId = {};
    links.forEach(function (a) {
      var id = decodeURIComponent(a.hash.slice(1));
      var sec = id && document.getElementById(id);
      if (sec) byId[id] = { a: a, sec: sec };
    });
    function setActive(a) {
      links.forEach(function (l) {
        l.classList.remove('nav-active');
        l.removeAttribute('aria-current');
      });
      if (a) {
        a.classList.add('nav-active');
        a.setAttribute('aria-current', 'true');
      }
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting && byId[e.target.id]) setActive(byId[e.target.id].a);
      });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });
    Object.keys(byId).forEach(function (id) { io.observe(byId[id].sec); });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
})();
