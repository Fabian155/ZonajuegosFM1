from django.shortcuts import render, redirect
from .models import Videojuego
from Aplicaciones.Plataformas.models import Plataforma
from django.shortcuts import get_object_or_404
from django.contrib import messages

# Create your views here.

def inicio1(request):
    listaJuegos=Videojuego.objects.all()
    return render(request, "inicio1.html", {'Juegos': listaJuegos})


def nuevoCurso(request):
    instructores=Instructor.objects.all()
    return render(request, "nuevoCurso.html", {'instructores': instructores})

def GuardarC(request):
    nombre=request.POST["nombre"]
    descripcion=request.POST["descripcion"]
    dificultad=request.POST["dificultad"]
    duracion=request.POST["duracion"]
    lugar=request.POST["lugar"]
    instructor_id = request.POST['instructor']
    instructor = Instructor.objects.get(id=instructor_id)
    nuevoCurso=Curso.objects.create(nombre=nombre, descripcion=descripcion, dificultad=dificultad, duracion=duracion, lugar=lugar, instructor=instructor)
    messages.success(request, "CURSO GUARDADO")
    return redirect('/')

def EliminarCurso(request, id):
    EliminarC=Curso.objects.get(id=id)
    EliminarC.delete()
    return redirect('/')


def editaCurso(request, id):
    editarCur=get_object_or_404(Curso, id=id)
    instructores=Instructor.objects.all()
    return render(request, "editaCurso.html", {'editaC': editarCur, 'instructores': instructores})

def GuardarEdicion2(request):
    id=request.POST["id"]
    nombre=request.POST["nombre"]
    descripcion=request.POST["descripcion"]
    dificultad=request.POST["dificultad"]
    duracion=request.POST["duracion"]
    lugar=request.POST["lugar"]
    instructor_id = request.POST['instructor'].replace(',','.')

    editalos=Curso.objects.get(id=id)

    editalos.nombre=nombre
    editalos.descripcion=descripcion
    editalos.dificultad=dificultad
    editalos.duracion=duracion
    editalos.lugar=lugar
    editalos.instructor = Instructor.objects.get(id=instructor_id)
    editalos.save()
    messages.success(request, "Actualizacion Completa")
    return redirect('/')