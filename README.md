Zara Inspirations


# Descripción:
Este es un proyecto de Django que permite a los usuarios buscar y explorar
perfumes y sus inspiraciones. El proyecto incluye funcionalidades para listar 
perfumes, filtrar por nombre, y ver detalles específicos de cada perfume e 
inspiración. Solo los usuarios administradores tienen permisos
para agregar, editar y eliminar perfumes.

# Link video en "Youtube":
https://www.youtube.com/watch?v=K8aBCi3_oRs


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
    USER : administrador
    PASSWORD: 1234

2. Usuario ejemplo:
    USER : pedrito
    PASSWORD: santiagocastillo
   (este usuario no cuenta con "foto de perfil", se le puede agregar)


Estructura del Proyecto:
- zar/: Contiene las vistas y URLs del proyecto.
- templates/zar/: Contiene las plantillas HTML.
- static/: Contiene los archivos estáticos, como CSS e imágenes.


# Funcionalidades y Cómo Probarlas:

1. **Página de Inicio**
   - **URL:** /
   - **Contenido:** Presenta la introducción al proyecto y enlaces a las categorías de inspiraciones y perfumes, con header funcional.

2. **Categoría de Inspiraciones**
   - **URL:** /categoria_inspiraciones/
   - **Contenido:** Muestra un HTML previo para elegir qué inspiraciones buscar, de dama o caballero.

3. **Categoría de Perfumes**
   - **URL:** /categoria_perfumes/
   - **Contenido:** Muestra un HTML previo para elegir qué perfumes buscar, de dama o caballero.

4. **Lista de Inspiraciones Caballero**
   - **URL:** /inspiraciones/
   - **Contenido:** Lista todas las inspiraciones de caballero disponibles con una barra de búsqueda para filtrar las inspiraciones por nombre.
   - **Instrucciones para probar:** Utiliza la barra de búsqueda para filtrar las inspiraciones.

5. **Detalles de Inspiraciones Caballero**
   - **URL:** /perfume_detail/<int:perfume_id>/
   - **Contenido:** Muestra los detalles específicos de una inspiración para caballero seleccionada.

6. **Lista de Perfumes Caballero**
   - **URL:** /perfumes/
   - **Contenido:** Lista todos los perfumes de caballero disponibles con una barra de búsqueda para filtrar los perfumes por nombre.
   - **Instrucciones para probar:** Utiliza la barra de búsqueda para filtrar los perfumes.

7. **Detalles de Perfumes Caballero**
   - **URL:** /perfumes/<int:perfume_id>/
   - **Contenido:** Muestra los detalles específicos de un perfume para caballero seleccionado.

8. **Lista de Inspiraciones Dama**
   - **URL:** /inspiraciones_woman/
   - **Contenido:** Lista todas las inspiraciones para dama disponibles con una barra de búsqueda para filtrar las inspiraciones por nombre.
   - **Instrucciones para probar:** Utiliza la barra de búsqueda para filtrar las inspiraciones.

9. **Detalles de Inspiraciones Dama**
   - **URL:** /perfume_woman_detail/<int:perfume_id>/
   - **Contenido:** Muestra los detalles específicos de una inspiración para dama seleccionada.

10. **Lista de Perfumes para Damas**
    - **URL:** /perfumes_woman/
    - **Contenido:** Lista todos los perfumes para damas disponibles.

11. **Detalles de Perfumes para Damas**
    - **URL:** /perfume_woman/<int:perfume_id>/
    - **Contenido:** Muestra los detalles específicos de un perfume para damas seleccionado.

12. **Página para agregar perfume de Caballero**
    - **URL:** /add_perfume
    - **Contenido:** Formulario para agregar perfume de caballero en la base de datos.
    - **Solo para administradores:** Sí

13. **Página para agregar perfume de Dama**
    - **URL:** /add_perfume_woman
    - **Contenido:** Formulario para agregar perfume de dama en la base de datos.
    - **Solo para administradores:** Sí

14. **Página de Sobre Mí**
    - **URL:** /sobre_mi/
    - **Contenido:** Solo muestra la clase "Staff" de la base de datos.

15. **Editar Perfume de Caballero**
    - **URL:** /perfume/<int:perfume_id>/edit/
    - **Contenido:** Muestra formulario para editar el perfume seleccionado.
    - **Solo para administradores:** Sí

16. **Eliminar Perfume de Caballero**
    - **URL:** /perfume/<int:perfume_id>/delete/
    - **Contenido:** Elimina el perfume seleccionado.
    - **Solo para administradores:** Sí

17. **Editar Perfume de Dama**
    - **URL:** /perfume_woman/<int:perfume_id>/edit/
    - **Contenido:** Muestra formulario para editar el perfume seleccionado.
    - **Solo para administradores:** Sí

18. **Eliminar Perfume de Dama**
    - **URL:** /perfume_woman/<int:perfume_id>/delete/
    - **Contenido:** Elimina el perfume seleccionado.
    - **Solo para administradores:** Sí

19. **Página de Login**
    - **URL:** /login/
    - **Contenido:** Formulario de login.

20. **Página de Logout**
    - **URL:** /logout/
    - **Contenido:** Cierra la sesión del usuario.

21. **Página de Registro**
    - **URL:** /register/
    - **Contenido:** Formulario de registro.

22. **Detalle del Perfil**
    - **URL:** /perfil/
    - **Contenido:** Muestra los detalles del perfil del usuario.

23. **Subir Avatar**
    - **URL:** /subir-avatar/
    - **Contenido:** Muestra formulario para subir un avatar.

24. **Eliminar Avatar**
    - **URL:** /eliminar-avatar/
    - **Contenido:** Elimina el avatar del perfil del usuario.

25. **Editar Perfil de Usuario**
    - **URL:** /perfil/editar/
    - **Contenido:** Muestra formulario para editar los detalles del usuario.

26. **Cambiar Contraseña**
    - **URL:** /perfil/cambiar_contraseña/
    - **Contenido:** Muestra formulario para cambiar la contraseña del usuario.



Archivos y Configuración:
- zar/views.py: Contiene las vistas que manejan la lógica de cada página.
- zar/urls.py: Define las URLs del proyecto y las rutas a las vistas correspondientes.
- templates/zar/: Contiene las plantillas HTML para renderizar las vistas.
- zar/static: Contiene los archivos estáticos como CSS e imágenes.


Notas Adicionales:
- Asegúrate de que DEBUG esté configurado como True en settings.py durante el desarrollo.
- Los archivos de imágenes deben estar en el directorio configurado para MEDIA_ROOT.
