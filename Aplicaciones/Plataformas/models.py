from django.db import models

# Create your models here.

class Plataforma(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()
    fabricante = models.TextField()
    anio_lanzamiento = models.IntegerField()
    tipo = models.TextField()
    region_disponible = models.TextField()

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
        return self.nombre