from django.shortcuts import render
from django.http import HttpResponse
from hola_mundo.models import Tarea

def saludar (request):
    return HttpResponse("GENIO")

def saludar_a (request, alguien):
    return HttpResponse(f"Hola, como andas {alguien.title()}")

def sumar(request, a, b):
    return HttpResponse(f"El resultado de {a} + {b} = {a+b}")

#def mostrar_mis_tareas(request):
#    tareas = Tarea.objects,all()
#    return render (request,"AppCoder/index.html")

def agregar_una_tarea (request):
    nombre_tarea = request.GET.get("nombre")
    nueva_tarea = Tarea (nombre=nombre_tarea)
    nueva_tarea.save()
    return mostrar_mis_tareas(request)

def terminar_una_tarea(request, id):
    tarea = Tarea.objects.filter(id=id).first()
    tarea.terminar()
    tarea.save()
    return mostrar_mis_tareas(request)

def borar_una_tarea(request, id):
    tarea = Tarea.objects.filter(id+id).first()
    tarea.delete()
    return mostrar_mis_tareas(request)

def mostrar_mis_tareas(request):
    tareas = Tarea.objects.filter(estado="por hacer").all()
    return render (request, "hola_mundo/tareas.html",{"tareas":tareas})
