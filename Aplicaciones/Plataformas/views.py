from django.shortcuts import render, redirect
from .models import Plataforma
from django.contrib import messages

# Create your views here.

def inicio2(request):
    listaPlataforma=Plataforma.objects.all()
    return render(request, "inicio2.html", {'Plataformas': listaPlataforma})


def nuevaPlataforma(request):
    return render(request, "nuevaPlataforma.html")

def Guardar(request):
    nombre=request.POST["nombre"]
    fabricante=request.POST["especialidad"]
    anio_lanzamiento=request.POST["experiencia"]
    tipo=request.POST["contacto"]
    region_disponible=request.POST["nacionalidad"]

    logo=request.FILES.get("logo")
    pdf = request.FILES.get("pdf")

    nuevaplataforma=Plataforma.objects.create(nombre=nombre, fabricante=fabricante, anio_lanzamiento=anio_lanzamiento, tipo=tipo, region_disponible=region_disponible, logo=logo, pdf=pdf)
    messages.success(request, "INSTRUCTOR GUARDADO")
    return redirect('/')

def EliminarPlataforma(request, id):
    EliminarP=Plataforma.objects.get(id=id)
    EliminarP.delete()
    return redirect('/')


def editarPlataforma(request, id):
    editarPLA=Plataforma.objects.get(id=id)
    return render(request, "editarPlataforma.html", {'editarP': editarPLA})

def GuardarEdicion2(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    fabricante=request.POST["especialidad"]
    anio_lanzamiento=request.POST["experiencia"]
    tipo=request.POST["contacto"]
    region_disponible=request.POST["nacionalidad"].replace(',','.')

    editele=Plataforma.objects.get(id=id)
    nuevo_logo = request.FILES.get("logo")
    nuevo_pdf = request.FILES.get("pdf")

    editele.nombre=nombre
    editele.fabricante=fabricante
    editele.anio_lanzamiento=anio_lanzamiento
    editele.tipo=tipo
    editele.region_disponible=region_disponible
    if nuevo_logo:
        editele.logo = nuevo_logo
    if nuevo_pdf:
        editele.pdf = nuevo_pdf
    editele.save()
    messages.success(request, "Actualizacion Completa")
    return redirect('/')
