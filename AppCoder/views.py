from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def saludo(request):
    fecha = datetime.now()
    return HttpResponse(f"Hola mundo {fecha}")


def saludar_a(request, nombre):
    return HttpResponse(f"Hola, como estas {nombre.capitalize()}?")