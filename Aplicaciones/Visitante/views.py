from django.shortcuts import render, redirect
from .models import Visitante
from django.contrib import messages

# Renderizar listado de visitantes
def inicioVisitante(request):
    listadoVisitantes = Visitante.objects.all()
    return render(request, "Visitante/inicioVisitante.html", {'visitantes': listadoVisitantes})

# Renderizar formulario para agregar un nuevo visitante
def nuevoVisitante(request):
    return render(request, "Visitante/nuevoVisitante.html")

# Almacenar datos del visitante en la BD
def guardarVisitante(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        email = request.POST["email"]

        Visitante.objects.create(nombre=nombre, email=email)
        messages.success(request, "SE HA CREADO EL VISITANTE")

        return redirect('indexVisitante')
    return redirect('indexVisitante')

# Eliminar visitante por ID
def eliminarVisitante(request, id):
    visitanteEliminar = Visitante.objects.get(id=id)
    visitanteEliminar.delete()
    messages.success(request, "SE HA ELIMINADO EL VISITANTE")
    return redirect('indexVisitante')

# Renderizar formulario de edición de visitante
def editarVisitante(request, id):
    visitante = Visitante.objects.get(id=id)
    return render(request, "Visitante/editarVisitante.html", {'visitante': visitante})

# Procesar la edición y actualizar en la BD
def procesarEdicionVisitante(request, id):
    nombre = request.POST["nombre"]
    email = request.POST["email"]

    visitante = Visitante.objects.get(id=id)
    visitante.nombre = nombre
    visitante.email = email
    visitante.save()
    messages.success(request, "SE HA EDITADO EL VISITANTE")

    return redirect('indexVisitante')
