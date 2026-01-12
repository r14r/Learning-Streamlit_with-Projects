document.addEventListener('DOMContentLoaded', () => {
  const tabContainers = document.querySelectorAll('[data-tabs]');
  tabContainers.forEach(container => {
    const buttons = container.querySelectorAll('.tab-btn');
    const panels = container.querySelectorAll('.tab-panel');
    if (!buttons.length) return;
    const activate = (index) => {
      buttons.forEach((btn, idx) => btn.classList.toggle('active', idx === index));
      panels.forEach((panel, idx) => panel.classList.toggle('active', idx === index));
    };
    buttons.forEach((btn, idx) => {
      btn.addEventListener('click', () => activate(idx));
    });
    activate(0);
  });

  if (window.AOS) {
    AOS.init({
      duration: 650,
      easing: 'ease-out-cubic',
      once: true,
    });
  }

  const navSearch = document.getElementById('nav-search');
  if (navSearch) {
    navSearch.addEventListener('input', (event) => {
      const query = event.target.value.toLowerCase().trim();
      const items = document.querySelectorAll('.nav li');
      items.forEach((item) => {
        const text = item.textContent.toLowerCase();
        const matches = !query || text.includes(query);
        item.style.display = matches ? '' : 'none';
      });
    });
  }
});
