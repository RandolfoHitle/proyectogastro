from django.db import models
from users.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nombre}'


class Receta(models.Model):
    titulo = models.CharField(max_length=200)
    ingredientes = models.TextField()
    instrucciones = models.TextField()
    tiempo_preparacion = models.IntegerField()  # En minutos
    categoria = models.ManyToManyField(Categoria)
    imagen = models.ImageField(upload_to='recetas/')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    valoracion = models.FloatField(default=0.0)

    def __str__(self):
        return f'{self.titulo}'

