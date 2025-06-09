from django.db import models

class Plataforma(models.Model):
    id = models.AutoField(primary_key=True)  
    nombre = models.CharField(max_length=100, unique=True)  
    fabricante = models.CharField(max_length=100)  
    anio_lanzamiento = models.IntegerField()  
    tipo = models.CharField(max_length=50)  
    region_disponible = models.CharField(max_length=100)  

    logo = models.FileField(upload_to='plataformas', null=True, blank=True)  
    pdf = models.FileField(upload_to='plataformas', null=True, blank=True)  

    def __str__(self):
        return f"{self.nombre} ({self.fabricante})"
