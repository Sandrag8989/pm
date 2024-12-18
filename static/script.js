// script.js
document.getElementById('contactForm').addEventListener('submit', function (e) {
    e.preventDefault(); // Evita el envío tradicional del formulario
    
    var formData = new FormData(this);
    
    fetch('/submit', {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        var responseMessage = document.getElementById('responseMessage');
        if (data.status === 'success') {
            responseMessage.innerHTML = `Gracias, ${data.name}! Hemos recibido tu mensaje: "${data.message}"`;
        } else {
            responseMessage.innerHTML = 'Hubo un error al enviar el mensaje.';
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
