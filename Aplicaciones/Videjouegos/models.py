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

    logo = models.FileField(
        upload_to='cargos',  # Carpeta dentro de media/ donde se guarda el logo
        null=True,            # Permite que el campo quede vacío (nulo)
        blank=True            # Permite que el formulario lo deje vacío
    )

    pdf = models.FileField(
        upload_to='pdfs',  # Carpeta dentro de media/ donde se guarda el PDF
        null=True,                # Permite campo vacío
        blank=True
    )

    def __str__(self):
        return self.titulo