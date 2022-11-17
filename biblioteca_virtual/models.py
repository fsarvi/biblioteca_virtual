from django.db import models

class Persona(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)
    apellido = models.CharField(max_length=30, blank=False, null=False)
    
    def __str__(self):
        return self.nombre + " " + self.apellido

class Autor(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)

    def __str__(self):
        return self.persona.nombre + " " + self.persona.apellido

class Usuario(models.Model):
    persona = models.OneToOneField(Persona, on_delete=models.CASCADE)
    correo = models.EmailField(max_length=254)
    contrasenia = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.persona.nombre + " " + self.persona.apellido

class Editorial(models.Model):
    nombre = models.CharField(max_length=120, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Genero(models.Model):
    nombre = models.CharField(max_length=30, blank=False, null=False)

    def __str__(self):
        return self.nombre

class Critica(models.Model):
    critica = models.CharField(max_length=254, blank=False, null=False)
    fuente = models.CharField(max_length=120, blank=False, null=False)

    def __str__(self):
        return self.fuente + ":" + self.critica

class Estado(models.Model):
    nuevo = models.BooleanField(default=False)
    leyendo = models.BooleanField(default=False)
    leido = models.BooleanField(default=False)
    favorito = models.BooleanField(default=False)

    def __str__(self):
        nuevo = str(self.nuevo)
        leyendo = str(self.leyendo)
        leido = str(self.leido)
        favorito = str(self.favorito)

        return "Nuevo: " + nuevo + ". Leyendo: " + leyendo + ". Leído: " + leido + ". Favorito: " + favorito

class Resenia(models.Model):
    titulo = models.CharField(max_length=120, blank=False, null=False)
    resenia = models.TextField(max_length=500, blank=False, null=False)

    def __str__(self):
        return self.titulo

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
    autor = models.ForeignKey(Autor, on_delete=models.CASCADE, default = 1)
    resenia = models.OneToOneField(Resenia, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    comentario = models.TextField(max_length=500, blank=False, null=False)
    puntuacion = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.usuario.persona.nombre + " " + self.usuario.persona.apellido + ":" + self.libro.titulo
