from django.db import models

class Lista_libros(models.Model):
    libro_titulo = models.CharField(max_length=120)
    libro_descripcion_breve = models.CharField(max_length=200)
    libro_imagen = models.CharField(max_length=120)
    libro_nuevo = models.BooleanField()
    libro_leyendo = models.BooleanField()
    libro_numero_id = models.IntegerField()  # Sirve para la url de la sinopsis
    libro_sinopsis_breve = models.TextField()
    libro_fecha_publicacion = models.DateField()
    libro_autor  = models.CharField(max_length=150)
    libro_genero = models.CharField(max_length=150)
    libro_formato = models.CharField(max_length=150)
    libro_critica_breve = models.CharField(max_length=400)
    libro_critica_fuente = models.CharField(max_length=150)

class Lista_libros_relacionados(models.Model):
    libro_relacionado_titulo = models.CharField(max_length=200)
    libro_relacionado_imagen = models.CharField(max_length=200)


class Lista_usuarios(models.Model):
    usuario_nombre = models.CharField(max_length=120)
    usuario_critica_libro = models.TextField()
    usuario_puntuacion_libro = models.IntegerField()
