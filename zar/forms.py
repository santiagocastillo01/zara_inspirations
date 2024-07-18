from django import forms
from .models import Perfume, Perfume_woman
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from .models import Usuario
from .models import Avatar

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

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ["username", "email"]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields.pop('password')

        
        self.fields['username'].label = "Nombre de usuario"

class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}))
    new_password2 = forms.CharField(
            widget=forms.PasswordInput(attrs={'class': 'form-control', 'type': 'password'}),
            label="Confirm new password"
    )

    class Meta:
        model = User
        fields = ("old_password", "new_password1", "new_password2")

class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['imagen']