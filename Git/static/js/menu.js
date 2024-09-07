$(document).ready(function() {
  // Manejar clic en el botón del menú
  $('.menu-btn').click(function() {
    $('.sidebar').toggleClass('active');
    $('.main-content').toggleClass('active');
  });

  // Manejar clic en los enlaces de menú y submenú
  $('.menu > ul > li > a').click(function (e) {
    // Si el enlace tiene un `data-content`, muestra el contenido
    var contentId = $(this).data('content');
    if (contentId) {
      $('.content-section').removeClass('active');
      $('#' + contentId).addClass('active');
    }

    // Manejo de la visibilidad de los sub-menús
    $(this).parent().siblings().removeClass("active");
    $(this).parent().siblings().find("ul").slideUp(); // Oculta otros sub-menús
    $(this).parent().toggleClass("active");
    $(this).parent().find("ul").slideToggle(); // Muestra u oculta el sub-menú

    $(this).parent().siblings().find("ul").find("li").removeClass("active");
  });

  // Manejar el clic en los enlaces del navbar
  $('.navbar-links a').click(function (e) {
    // Quita el comportamiento por defecto
    // e.preventDefault(); // Eliminar esta línea para permitir navegación de enlaces

    // Si el enlace tiene un href con una id de contenido
    var contentId = $(this).attr('href').substring(1); // Quita el `#` para obtener el id
    if (contentId) {
      $('.content-section').removeClass('active');
      $('#' + contentId).addClass('active');

      // Manejo de la visibilidad de los sub-menús en el sidebar
      $('.menu > ul > li').removeClass('active');
      $('.menu .sub-menu').slideUp(); // Oculta todos los sub-menús
    }
  });

  // Mostrar el contenido de inicio por defecto
  $('#home').addClass('active');
  
  let currentFontSize = 100; // Tamaño base de fuente

  // Aumentar tamaño de letra
  document.getElementById('increaseFontBtn').addEventListener('click', function() {
      if (currentFontSize < 150) {
          currentFontSize += 10;
          document.body.style.fontSize = currentFontSize + '%';
      }
  });
  
  // Disminuir tamaño de letra
  document.getElementById('decreaseFontBtn').addEventListener('click', function() {
      if (currentFontSize > 50) {
          currentFontSize -= 10;
          document.body.style.fontSize = currentFontSize + '%';
      }
  });
  
  let currentZoom = 1;
  
  // Zoom in
  document.getElementById('zoomInBtn').addEventListener('click', function() {
      if (currentZoom < 2) {
          currentZoom += 0.1;
          document.body.style.transform = `scale(${currentZoom})`;
          document.body.style.transformOrigin = '0 0'; // Fija el origen para evitar desplazamientos
      }
  });
  
  // Zoom out
  document.getElementById('zoomOutBtn').addEventListener('click', function() {
      if (currentZoom > 1) {
          currentZoom -= 0.1;
          document.body.style.transform = `scale(${currentZoom})`;
          document.body.style.transformOrigin = '0 0'; // Fija el origen para evitar desplazamientos
      }
  });
  
  let speech = null;
  
  // Activar lector de voz
  document.getElementById('readerBtn').addEventListener('click', function() {
      const textToRead = document.body.innerText;
      speech = new SpeechSynthesisUtterance(textToRead);
      window.speechSynthesis.speak(speech);
  });
  
  // Detener lector de voz
  document.getElementById('stopReaderBtn').addEventListener('click', function() {
      if (speech) {
          window.speechSynthesis.cancel(); // Detiene cualquier voz en curso
      }
  });
  
});
