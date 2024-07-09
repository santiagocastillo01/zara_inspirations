from django import forms
from .models import Perfume, Perfume_woman

class PerfumeForm(forms.ModelForm):
    class Meta:
        model = Perfume
        fields = ['imagen_perfume', 'nombre', 'descripcion', 'inspiracion', 'imagen_inspiracion']
        
class PerfumeWomanForm(forms.ModelForm):
    class Meta:
        model = Perfume_woman
        fields = ['imagen_perfume', 'nombre', 'descripcion', 'inspiracion', 'imagen_inspiracion']
