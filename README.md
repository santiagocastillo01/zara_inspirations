Zara Inspirations


Descripción:
Este es un proyecto de Django que permite a los usuarios buscar y explorar 
perfumes y sus inspiraciones. El proyecto incluye funcionalidades para listar 
perfumes, filtrar por nombre, y ver detalles específicos de cada perfume e inspiración.
(proximamente se agregara un CRUD para los productos.)


Requisitos:
- Python 3.11
- Django 5.0.6


Instalación:
1. Clona el repositorio a tu máquina local:
   git clone https://github.com/santiagocastillo01/zara_inspirations.git

2. Navega al directorio del proyecto:
   cd zains

3. Realiza las migraciones de la base de datos:
   python manage.py migrate

4. Ejecuta el servidor de desarrollo:
   python manage.py runserver


Informaciòn:
1. SuperUser para .../admin:
    USER : admin
    PASSWORD: 1111


Estructura del Proyecto:
- zar/: Contiene las vistas y URLs del proyecto.
- templates/zar/: Contiene las plantillas HTML.
- static/: Contiene los archivos estáticos, como CSS e imágenes.


Funcionalidades y Cómo Probarlas:
_#. Página de Inicio
   - URL: /
   - Contenido: Presenta la introducción al proyecto y enlaces a las categorías de inspiraciones y perfumes, con header funcional

_#. Categoría de Inspiraciones
   - URL: /categoria_inspiraciones/
   - Contenido: Muestra un html previo para elegir que inspiraciones buscar, de dama o caballero.

_#. Categoría de Perfumes
   - URL: /categoria_perfumes/
   - Contenido: Muestra un html previo para elegir que perfumes buscar, de dama o caballero.

_#. Lista de Inspiraciones Caballero
   - URL: /inspiraciones/
   - Contenido: Lista todas las inspiraciones de caballero disponibles con una barra de búsqueda para filtrar las inspiraciones por nombre.
   - Instrucciones para probar: Utiliza la barra de búsqueda para filtrar las inspiraciones.

_#. Detalles de Inspiraciones Caballero
   - URL: /perfume_detail/<int:perfume_id>/
   - Contenido: Muestra los detalles específicos de una inspiración para caballero seleccionada.

_#. Lista de Perfumes Caballero
   - URL: /perfumes/
   - Contenido: Lista todos los perfumes de caballero disponibles con una barra de búsqueda para filtrar los perfumes por nombre.
   - Instrucciones para probar: Utiliza la barra de búsqueda para filtrar los perfumes.

_#. Detalles de Perfumes Caballero
   - URL: /perfumes/<int:perfume_id>/
   - Contenido: Muestra los detalles específicos de un perfume para caballero seleccionado.

_#. Lista de Inspiraciones Dama
   - URL: /inspiraciones_woman/
   - Contenido: Lista todas las inspiraciones para dama disponibles con una barra de búsqueda para filtrar las inspiraciones por nombre.
   - Instrucciones para probar: Utiliza la barra de búsqueda para filtrar las inspiraciones.

_#. Detalles de Inspiraciones Dama
   - URL: /perfume_woman_detail/<int:perfume_id>/
   - Contenido: Muestra los detalles específicos de una inspiración para dama seleccionada.

_#. Lista de Perfumes para Damas
   - URL: /perfumes_woman/
   - Contenido: Lista todos los perfumes para damas disponibles.

_#. Detalles de Perfumes para Damas
   - URL: /perfume_woman/<int:perfume_id>/
   - Contenido: Muestra los detalles específicos de un perfume para damas seleccionado.

_#. Página de Contacto (se modificara, para un proximo " login | register " de usuario)
   - URL: /contacto/
   - Contenido: Presenta un html con mi CV.


Archivos y Configuración:
- zar/views.py: Contiene las vistas que manejan la lógica de cada página.
- zar/urls.py: Define las URLs del proyecto y las rutas a las vistas correspondientes.
- templates/zar/: Contiene las plantillas HTML para renderizar las vistas.
- zar/static: Contiene los archivos estáticos como CSS e imágenes.


Notas Adicionales:
- Asegúrate de que DEBUG esté configurado como True en settings.py durante el desarrollo.
- Los archivos de imágenes deben estar en el directorio configurado para MEDIA_ROOT.
