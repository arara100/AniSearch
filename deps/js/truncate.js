function truncateTextByClass(className, maxLength) {
    // Отримуємо всі елементи з вказаним класом
    var elements = document.getElementsByClassName(className);
    
    // Перебираємо всі елементи і обрізаємо текст
    for (var i = 0; i < elements.length; i++) {
      var element = elements[i];
      var text = element.innerText;
      if (text.length > maxLength) {
        element.innerText = text.slice(0, maxLength) + '...';
      }
    }
  }
  
  // Викликаємо функцію після завантаження контенту
  document.addEventListener('DOMContentLoaded', function() {
    truncateTextByClass('content-text', 10); // Обрізає текст до 20 символів
  });
  