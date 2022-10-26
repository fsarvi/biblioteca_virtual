from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= 'index'),
    path('sinopsis/<int:id>/',views.sinopsis, name= 'sinopsis'),
    path('nuestro-equipo/',views.equipo, name= 'equipo'),
    path('contacto/',views.contacto, name= 'contacto')
]
