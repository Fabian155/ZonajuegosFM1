from django.shortcuts import render, redirect
from .models import Plataforma
from django.contrib import messages
from django.conf import settings
import os

# ✅ Listar plataformas
def listarPlataformas(request):
    listaPlataforma = Plataforma.objects.all()  # Obtiene todas las plataformas
    return render(request, "Plataformas/inicio2.html", {'plataformas': listaPlataforma})

# ✅ Formulario para agregar una nueva plataforma
def nuevaPlataforma(request):
    return render(request, "Plataformas/nuevaPlataforma.html")

# ✅ Guardar plataforma en la base de datos
def guardarPlataforma(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        fabricante = request.POST["fabricante"]
        anio_lanzamiento = request.POST["anio_lanzamiento"]
        tipo = request.POST["tipo"]
        region_disponible = request.POST["region_disponible"]

        logo = request.FILES.get("logo")
        pdf = request.FILES.get("pdf")

        Plataforma.objects.create(
            nombre=nombre, fabricante=fabricante,
            anio_lanzamiento=anio_lanzamiento, tipo=tipo,
            region_disponible=region_disponible, logo=logo, pdf=pdf
        )

        messages.success(request, "SE HA AGREGADO LA PLATAFORMA")
        return redirect('listarPlataformas')

    return redirect('listarPlataformas')

# ✅ Eliminar plataforma y sus archivos relacionados
def eliminarPlataforma(request, id):
    plataformaEliminar = Plataforma.objects.get(id=id)

    if plataformaEliminar.logo:
        ruta_logo = os.path.join(settings.MEDIA_ROOT, plataformaEliminar.logo.name)
        if os.path.isfile(ruta_logo):
            os.remove(ruta_logo)

    if plataformaEliminar.pdf:
        ruta_pdf = os.path.join(settings.MEDIA_ROOT, plataformaEliminar.pdf.name)
        if os.path.isfile(ruta_pdf):
            os.remove(ruta_pdf)

    plataformaEliminar.delete()
    messages.success(request, "SE HA ELIMINADO LA PLATAFORMA")
    return redirect('listarPlataformas')

# ✅ Formulario de edición de plataforma
def editarPlataforma(request, id):
    plataforma = Plataforma.objects.get(id=id)
    return render(request, "Plataformas/editarPlataforma.html", {'plataforma': plataforma})

# ✅ Procesar edición y actualizar en la BD
def procesarEdicionPlataforma(request, id):
    nombre = request.POST["nombre"]
    fabricante = request.POST["fabricante"]
    anio_lanzamiento = request.POST["anio_lanzamiento"]
    tipo = request.POST["tipo"]
    region_disponible = request.POST["region_disponible"]

    plataforma = Plataforma.objects.get(id=id)
    plataforma.nombre = nombre
    plataforma.fabricante = fabricante
    plataforma.anio_lanzamiento = anio_lanzamiento
    plataforma.tipo = tipo
    plataforma.region_disponible = region_disponible

    if "logo" in request.FILES:
        nuevo_logo = request.FILES.get("logo")
        if plataforma.logo:
            ruta_logo_antiguo = os.path.join(settings.MEDIA_ROOT, plataforma.logo.name)
            if os.path.isfile(ruta_logo_antiguo):
                os.remove(ruta_logo_antiguo)
        plataforma.logo = nuevo_logo

    if "pdf" in request.FILES:
        nuevo_pdf = request.FILES.get("pdf")
        if plataforma.pdf:
            ruta_pdf_antiguo = os.path.join(settings.MEDIA_ROOT, plataforma.pdf.name)
            if os.path.isfile(ruta_pdf_antiguo):
                os.remove(ruta_pdf_antiguo)
        plataforma.pdf = nuevo_pdf

    plataforma.save()
    messages.success(request, "SE HA EDITADO LA PLATAFORMA")

    return redirect('listarPlataformas')
