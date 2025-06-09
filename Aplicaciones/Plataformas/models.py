from django.db import models

# Create your models here.

class Plataforma(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    fabricante = models.TextField()
    anio_lanzamiento = models.IntegerField()
    tipo = models.TextField()
    region_disponible = models.TextField()

    def __str__(self):
        return self.nombre