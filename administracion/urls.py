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
    ]
