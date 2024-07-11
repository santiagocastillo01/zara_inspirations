from django import forms
from .models import Perfume, Perfume_woman
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

class PerfumeForm(forms.ModelForm):
    class Meta:
        model = Perfume
        fields = ['imagen_perfume', 'nombre', 'descripcion', 'inspiracion', 'imagen_inspiracion']
        
class PerfumeWomanForm(forms.ModelForm):
    class Meta:
        model = Perfume_woman
        fields = ['imagen_perfume', 'nombre', 'descripcion', 'inspiracion', 'imagen_inspiracion']


class RegistroForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Contraseña a confirmar", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]