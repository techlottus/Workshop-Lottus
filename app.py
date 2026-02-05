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
    alumnos = leer_alumnos()
    nuevo_alumno = request.json
    nuevo_alumno['id'] = len(alumnos) + 1
    alumnos.append(nuevo_alumno)
    guardar_alumnos(alumnos)
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
