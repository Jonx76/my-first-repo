from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def saludo(request):
    fecha = datetime.now()
    return HttpResponse(f"Hola mundo {fecha}")


def saludar_a(request, nombre):
    return HttpResponse(f"Hola, como estas {nombre.capitalize()}?")



def saludo_personalizado(request):  
    context = {}

    if request.GET:
        context["nombre"] = request.GET["nombre"]

    return render(request, "AppCoder/index.html", context) 


def listar_cursos(request):
    context = {}

    context["cursos"] = Curso.objects.all(),

    return render(request, "AppCoder/listar_cursos.html", context)

def listar_estudiantes(request):
    context = {

        "estudiantes": Estudiante.objects.all(),
    }
    return render(request, "AppCoder/estudiantes.html", context)