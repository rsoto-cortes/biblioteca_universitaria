# Biblioteca Universitaria

Aplicación web desarrollada con **Flask** que presenta información de una biblioteca universitaria mediante varias páginas enlazadas.

## Elementos implementados

### Aplicación y rutas

El archivo `server.py` crea la aplicación Flask y define las rutas disponibles:

La ruta con `/` nos lleva a Inicio la cual es la presentación de la biblioteca, propósito y horario de atención. 

La ruta con `/catalogo`  nos lleva a Catálogo la cual nos presenta las categorías de materiales disponibles y una breve descripción. 

La ruta con `/servicios` nos lleva a Servicios la cual muestra los servicios de la biblioteca y explicación de cada uno. 

La ruta con `/contacto`  nos lleva a Contacto la cual muesta la ubicación, teléfono, correo electrónico y horario de atención.

Cada ruta renderiza su plantilla y le pasa un título y un mensaje de bienvenida.

### Plantillas HTML

Las plantillas están en la carpeta `templates/`:

- **`layout.html`**: estructura HTML compartida, título dinámico y pestañas de navegación que enlazan con las cuatro páginas y resaltan la página actual. También carga Bootstrap 4.6.2 desde un CDN.
- **`index.html`**: página de inicio de la Biblioteca Universitaria, con su propósito y horario.
- **`catalogo.html`**: enumera libros, revistas, periódicos, artículos y tesis.
- **`servicios.html`**: describe el préstamo de libros, la consulta en sala, el acceso a recursos electrónicos y el asesoramiento en investigación.
- **`contacto.html`**: muestra la ubicación de la biblioteca y sus medios de contacto.

Las páginas de contenido extienden `layout.html` y colocan su contenido en el bloque `content`. Las variables `title` y `message` se insertan con expresiones de Jinja2.

### Dependencias

`requirements.txt` especifica las dependencias de Python. La aplicación utiliza Flask; sus paquetes relacionados, como Jinja2 y Werkzeug, también aparecen en la lista.
