console.log("Debt Pro Calculator ready");

document.querySelectorAll('a').forEach(link => {
  link.addEventListener('click', () => {
    if (link.href.includes('TU_LINK_AFILIADO')) {
      console.log('Click afiliado');
      // opcional: enviar evento a GA
    }
  });
});