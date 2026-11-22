(function () {
  var doc = document.documentElement;
  doc.classList.add('js');

  // Reveal on scroll
  var items = document.querySelectorAll('.reveal');
  if ('IntersectionObserver' in window) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12, rootMargin: '0px 0px -40px 0px' });
    items.forEach(function (el, i) {
      el.style.transitionDelay = (el.closest('.hero') ? i * 90 : 0) + 'ms';
      io.observe(el);
    });
  } else {
    items.forEach(function (el) { el.classList.add('in'); });
  }

  // Top bar + floating WhatsApp
  var bar = document.querySelector('.topbar');
  var wa = document.querySelector('.wa-float');
  var contact = document.querySelector('.contact');
  function onScroll() {
    var y = window.scrollY;
    bar.classList.toggle('scrolled', y > 20);
    var nearContact = contact && contact.getBoundingClientRect().top < window.innerHeight * 0.8;
    wa.classList.toggle('show', y > window.innerHeight * 0.6 && !nearContact);
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();

  // Active nav link
  var links = document.querySelectorAll('.nav a');
  if ('IntersectionObserver' in window) {
    var secObs = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) {
          links.forEach(function (a) { a.classList.toggle('active', a.getAttribute('href') === '#' + e.target.id); });
        }
      });
    }, { rootMargin: '-45% 0px -50% 0px' });
    document.querySelectorAll('main section[id]').forEach(function (s) { secObs.observe(s); });
  }

  // Copy buttons
  document.querySelectorAll('.copy').forEach(function (btn) {
    var label = btn.textContent;
    btn.addEventListener('click', function () {
      var text = btn.getAttribute('data-copy');
      var done = function () {
        btn.textContent = btn.getAttribute('data-done');
        btn.classList.add('done');
        setTimeout(function () { btn.textContent = label; btn.classList.remove('done'); }, 1800);
      };
      if (navigator.clipboard) { navigator.clipboard.writeText(text).then(done, function () {}); }
    });
  });

  // Contact form -> mailto / WhatsApp
  var form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (ev) {
      ev.preventDefault();
      var via = (ev.submitter && ev.submitter.value) || 'mail';
      var name = form.name.value.trim();
      var email = form.email.value.trim();
      var msg = form.message.value.trim();
      var body = msg + '\n\n— ' + name + (email ? ' (' + email + ')' : '');
      if (via === 'wa') {
        window.open('https://wa.me/' + form.dataset.wa + '?text=' + encodeURIComponent(body), '_blank', 'noopener');
      } else {
        window.location.href = 'mailto:' + form.dataset.email +
          '?subject=' + encodeURIComponent(form.dataset.subject + ' — ' + name) +
          '&body=' + encodeURIComponent(body);
      }
    });
  }

  var y = document.getElementById('year');
  if (y) y.textContent = new Date().getFullYear();
})();
