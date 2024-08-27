document.addEventListener('DOMContentLoaded', function() {
    // Отримуємо всі радіо-кнопки
    const radioButtons = document.querySelectorAll('input[type="radio"]');

    // Додаємо обробник подій для кожної радіо-кнопки
    radioButtons.forEach(button => {
        button.addEventListener('change', function() {
            // Видаляємо активний стан з усіх label
            document.querySelectorAll('label').forEach(label => label.classList.remove('active'));

            // Додаємо активний стан до батьківського label вибраної радіо-кнопки
            if (this.checked) {
                this.parentElement.classList.add('active');
            }
        });
    });

    // Встановлюємо вибрану радіо-кнопку при завантаженні сторінки
    const defaultCheckedButton = document.querySelector('input[type="radio"][checked]');
    if (defaultCheckedButton) {
        defaultCheckedButton.parentElement.classList.add('active');
    }
});
