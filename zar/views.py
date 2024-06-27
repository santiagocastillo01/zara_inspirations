from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from .models import Perfume


def home (request):
    return render(request, "zar/home.html")

def perfumes (request):
    perfumes = Perfume.objects.all()
    return render(request, 'zar/perfumes.html', {'perfumes': perfumes})

def inspiraciones(request):
    inspiraciones = Perfume.objects.all()
    return render(request, 'zar/inspiraciones.html', {'inspiraciones': inspiraciones})

def contacto (request):
    return render(request, "zar/contacto.html")

def perfume_detail(request, perfume_id):
    perfume = get_object_or_404(Perfume, pk=perfume_id)
    return render(request, 'zar/perfume_detail.html', {'perfume': perfume})
