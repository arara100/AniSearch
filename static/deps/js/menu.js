document.addEventListener('DOMContentLoaded', function() {
    const menu = document.querySelector('.side-menu');
    const menuIcon = document.querySelector('.list');

    menuIcon.addEventListener('click', function() {
        menu.classList.toggle('active');
        menuIcon.classList.toggle('active');
    });

    document.addEventListener('click', function(event) {
        if (!menu.contains(event.target) && !menuIcon.contains(event.target) && menu.classList.contains('active')) {
            menu.classList.remove('active');
            menuIcon.classList.remove('active');
        }
    });
});
