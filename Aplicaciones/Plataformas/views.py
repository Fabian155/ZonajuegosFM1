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

def GuardarEdicion(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    especialidad=request.POST["especialidad"]
    experiencia=request.POST["experiencia"]
    contacto=request.POST["contacto"]
    nacionalidad=request.POST["nacionalidad"].replace(',','.')

    editalo=Instructor.objects.get(id=id)

    editalo.nombre=nombre
    editalo.especialidad=especialidad
    editalo.experiencia=experiencia
    editalo.contacto=contacto
    editalo.nacionalidad=nacionalidad
    editalo.save()
    messages.success(request, "Actualizacion Completa")
    return redirect('/')
