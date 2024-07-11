from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


from .models import *
from .forms import *


from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import PasswordChangeView

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

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

def add_perfume(request):
    if request.method == "POST":
        form = PerfumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PerfumeForm()
    return render(request, 'zar/add_perfume.html', {'form': form})


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

def add_perfume_woman(request):
    if request.method == "POST":
        form = PerfumeWomanForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PerfumeWomanForm()
    return render(request, 'zar/add_perfume_woman.html', {'form': form})

#__Sobre_mi
def sobre_mi(request):
    staff = Staff.objects.first()
    return render(request, "zar/sobre_mi.html", {'staff': staff})


# ___ Login / Logout / Registration

def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)

            #_______ Buscar Avatar
            try:
                avatar = Avatar.objects.get(user=request.user.id).imagen.url
            except:
                avatar = "/media/avatares/default.png"
            finally:
                request.session["avatar"] = avatar
            #______________________________________________________________
            return render(request, "zar/home.html")
        else:
            return redirect(reverse_lazy('login'))

    else:
        miForm = AuthenticationForm()

    return render(request, "zar/login.html", {"form": miForm})

def perfil(request):
    return render(request, "zar/perfil.html")

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST)
        if miForm.is_valid():
            #usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = RegistroForm()

    return render(request, "zar/register.html", {"form": miForm})

def edit_perfil(request):
    return render(request, "zar/edit_perfil.html")
