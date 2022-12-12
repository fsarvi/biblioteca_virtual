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
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        #se inicializan los widget obteniendo las actualizaciones con el metodo .update y se le da el estilo .form-control a los campos select
        self.fields['autor'].widget.attrs.update({'class':'form-control'})
        self.fields['critica'].widget.attrs.update({'class':'form-control'})
        self.fields['genero'].widget.attrs.update({'class':'form-control'})
        self.fields['estado'].widget.attrs.update({'class':'form-control'})
        self.fields['resenia'].widget.attrs.update({'class':'form-control'})
        self.fields['editorial'].widget.attrs.update({'class':'form-control'})

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

class CriticaForm(forms.ModelForm):

    class Meta:
        model = Critica
        
        fields = ['critica', 'fuente']
        widgets = {
            'critica': forms.TextInput(attrs={'class': 'form-control'}),
            'fuente': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ReseniaForm(forms.ModelForm):

    class Meta:
        model = Resenia
        
        fields = ['titulo', 'resenia']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'resenia': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PersonaForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ['nombre', 'apellido']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
        }

class AutorForm(forms.ModelForm):

    class Meta:
        model = Autor
        fields = ['persona',]
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['persona'].widget.attrs.update({'class':'form-control'})

class UsuarioForm(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['persona', 'correo', 'contrasenia']

        widgets = {
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'contrasenia': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['persona'].widget.attrs.update({'class':'form-control'})
