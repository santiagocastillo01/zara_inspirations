from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Perfume(models.Model):
    imagen_perfume = models.ImageField(upload_to='perfumes/', default='Error.')
    nombre = models.CharField(max_length=100, default='Nombre de perfume')
    descripcion = models.TextField(default='Descripción')
    inspiracion = models.CharField(max_length=100, default='Nombre Inspiracion')
    imagen_inspiracion = models.ImageField(upload_to='inspiraciones/', default='Error.')

    def __str__(self):
        return self.nombre
     
    class Meta:
        ordering = ['nombre']

class Perfume_woman(models.Model):
    imagen_perfume = models.ImageField(upload_to='perfumes_woman/', default='Error.')
    nombre = models.CharField(max_length=100, default='Nombre de perfume')
    descripcion = models.TextField(default='Descripción')
    inspiracion = models.CharField(max_length=100, default='Nombre Inspiracion')
    imagen_inspiracion = models.ImageField(upload_to='inspiraciones_woman/', default='Error.')

    def __str__(self):
        return self.nombre
    
    class Meta:
        ordering = ['nombre']


class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio')
        email = self.normalize_email(email)
        usuario = self.model(email=email, **extra_fields)
        usuario.set_password(password)
        usuario.save(using=self._db)
        return usuario

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser):
    imagen_usuario = models.ImageField(upload_to='usuario/', default='usuario/default.png')
    nombre_usuario = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'nombre_usuario'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email']

    objects = UsuarioManager()

    def __str__(self):
        return self.nombre_usuario

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

    def set_password(self, raw_password):
        self.password = make_password(raw_password)
        self.save()

class Staff(models.Model):
    imagen_perfil = models.ImageField(upload_to='usuario/', default='Error.')
    nombre_completo = models.CharField(max_length=100, default='Nombre no disponible')
    email = models.EmailField(unique=True)
    sobre_mi = models.TextField(blank=True, null=True, default='')
    linkedin_url = models.URLField(blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)  

    def __str__(self):
        return self.nombre_completo

class Avatar(models.Model):
    imagen = models.ImageField(upload_to="avatares") 
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} {self.imagen}" 
