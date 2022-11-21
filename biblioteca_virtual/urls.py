from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name= 'index'),
    path('sinopsis/<int:id>/',views.sinopsis, name= 'sinopsis'),
    path('buscar/',views.buscar, name= 'busqueda'),
    path('nuestro-equipo/',views.equipo, name= 'equipo'),
    path('contacto/',views.contacto, name= 'contacto'),
    path('reseñas/',views.resenias, name='reseñas'),
    path('entrada-reseña', views.entrada_resenia, name='entradareseña'),
    path('favoritos', views.favoritos, name='favoritos'),
    # # URLs solo para poblar la base de datos
    # path('llenar_recomendaciones_1/', views.llenar_recomendaciones_1, name='llenar_recomendaciones_1'),
    # path('llenar_recomendaciones_1/llenar_recomendaciones/', views.llenar_recomendaciones, name='llenar_recomendaciones'),
    # path('llenar_libros_1/', views.llenar_libros_1, name='llenar_libros_1'),
    path('llenar_libros_1/llenar_libros/', views.llenar_libros, name='llenar_libros'),
    # path('llenar_relacionados_1/', views.llenar_relacionados_1, name='llenar_relacionados_1'),
    # path('llenar_relacionados_1/llenar_relacionados/', views.llenar_relacionados, name='llenar_relacionados'),
    # # fin URLs para poblar base de datos
    # path('ver_tabla_libros', views.ver_tabla_libros, name= 'ver_tabla_libros'),
    ]
