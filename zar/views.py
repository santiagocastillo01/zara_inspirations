from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from .models import Perfume
from .models import Perfume_woman

#___Home
def home (request):
    return render(request, "zar/home.html")

#__Categorias -> Caballero | Dama
def categoria_perfumes (request):
    return render(request, "zar/categoria_perfumes.html")

def categoria_inspiraciones (request):
    return render(request, "zar/categoria_inspiraciones.html")


#__Perfumes hombre
def perfumes(request):
    search_query = request.GET.get('search', '')
    if search_query:
        perfumes = Perfume.objects.filter(nombre__icontains=search_query)
    else:
        perfumes = Perfume.objects.all()
    
    context = {
        'perfumes': perfumes,
        'search_query': search_query,
    }
    return render(request, 'zar/perfumes.html', context)

def inspiraciones(request):
    search_query = request.GET.get('search', '')
    if search_query:
        perfumes = Perfume.objects.filter(inspiracion__icontains=search_query)
    else:
        perfumes = Perfume.objects.all()
    
    context = {
        'inspiraciones': perfumes, 
        'search_query': search_query,
    }
    return render(request, 'zar/inspiraciones.html', context)

def perfume_detail(request, perfume_id):
    perfume = get_object_or_404(Perfume, pk=perfume_id)
    return render(request, 'zar/perfume_detail.html', {'perfume': perfume})

#___Perfumes Mujer

def perfumes_woman(request):
    search_query = request.GET.get('search', '')
    if search_query:
        perfumes = Perfume_woman.objects.filter(nombre__icontains=search_query)
    else:
        perfumes = Perfume_woman.objects.all()
    
    context = {
        'perfumes': perfumes,
        'search_query': search_query,
    }
    return render(request, 'zar/perfumes_woman.html', context)

def perfume_woman_detail(request, perfume_id):
    perfume_woman = get_object_or_404(Perfume_woman, pk=perfume_id)
    return render(request, 'zar/perfume_woman_detail.html', {'perfume_woman': perfume_woman})

def inspiraciones_woman(request):
    search_query = request.GET.get('search', '')
    if search_query:
        perfumes = Perfume_woman.objects.filter(inspiracion__icontains=search_query)
    else:
        perfumes = Perfume_woman.objects.all()
    
    context = {
        'inspiraciones': perfumes, 
        'search_query': search_query,
    }
    return render(request, 'zar/inspiraciones_woman.html', context)

#__Contacto
def contacto (request):
    return render(request, "zar/contacto.html")



