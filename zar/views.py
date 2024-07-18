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
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .forms import UserEditForm, PasswordChangingForm
from .models import Avatar
from django.contrib.auth.models import User
from .forms import AvatarForm 

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
    user = request.user
    avatar = Avatar.objects.filter(user=user).first()

    context = {
        "user": user,
        "avatar": avatar,
    }
    return render(request, 'zar/perfil_detail.html', context)

def upload_avatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.save(commit=False)
            avatar.user = request.user
            avatar.save()
            messages.success(request, '¡Avatar subido correctamente!')
            return redirect('perfil')
        else:
            messages.error(request, 'Hubo un error al subir el avatar. Por favor, corrige los errores.')
    else:
        form = AvatarForm()
    
    return render(request, 'zar/subir_avatar.html', {'form': form})

def delete_avatar(request):
    if request.method == 'POST':
        user = request.user
        avatar = Avatar.objects.filter(user=user).first()
        if avatar:
            avatar.delete()
            messages.success(request, '¡Avatar eliminado correctamente!')
        else:
            messages.error(request, 'No tienes un avatar configurado.')
    return redirect('perfil')

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
    
@login_required
def edit_profile(request):
    if request.method == 'POST':
        user_form = UserEditForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            messages.success(request, '¡Tu perfil ha sido actualizado con éxito!')
            return redirect('perfil')
    else:
        user_form = UserEditForm(instance=request.user)
    
    return render(request, 'zar/edit_profile.html', {'user_form': user_form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangingForm(data=request.POST, user=request.user)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, '¡Tu contraseña ha sido cambiada con éxito!')
            return redirect('perfil')
        else:
            messages.error(request, 'Por favor corrige el error a continuación.')
    else:
        form = PasswordChangingForm(user=request.user)
    
    return render(request, 'zar/change_password.html', {'form': form})
