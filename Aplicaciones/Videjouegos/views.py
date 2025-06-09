from django.shortcuts import render, redirect
from .models import Videojuego
from Aplicaciones.Plataformas.models import Plataforma
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.

def inicio1(request):
    listaJuegos=Videojuego.objects.all()
    return render(request, "inicio1.html", {'Juegos': listaJuegos})


def NuevoJuego(request):
    plataformas=Plataforma.objects.all()
    return render(request, "NuevoJuego.html", {'plataformas': plataformas})

def GuardarJ(request):
    titulo=request.POST["titulo"]
    genero=request.POST["genero"]
    desarrollador=request.POST["desarollador"]
    fecha_lanzamiento =request.POST["fecha_lanzamiento"]
    clasificacion=request.POST["clasificacion"]
    plataforma_id = request.POST['plataforma']
    plataforma = Plataforma.objects.get(id=plataforma_id)

    logo=request.FILES.get("logo")
    pdf = request.FILES.get("pdf")

    nuevaPLata=Videojuego.objects.create(titulo=titulo, genero=genero, desarrollador=desarrollador, fecha_lanzamiento=fecha_lanzamiento, clasificacion=clasificacion, plataforma=plataforma, logo=logo, pdf=pdf)
    messages.success(request, " GUARDADO CORRECTA MENTE")
    return redirect('/')

def EliminarJuego(request, id):
    EliminarJ=Videojuego.objects.get(id=id)
    EliminarJ.delete()
    return redirect('/')


def editarJuego(request, id):
    editalJuego=get_object_or_404(Videojuego, id=id)
    plataformas=Plataforma.objects.all()
    return render(request, "editarJuego.html", {'editarJ': editalJuego, 'plataformas': plataformas})

def GuardarEdicion1(request):
    id=request.POST["id"]
    titulo=request.POST["titulo"]
    genero=request.POST["genero"]
    desarrollador=request.POST["desarollador"]
    fecha_lanzamiento =request.POST["fecha_lanzamiento"]
    clasificacion=request.POST["clasificacion"]
    plataforma_id = request.POST['plataforma'].replace(',','.')

    editalos=Videojuego.objects.get(id=id)
    nuevo_logo = request.FILES.get("logo")
    nuevo_pdf = request.FILES.get("pdf")

    editalos.titulo=titulo
    editalos.genero=genero
    editalos.desarrollador=desarrollador
    editalos.fecha_lanzamiento=fecha_lanzamiento
    editalos.clasificacion=clasificacion
    editalos.plataforma = Plataforma.objects.get(id=plataforma_id)
    if nuevo_logo:
        editalos.logo = nuevo_logo
    if nuevo_pdf:
        editalos.pdf = nuevo_pdf
    editalos.save()
    messages.success(request, "Actualizacion Completa")
    return redirect('/')