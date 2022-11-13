from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)

class Autor(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)

class Usuario(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    correo = models.EmailField(max_length=254)
    contrasenia = models.CharField(max_length=30, blank=False, null=False)

class Editorial(models.Model):
    nombre = models.CharField(max_length=120, blank=False, null=False)

class Genero(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)

class Critica(models.Model):
    critica = models.CharField(max_length=254, blank=False, null=False)
    fuente = models.CharField(max_length=120, blank=False, null=False)

class Estado(models.Model):
    nuevo = models.BooleanField(default=False)
    leyendo = models.BooleanField(default=False)
    leido = models.BooleanField(default=False)
    favorito = models.BooleanField(default=False)

class Resenia(models.Model):
    titulo = models.CharField(max_length=120, blank=False, null=False)
    resenia = models.TextField(max_length=500, blank=False, null=False)

class Libro(models.Model):
    titulo = models.CharField(max_length=120, blank=False, null=False)
    descripcion = models.CharField(max_length=254, blank=False, null=False)
    imagen = models.CharField(max_length=120, blank=False, null=False)
    sinopsis = models.TextField(max_length=500, blank=False, null=False)
    fecha_publicacion = models.DateField(blank=False, null=False)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    genero = models.ManyToManyField(Genero)
    critica = models.OneToOneField(Critica, on_delete=models.CASCADE)
    estado = models.ForeignKey(Estado, on_delete=models.CASCADE)
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
    resenia = models.OneToOneField(Resenia, on_delete=models.CASCADE)

class Comentario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=500, blank=False, null=False)
    puntuacion = models.IntegerField(null=False, blank=False)
