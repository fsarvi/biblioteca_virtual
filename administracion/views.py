from django.shortcuts import render, redirect
from django.contrib import messages

from biblioteca_virtual.models import Libro, Genero, Editorial
from administracion.forms import LibroForm, GeneroForm, EditorialForm

def inicio(request):

    return render(request, 'administracion/inicio_administracion.html')

def crear_libro(request):

    formulario = LibroForm(request.POST or None,request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request,'Se ha creado el libro de forma exitosa')   
        return redirect('administracion/inicio_administracion.html')

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
        return redirect('administracion/inicio_administracion.html')

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
        return redirect('administracion/inicio_administracion.html')

    return render(request,'administracion/crear_editorial.html',{'formulario':formulario})

def editar_editorial(request):

    return render(request, 'administracion/inicio_administracion.html')

def eliminar_editorial(request):

    return render(request, 'administracion/inicio_administracion.html')