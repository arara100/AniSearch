document.addEventListener('DOMContentLoaded', function() {
    const container = document.getElementById('anime-container');
    const radios = document.querySelectorAll('input[name="sort"]');

    function fetchAnimeData(sortBy) {
        fetch(`/anime?sort=${sortBy}`)
            .then(response => response.json())
            .then(data => {
                // Очищення контейнера
                container.innerHTML = '';

                // Додавання нових даних
                data.data.forEach(anime => {
                    const item = document.createElement('div');
                    item.className = 'anime-item';
                    item.innerHTML = `
                        <h3>${anime.title}</h3>
                        <img src="${anime.image_url}" alt="${anime.title}">
                    `;
                    container.appendChild(item);
                });
            })
            .catch(error => console.error('Error fetching data:', error));
    }

    // Завантаження даних при завантаженні сторінки
    fetchAnimeData('rating');

    // Обробка змін вибору радіокнопок
    radios.forEach(radio => {
        radio.addEventListener('change', function() {
            fetchAnimeData(this.value);
        });
    });
});
