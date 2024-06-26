from django.shortcuts import render
from .models import *

def home (request):
    return render(request, "zar/home.html")

def perfumes (request):
    perfumes = Perfume.objects.all()
    return render(request, 'zar/perfumes.html', {'perfumes': perfumes})

def inspiraciones (request):
    return render(request, "zar/inspiraciones.html")

def contacto (request):
    return render(request, "zar/contacto.html")
