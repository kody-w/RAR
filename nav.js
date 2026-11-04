(() => {
  const nav = document.getElementById('rar-nav');
  if (!nav) return;

  const destinations = [
    ['Browse', 'index.html'],
    ['Distros', 'distros.html'],
    ['Skills', 'skills.html'],
    ['Install', 'install.html'],
    ['Front page', 'front.html'],
    ['Advanced', 'store.html'],
    ['For AIs', 'llms.txt'],
  ];
  const primary = nav.querySelector('.rar-primary');
  const root = nav.dataset.root || '';
  const currentPage = root ? '' : location.pathname.split('/').pop() || 'index.html';
  for (const [label, href] of destinations) {
    const link = document.createElement('a');
    link.textContent = label;
    link.setAttribute('href', root + href);
    if (href === currentPage) link.setAttribute('aria-current', 'page');
    primary.appendChild(link);
  }

  const more = nav.querySelector('.rar-more-content');
  for (const id of ['header-actions', 'user-area', 'refresh']) {
    const control = document.getElementById(id);
    if (control) more.appendChild(control);
  }
  const connection = document.querySelector('.rar-page-header .conn');
  if (connection) more.appendChild(connection);

  // Move the existing cart, keeping its handlers, badge and page-owned state.
  const cart = document.getElementById('cart-toggle');
  if (cart) {
    cart.setAttribute('role', 'button');
    cart.setAttribute('tabindex', '0');
    cart.setAttribute('aria-label', 'Agent Cart');
    cart.addEventListener('keydown', event => {
      if (event.key === 'Enter' || event.key === ' ') {
        event.preventDefault();
        cart.click();
      }
    });
    nav.appendChild(cart);
  }

  const updateHeight = () => {
    document.documentElement.style.setProperty('--rar-nav-height', `${nav.offsetHeight}px`);
  };
  updateHeight();
  new ResizeObserver(updateHeight).observe(nav);
})();
