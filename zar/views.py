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
from django.contrib.auth import logout

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

def edit_perfume(request, perfume_id):
    perfume = get_object_or_404(Perfume, pk=perfume_id)
    if request.method == 'POST':
        form = PerfumeForm(request.POST, request.FILES, instance=perfume)
        if form.is_valid():
            form.save()
            return redirect('perfume_detail', perfume_id=perfume.id)
    else:
        form = PerfumeForm(instance=perfume)
    return render(request, 'zar/edit_perfume.html', {'form': form, 'perfume': perfume})

def delete_perfume(request, perfume_id):
    perfume = get_object_or_404(Perfume, pk=perfume_id)
    if request.method == 'POST':
        perfume.delete()
        return redirect('perfumes') 
    return render(request, 'zar/delete_perfume.html', {'perfume': perfume})

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

def edit_perfume_woman(request, perfume_id):
    perfume = get_object_or_404(Perfume_woman, pk=perfume_id)
    if request.method == 'POST':
        form = PerfumeWomanForm(request.POST, request.FILES, instance=perfume)
        if form.is_valid():
            form.save()
            return redirect('perfume_woman_detail', perfume_id=perfume.id)
    else:
        form = PerfumeWomanForm(instance=perfume)
    return render(request, 'zar/edit_perfume_woman.html', {'form': form, 'perfume': perfume})

def delete_perfume_woman(request, perfume_id):
    perfume = get_object_or_404(Perfume_woman, pk=perfume_id)
    if request.method == 'POST':
        perfume.delete()
        return redirect('perfumes_woman') 
    return render(request, 'zar/delete_perfume_woman.html', {'perfume': perfume})
#__Sobre_mi
def sobre_mi(request):
    staff = Staff.objects.first()
    return render(request, "zar/sobre_mi.html", {'staff': staff})


# ___ Login / Logout / Registration

def loginRequest(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)  # Ajuste aquí
            if user is not None:
                login(request, user)
                return redirect('perfil')  # Redirige a la vista de perfil después de iniciar sesión
        # Renderiza el formulario con errores si no es válido
        return render(request, 'zar/login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render(request, 'zar/login.html', {'form': form})


@login_required
def perfil(request):
    return render(request, 'zar/perfil_detail.html', {"user": request.user})

def logout_view(request):
    logout(request)
    return redirect('login')

def register(request):
    if request.method == "POST":
        miForm = RegistroForm(request.POST, request.FILES)
        if miForm.is_valid():
            user = miForm.save(commit=False)
            user.set_password(miForm.cleaned_data["password1"])
            user.save()
            login(request, user)
            return redirect('perfil')  # Redirige a la vista de perfil después de registrarse
        # Renderiza el formulario con errores si no es válido
        return render(request, "zar/register.html", {"form": miForm})
    else:
        miForm = RegistroForm()
        return render(request, "zar/register.html", {"form": miForm})
