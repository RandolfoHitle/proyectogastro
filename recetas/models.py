from django.db import models

class Usuario(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=255)
    fecha_registro = models.DateTimeField(auto_now_add=True)

class Pais(models.Model):
    nombre = models.CharField(max_length=100)

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    es_original = models.BooleanField(default=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    version_num = models.IntegerField(default=1)

class Ingrediente(models.Model):
    nombre = models.CharField(max_length=100)

class RecetaIngrediente(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    ingrediente = models.ForeignKey(Ingrediente, on_delete=models.CASCADE)
    cantidad = models.CharField(max_length=50)

class Comentario(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    texto = models.TextField()
    fecha_comentario = models.DateTimeField(auto_now_add=True)

class Calificacion(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    calificacion = models.IntegerField()

class PropuestaReceta(models.Model):
    nombre_usuario = models.CharField(max_length=100)
    correo_usuario = models.EmailField()
    nombre_receta = models.CharField(max_length=100)
    descripcion = models.TextField()
    es_original = models.BooleanField(default=True)
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, null=True)
    revisada = models.BooleanField(default=False)
    aprobada = models.BooleanField(default=False)
    fecha_propuesta = models.DateTimeField(auto_now_add=True)

class RegistroActividad(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    accion = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_actividad = models.DateTimeField(auto_now_add=True)

class HistorialVersionesReceta(models.Model):
    receta = models.ForeignKey(Receta, on_delete=models.CASCADE)
    version_num = models.IntegerField()
    cambios = models.TextField()
    fecha_version = models.DateTimeField(auto_now_add=True)

class TecnicaCulinaria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    video_url = models.CharField(max_length=255, blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
