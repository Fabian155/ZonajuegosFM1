from django.shortcuts import render, redirect
from .models import Videojuego
from Aplicaciones.Plataformas.models import Plataforma
from django.contrib import messages
from django.conf import settings
import os

# ✅ Listar videojuegos
def listarVideojuegos(request):
    listaJuegos = Videojuego.objects.select_related('plataforma').all()  # Optimización con select_related
    return render(request, "Videojuegos/inicio1.html", {'Juegos': listaJuegos})

# ✅ Formulario para agregar un nuevo videojuego
def nuevoVideojuego(request):
    plataformas = Plataforma.objects.all()  # Obtener todas las plataformas disponibles
    return render(request, "Videojuegos/nuevoVideojuego.html", {'plataformas': plataformas})

# ✅ Guardar videojuego en la base de datos
def guardarVideojuego(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        genero = request.POST["genero"]
        desarrollador = request.POST["desarrollador"]
        fecha_lanzamiento = request.POST["fecha_lanzamiento"]
        clasificacion = request.POST["clasificacion"]

        plataforma_id = request.POST["plataforma"]
        plataforma = Plataforma.objects.get(id=plataforma_id)

        logo = request.FILES.get("logo")
        pdf = request.FILES.get("pdf")

        Videojuego.objects.create(
            titulo=titulo, genero=genero, desarrollador=desarrollador,
            fecha_lanzamiento=fecha_lanzamiento, clasificacion=clasificacion,
            plataforma=plataforma, logo=logo, pdf=pdf
        )

        messages.success(request, "SE HA AGREGADO EL VIDEOJUEGO")
        return redirect('listarVideojuegos')

    return redirect('listarVideojuegos')

# ✅ Eliminar videojuego y sus archivos relacionados
def eliminarVideojuego(request, id):
    videojuegoEliminar = Videojuego.objects.get(id=id)

    if videojuegoEliminar.logo:
        ruta_logo = os.path.join(settings.MEDIA_ROOT, videojuegoEliminar.logo.name)
        if os.path.isfile(ruta_logo):
            os.remove(ruta_logo)

    if videojuegoEliminar.pdf:
        ruta_pdf = os.path.join(settings.MEDIA_ROOT, videojuegoEliminar.pdf.name)
        if os.path.isfile(ruta_pdf):
            os.remove(ruta_pdf)

    videojuegoEliminar.delete()
    messages.success(request, "SE HA ELIMINADO EL VIDEOJUEGO")
    return redirect('listarVideojuegos')

# ✅ Formulario de edición de videojuego
def editarVideojuego(request, id):
    videojuego = Videojuego.objects.get(id=id)
    plataformas = Plataforma.objects.all()  # Obtener todas las plataformas disponibles
    return render(request, "Videojuegos/editarVideojuego.html", {'videojuego': videojuego, 'plataformas': plataformas})

# ✅ Procesar edición y actualizar en la BD
def procesarEdicionVideojuego(request, id):
    titulo = request.POST["titulo"]
    genero = request.POST["genero"]
    desarrollador = request.POST["desarrollador"]
    fecha_lanzamiento = request.POST["fecha_lanzamiento"]
    clasificacion = request.POST["clasificacion"]

    plataforma_id = request.POST["plataforma"]
    videojuego = Videojuego.objects.get(id=id)
    videojuego.titulo = titulo
    videojuego.genero = genero
    videojuego.desarrollador = desarrollador
    videojuego.fecha_lanzamiento = fecha_lanzamiento
    videojuego.clasificacion = clasificacion
    videojuego.plataforma = Plataforma.objects.get(id=plataforma_id)

    if "logo" in request.FILES:
        nuevo_logo = request.FILES.get("logo")
        if videojuego.logo:
            ruta_logo_antiguo = os.path.join(settings.MEDIA_ROOT, videojuego.logo.name)
            if os.path.isfile(ruta_logo_antiguo):
                os.remove(ruta_logo_antiguo)
        videojuego.logo = nuevo_logo

    if "pdf" in request.FILES:
        nuevo_pdf = request.FILES.get("pdf")
        if videojuego.pdf:
            ruta_pdf_antiguo = os.path.join(settings.MEDIA_ROOT, videojuego.pdf.name)
            if os.path.isfile(ruta_pdf_antiguo):
                os.remove(ruta_pdf_antiguo)
        videojuego.pdf = nuevo_pdf

    videojuego.save()
    messages.success(request, "SE HA EDITADO EL VIDEOJUEGO")

    return redirect('listarVideojuegos')