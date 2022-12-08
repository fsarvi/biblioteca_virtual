from django import forms
from django.forms import ValidationError

from biblioteca_virtual.models import *


class LibroForm(forms.ModelForm):

    class Meta:
        model = Libro
        #imagen como campo charfield, pasar a uno que se puede cargar imagen?
        fields = ['titulo', 'descripcion', 'imagen', 'sinopsis', 'fecha_publicacion',
                  'editorial', 'genero', 'critica', 'estado', 'autor', 'resenia']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'imagen': forms.TextInput(attrs={'class': 'form-control'}),
            'sinopsis': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_publicacion': forms.TextInput(attrs={'class': 'form-control'}),
            'editorial': forms.TextInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'}),
            'critica': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'resenia': forms.TextInput(attrs={'class': 'form-control'}),
        }

class GeneroForm(forms.ModelForm):

    class Meta:
        model = Genero
        
        fields = ['nombre',]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }

class EditorialForm(forms.ModelForm):

    class Meta:
        model = Editorial
        
        fields = ['nombre',]
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
        }
