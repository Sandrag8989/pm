from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Ruta para la página principal (GET)
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para manejar solicitudes POST
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        # Obtener los datos del formulario
        name = request.form.get('name')
        message = request.form.get('message')
        
        # Puedes hacer algo con estos datos, como guardarlos en una base de datos
        print(f'Nombre: {name}, Mensaje: {message}')
        
        # Enviar una respuesta en formato JSON
        return jsonify({'status': 'success', 'name': name, 'message': message})

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000)
    