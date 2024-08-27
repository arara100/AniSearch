document.querySelectorAll('.filter-title').forEach(title => {
    title.addEventListener('click', function() {
        // Знайти відповідний блок для анімації
        const group = this.parentElement;

        // Переключити клас "show" для поточного блоку
        group.classList.toggle('show');
    });
});
