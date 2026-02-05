from flask import Flask, render_template, request, jsonify
import json
import os

app = Flask(__name__)
DATA_FILE = 'alumnos.json'

# Inicializar archivo JSON si no existe
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'w') as f:
        json.dump([], f)

def leer_alumnos():
    with open(DATA_FILE, 'r') as f:
        return json.load(f)

def guardar_alumnos(alumnos):
    with open(DATA_FILE, 'w') as f:
        json.dump(alumnos, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/alumnos', methods=['GET'])
def obtener_alumnos():
    return jsonify(leer_alumnos())

@app.route('/api/alumnos', methods=['POST'])
def crear_alumno():
    if not request.is_json:
        return jsonify({'error': 'El cuerpo debe ser JSON'}), 400

    alumnos = leer_alumnos()
    print(alumnos)
    nuevo_alumno = request.json

    nombre = nuevo_alumno.get('nombre', '').strip()
    email = nuevo_alumno.get('email', '').strip()
    edad = nuevo_alumno.get('edad')

    if not nombre:
        return jsonify({'error': 'El nombre no puede estar vacío'}), 400

    if not email:
        return jsonify({'error': 'El email no puede estar vacío'}), 400

    if edad is None or edad < 0:
        return jsonify({'error': 'La edad no puede ser negativa'}), 400

    if any(a['email'] == email for a in alumnos):
        return jsonify({'error': 'Email ya registrado'}), 409

    nuevo_alumno['id'] = max([a['id'] for a in alumnos], default=0) + 1
    nuevo_alumno['nombre'] = nombre
    nuevo_alumno['email'] = email

    try:
        alumnos.append(nuevo_alumno)
        guardar_alumnos(alumnos)
    except Exception:
        return jsonify({'error': 'Error al guardar el alumno'}), 500

    return jsonify(nuevo_alumno), 201


@app.route('/api/alumnos/<int:id>', methods=['PUT'])
def actualizar_alumno(id):
    alumnos = leer_alumnos()
    for alumno in alumnos:
        if alumno['id'] == id:
            alumno.update(request.json)
            alumno['id'] = id
            guardar_alumnos(alumnos)
            return jsonify(alumno)
    return jsonify({'error': 'Alumno no encontrado'}), 404

@app.route('/api/alumnos/<int:id>', methods=['DELETE'])
def eliminar_alumno(id):
    alumnos = leer_alumnos()
    alumnos = [a for a in alumnos if a['id'] != id]
    guardar_alumnos(alumnos)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
