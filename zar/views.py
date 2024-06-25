from django.shortcuts import render
from .models import *

def home (request):
    return render(request, "zar/home.html")

def perfumes (request):
    return render(request, "zar/perfumes.html")

def inspiraciones (request):
    return render(request, "zar/inspiraciones.html")

def contacto (request):
    return render(request, "zar/contacto.html")
