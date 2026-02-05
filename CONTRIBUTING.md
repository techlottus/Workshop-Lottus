# Como contribuir al proyecto

¡Gracias por tu interés en contribuir al Sistema de Gestión de Alumnos! Apreciamos cualquier aporte que puedas hacer para mejorar este proyecto. A continuación, encontrarás una guía paso a paso sobre cómo puedes contribuir de manera efectiva.

## Detalles del proyecto
### Visualización de alumnos registrados
Permite consultar el listado de todos los alumnos registrados en el sistema.
La información se presenta de forma clara y ordenada, facilitando la búsqueda y revisión de datos como nombre, matrícula, correo electrónico y estatus.
 
### Registro de nuevos alumnos
Permite agregar nuevos alumnos al sistema mediante un formulario de captura.
El sistema valida la información ingresada para garantizar la integridad de los datos antes de almacenarlos.
 
### Actualización de la información del alumno
Permite modificar los datos de un alumno previamente registrado.
Esta funcionalidad asegura que la información se mantenga actualizada ante cambios académicos o administrativos.
 
### Eliminación de un alumno
Permite eliminar un alumno del sistema de forma controlada.
Incluye mecanismos de confirmación para evitar eliminaciones accidentales y preservar la consistencia de la información.

## Pasos para contribuir:
1. **Fork del repositorio**: Haz un clon de este repositorio para tener tu propia copia del proyecto.
2. **Crea una rama para tu contribución**: Navega al directorio del proyecto y crea una nueva rama para tu contribución:
```sh
git checkout -b type/ticket-id-description
```
3. **Realiza tus cambios**: Implementa las mejoras, correcciones o nuevas funcionalidades que desees aportar.
4. **Prueba tus cambios**: Asegúrate de que tus modificaciones no rompan la funcionalidad existente y que todo funciona correctamente.
5. **Commit de tus cambios**: Realiza un commit de tus cambios con un mensaje claro y descriptivo:
```sh
git add .
git commit -m "feat: an important description"
```
6. **Push de tu rama**: Sube tus cambios.
7. **Abre un Pull Request**: Ve al repositorio en GitHub y abre un Pull Request. Describe detalladamente los cambios realizados y el motivo de los mismos.

## API endpoints
| Método	| Endpoint |	Descripción
| -------- | -------- | -------- |
| GET	| / |	Carga la interfaz principal (index.html).
| GET	| /api/alumnos |	Obtiene la lista completa de alumnos.
| POST	| /api/alumnos |	Crea un nuevo alumno.
| PUT	| /api/alumnos/<id> |	Actualiza los datos de un alumno existente.
| DELETE	| /api/alumnos/<id> |	Elimina un alumno del registro.
