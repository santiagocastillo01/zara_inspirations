from django.db import models

# Create your models here.

class Perfume(models.Model):
    imagen_perfume = models.ImageField(upload_to='perfumes/', default='Error.')
    nombre = models.CharField(max_length=100, default='Nombre no disponible')
    descripcion = models.TextField(default='Descripción no disponible')
    inspiracion = models.CharField(max_length=100, default='Nombre no disponible')
    imagen_inspiracion = models.ImageField(upload_to='inspiraciones/', default='Error.')

    def __str__(self):
        return self.nombre
