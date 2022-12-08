from django.shortcuts import render, redirect
from django.contrib import messages

from biblioteca_virtual.models import Libro, Genero, Editorial, Estado, Autor, Persona, Usuario
from administracion.forms import LibroForm, GeneroForm, EditorialForm, AutorForm, PersonaForm, UsuarioForm

def inicio(request):

    return render(request, 'administracion/inicio_administracion.html')

def crear_libro(request):

    formulario = LibroForm(request.POST or None,request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el libro de forma exitosa')   
        return redirect('inicio')

    return render(request,'administracion/crear_libro.html',{'formulario':formulario})

def editar_libro(request):

    return render(request, 'administracion/inicio_administracion.html')

def eliminar_libro(request):

    return render(request, 'administracion/inicio_administracion.html')


def crear_genero(request):

    formulario = GeneroForm(request.POST or None,request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el género de forma exitosa')   
        return redirect('inicio')

    return render(request,'administracion/crear_genero.html',{'formulario':formulario})

def editar_genero(request):

    return render(request, 'administracion/inicio_administracion.html')

def eliminar_genero(request):

    return render(request, 'administracion/inicio_administracion.html')


def crear_editorial(request):

    formulario = EditorialForm(request.POST or None,request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado editorial de forma exitosa')   
        return redirect('inicio')

    return render(request,'administracion/crear_editorial.html',{'formulario':formulario})

def editar_editorial(request):

    return render(request, 'administracion/inicio_administracion.html')

def eliminar_editorial(request):

    return render(request, 'administracion/inicio_administracion.html')

def crear_persona(request):

    formulario = PersonaForm(request.POST or None,request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado la persona de forma exitosa')   
        return redirect('inicio')

    return render(request,'administracion/crear_persona.html',{'formulario':formulario})

def editar_persona(request):

    return render(request, 'administracion/inicio_administracion.html')

def eliminar_persona(request):

    return render(request, 'administracion/inicio_administracion.html')

def crear_autor(request):

    formulario = AutorForm(request.POST or None,request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el autor de forma exitosa')   
        return redirect('inicio')

    return render(request,'administracion/crear_autor.html',{'formulario':formulario})

def editar_autor(request):

    return render(request, 'administracion/inicio_administracion.html')

def eliminar_autor(request):

    return render(request, 'administracion/inicio_administracion.html')

def crear_usuario(request):

    formulario = UsuarioForm(request.POST or None,request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el usuario de forma exitosa')   
        return redirect('inicio')

    return render(request,'administracion/crear_usuario.html',{'formulario':formulario})

def editar_usuario(request):

    return render(request, 'administracion/inicio_administracion.html')

def eliminar_usuario(request):

    return render(request, 'administracion/inicio_administracion.html')


