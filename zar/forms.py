""" {% extends "entidades/index.html" %}


{% block titulo %}
<h1 class="mb-5">Formulario Cursos</h1>                                
{% endblock titulo %}


{% block contenido %}   

<form action="" method="post">
    {% csrf_token %}
    <table>
        {{ form }}
    </table>
    <input type="submit" value="Guardar">
</form>

{% endblock contenido %} """