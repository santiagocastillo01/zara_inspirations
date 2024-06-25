from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Perfume)
admin.site.register(Descripcion)
admin.site.register(Inspiracion)
