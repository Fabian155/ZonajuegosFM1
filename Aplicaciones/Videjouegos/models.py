from django.db import models
from Aplicaciones.Plataformas.models import Plataforma

class Videojuego(models.Model):
    id = models.AutoField(primary_key=True)  
    titulo = models.CharField(max_length=100, unique=True)  
    genero = models.CharField(max_length=50)  
    desarrollador = models.CharField(max_length=100)  
    fecha_lanzamiento = models.DateField()
    clasificacion = models.CharField(max_length=20)  
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE, related_name="videojuegos")  
    
    logo = models.FileField(upload_to='videojuegos', null=True, blank=True)  
    pdf = models.FileField(upload_to='videojuegos', null=True, blank=True)  

def __str__(self):
    return f"{self.titulo} ({self.plataforma.nombre})"
