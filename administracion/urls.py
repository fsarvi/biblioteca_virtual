from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('crear_libro/', views.crear_libro, name= 'crear_libro'),
    path('editar_libro/', views.editar_libro, name= 'editar_libro'),
    path('eliminar_libro/', views.eliminar_libro, name= 'eliminar_libro'),

    path('crear_genero/', views.crear_genero, name= 'crear_genero'),
    path('editar_genero/', views.editar_genero, name= 'editar_genero'),
    path('eliminar_genero/', views.eliminar_genero, name= 'eliminar_genero'),

    path('crear_editorial/', views.crear_editorial, name= 'crear_editorial'),
    path('editar_editorial/', views.editar_editorial, name= 'editar_editorial'),
    path('eliminar_editorial/', views.eliminar_editorial, name= 'eliminar_editorial'),

    path('crear_persona/', views.crear_persona, name= 'crear_persona'),
    path('editar_persona/', views.editar_persona, name= 'editar_persona'),
    path('eliminar_persona/', views.eliminar_persona, name= 'eliminar_persona'),

    path('crear_autor/', views.crear_autor, name= 'crear_autor'),
    path('editar_autor/', views.editar_autor, name= 'editar_autor'),
    path('eliminar_autor/', views.eliminar_autor, name= 'eliminar_autor'),

    path('crear_usuario/', views.crear_usuario, name= 'crear_usuario'),
    path('editar_usuario/', views.editar_usuario, name= 'editar_usuario'),
    path('eliminar_usuario/', views.eliminar_usuario, name= 'eliminar_usuario'),

    ]
