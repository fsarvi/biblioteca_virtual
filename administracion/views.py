from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from biblioteca_virtual.models import Libro, Genero, Editorial, Estado, Autor, Persona, Usuario, Critica, Resenia
from administracion.forms import LibroForm, GeneroForm, EditorialForm, AutorForm, PersonaForm, UsuarioForm, CriticaForm, ReseniaForm, RegistrarUsuario


def administracion_login(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            form = login(request, user)
            return redirect('index')
        else:
            messages.error(request, f'Error: Por favor revise el usuario o la contraseña ')
    
    form = AuthenticationForm()
    formulario_inicio = {'form': form, 'title': 'inicio de sesion'}
    return render(request, 'sesion/administracion_login.html', formulario_inicio )



def administracion_registro(request):
    if request.method == 'POST':
        form = RegistrarUsuario(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Cuenta creada con exito! inicie sesion.')
            return redirect('administracion_login')
    else:
        form = RegistrarUsuario()
    return render(request, 'sesion/administracion_registro.html', {'form': form, 'title': 'registrese aquí'})



def administracion_logout(request):
    logout(request)
    return redirect('index')


@login_required
def inicio(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def crear_libro(request):

    formulario = LibroForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Se ha creado el libro de forma exitosa')
        return redirect('inicio')

    return render(request, 'administracion/crear_libro.html', {'formulario': formulario})


@login_required
def editar_libro(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def eliminar_libro(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def crear_genero(request):

    formulario = GeneroForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Se ha creado el género de forma exitosa')
        return redirect('inicio')

    return render(request, 'administracion/crear_genero.html', {'formulario': formulario})


@login_required
def editar_genero(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def eliminar_genero(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def crear_editorial(request):

    formulario = EditorialForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Se ha creado editorial de forma exitosa')
        return redirect('inicio')

    return render(request, 'administracion/crear_editorial.html', {'formulario': formulario})


@login_required
def editar_editorial(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def eliminar_editorial(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def crear_critica(request):

    formulario = CriticaForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Se ha creado la crítica de forma exitosa')
        return redirect('inicio')

    return render(request, 'administracion/crear_critica.html', {'formulario': formulario})


@login_required
def editar_critica(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def eliminar_critica(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def crear_resenia(request):

    formulario = ReseniaForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Se ha creado la reseña de forma exitosa')
        return redirect('inicio')

    return render(request, 'administracion/crear_resenia.html', {'formulario': formulario})


@login_required
def editar_resenia(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def eliminar_resenia(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def crear_persona(request):

    formulario = PersonaForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Se ha creado la persona de forma exitosa')
        return redirect('inicio')

    return render(request, 'administracion/crear_persona.html', {'formulario': formulario})


@login_required
def editar_persona(request):

    return render(request, 'administracion/inicio_administracion.html')


def eliminar_persona(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def crear_autor(request):

    formulario = AutorForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Se ha creado el autor de forma exitosa')
        return redirect('inicio')

    return render(request, 'administracion/crear_autor.html', {'formulario': formulario})


@login_required
def editar_autor(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def eliminar_autor(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def crear_usuario(request):

    formulario = UsuarioForm(request.POST or None, request.FILES or None)

    if formulario.is_valid():
        formulario.save()
        messages.success(request, 'Se ha creado el usuario de forma exitosa')
        return redirect('inicio')

    return render(request, 'administracion/crear_usuario.html', {'formulario': formulario})


@login_required
def editar_usuario(request):

    return render(request, 'administracion/inicio_administracion.html')


@login_required
def eliminar_usuario(request):

    return render(request, 'administracion/inicio_administracion.html')
