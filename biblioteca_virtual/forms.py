from django import forms
from django.forms import ValidationError

def solo_caracteres(value):
    if any(char.isdigit() for char in value ):
        raise ValidationError('El campo no puede contener números: %(valor)s',
                            code='Error1',
                            params={'valor':value})

def maximo_caracteres(value):
          
        if len(value) > 10:
            raise ValidationError("Superas la cantidad máxima de 10 caracteres")
        return 

def clean_nombre(self):
        data = self.cleaned_data['nombre']
        if len(data) > 10:
            raise ValidationError("Superas la cantidad máxima de 10 caracteres")
        return data

class ContactoForm(forms.Form):

    nombre = forms.CharField(
            label='Nombre',
            max_length=10,
            validators=(solo_caracteres,maximo_caracteres),
            widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese solo texto'})
            )
    apellido = forms.CharField(
            label='Apellido',
            max_length=10,
            validators=(solo_caracteres,maximo_caracteres),
            widget= forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese solo texto'})
            )

    email = forms.EmailField(
            label='Email',
            max_length=50,
            error_messages={
                    'required': 'Por favor completa el campo',                    
                },
            widget= forms.TextInput(attrs={'class':'form-control','type':'email'})
            )
    mensaje = forms.CharField(
            label='Mensaje',
            max_length=500,
            widget=forms.Textarea(attrs={'class':'form-control','rows':5}))
