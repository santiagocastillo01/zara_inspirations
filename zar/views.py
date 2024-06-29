from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from .models import Perfume


def home (request):
    return render(request, "zar/home.html")

def perfumes(request):
    perfumes = Perfume.objects.all()
    perfumes_woman = Perfume_woman.objects.all()
    context = {
        'perfumes': perfumes,
        'perfumes_woman': perfumes_woman,
    }
    return render(request, 'zar/perfumes.html', context)

def inspiraciones(request):
    inspiraciones = Perfume.objects.all()
    return render(request, 'zar/inspiraciones.html', {'inspiraciones': inspiraciones})

def contacto (request):
    return render(request, "zar/contacto.html")

def perfume_detail(request, perfume_id):
    perfume = get_object_or_404(Perfume, pk=perfume_id)
    return render(request, 'zar/perfume_detail.html', {'perfume': perfume})

def perfume_woman_detail(request, perfume_id):
    perfume_woman = get_object_or_404(Perfume_woman, pk=perfume_id)
    return render(request, 'zar/perfume_woman_detail.html', {'perfume_woman': perfume_woman})