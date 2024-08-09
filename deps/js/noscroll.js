const sideMenu = document.querySelector('.side-menu');
const menuButton = document.querySelector('.list');

function toggleMenu() {
  const body = document.body;

  if (sideMenu.style.left === '0px') {
    sideMenu.style.left = '-250px';
    body.classList.remove('no-scroll');
  } else {
    sideMenu.style.left = '0px';
    body.classList.add('no-scroll');
  }
}

menuButton.addEventListener('click', toggleMenu);
