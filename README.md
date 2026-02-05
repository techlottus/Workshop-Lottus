# Sistema de gestión de alumnos
## Descripción del Proyecto

El Sistema de Gestión de Alumnos permite administrar información básica de estudiantes mediante operaciones CRUD. El objetivo principal de este repositorio no es solo el producto final, sino la forma en que se desarrolla, prueba y despliega siguiendo principios DevOps.

### Funcionalidades Core:
- Visualización de alumnos registrados
- Registro de nuevos alumnos
- Actualización de la información de un alumno
- Eliminación de un alumno

### Tecnologías Utilizadas
- Backend: Python 3.11, Flask 3.0
- Frontend: Vanilla JS, HTML, CSS

### Cómo iniciar
1. Clona el repositorio.
2. Navega al directorio del proyecto.
3. Crea un entorno virtual:
```sh
python -m venv .venv
# older versions
python3 -m venv .venv
```
Nota: `-m` indica que se está ejecutando un módulo como script. En este caso, `venv` es el módulo que crea entornos virtuales en Python.
4. Activa el entorno virtual:
```sh
# macOS/Linux
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```
5. Instala las dependencias:
```sh
pip install -r requirements.txt
```
6. Inicia la aplicación:
```sh
python app.py
```
7. Abre tu navegador y visita `http://localhost:5000` para ver la aplicación en funcionamiento.

## Cómo contribuir al proyecto
¡Las contribuciones son bienvenidas! Si deseas contribuir, te invitamos a conocer más a detalle el proyecto: [Como contribuir](./CONTRIBUTING.md)
