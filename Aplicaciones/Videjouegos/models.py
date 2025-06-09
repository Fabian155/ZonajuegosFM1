from django.db import models
from Aplicaciones.Plataformas.models import Plataforma

# Create your models here.

class Videojuego(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField()
    genero = models.TextField()
    desarrollador = models.TextField()
    fecha_lanzamiento = models.DateField()
    clasificacion = models.TextField()
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo