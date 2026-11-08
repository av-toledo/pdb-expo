// ===== PDB Expo — nav interactions =====
(function () {
  var hamburger = document.getElementById('hamburger');
  var navLinks  = document.getElementById('navLinks');

  if (hamburger && navLinks) {
    hamburger.addEventListener('click', function () {
      var open = navLinks.classList.toggle('open');
      hamburger.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // On mobile, tapping a dropdown parent expands it instead of navigating.
  var menus = document.querySelectorAll('.has-menu > .navlink');
  menus.forEach(function (label) {
    label.addEventListener('click', function (e) {
      if (window.matchMedia('(max-width: 760px)').matches) {
        e.preventDefault();
        label.parentElement.classList.toggle('open');
      }
    });
  });

  // Close mobile menu after choosing a link.
  navLinks && navLinks.querySelectorAll('a').forEach(function (a) {
    a.addEventListener('click', function () {
      navLinks.classList.remove('open');
      hamburger && hamburger.setAttribute('aria-expanded', 'false');
    });
  });

  // Visual-only forms (no backend yet): show a confirmation, disable inputs.
  document.querySelectorAll('form[data-demo]').forEach(function (f) {
    f.addEventListener('submit', function (e) {
      e.preventDefault();
      var note = f.querySelector('.form-note');
      if (note) { note.hidden = false; }
      f.querySelectorAll('input, select, textarea, button').forEach(function (el) {
        el.disabled = true;
      });
    });
  });
})();
