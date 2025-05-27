from django.shortcuts import render, redirect
from .models import Tipo
from django.contrib import messages

# Listar todos los tipos
def listarTipos(request):
    tipos = Tipo.objects.all()
    return render(request, "Tipo/inicioTipo.html", {'tipos': tipos})

# Mostrar formulario para agregar un nuevo tipo
def nuevoTipo(request):
    return render(request, "Tipo/nuevoTipo.html")

# Guardar nuevo tipo en la BD
def guardarTipo(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        anio = request.POST["anio"]
        genero = request.POST["genero"]
        popularidad = request.POST["popularidad"]

        Tipo.objects.create(nombre=nombre, descripcion=descripcion, anio=anio, genero=genero, popularidad=popularidad)
        messages.success(request, "SE HA AGREGADO EL TIPO")

        return redirect('listarTipos')
    return redirect('listarTipos')

# Eliminar un tipo por ID
def eliminarTipo(request, id):
    tipoEliminar = Tipo.objects.get(id=id)
    tipoEliminar.delete()
    messages.success(request, "SE HA ELIMINADO EL TIPO")
    return redirect('listarTipos')

# Mostrar formulario de edición para un tipo
def editarTipo(request, id):
    tipo = Tipo.objects.get(id=id)
    return render(request, "Tipo/editarTipo.html", {'tipo': tipo})

# Procesar edición del tipo y guardar cambios en la BD
def procesarEdicionTipo(request, id):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        descripcion = request.POST["descripcion"]
        anio = request.POST["anio"]
        genero = request.POST["genero"]
        popularidad = request.POST["popularidad"]

        tipo = Tipo.objects.get(id=id)
        tipo.nombre = nombre
        tipo.descripcion = descripcion
        tipo.anio = anio
        tipo.genero = genero
        tipo.popularidad = popularidad
        tipo.save()
        messages.success(request, "SE HA EDITADO EL TIPO")

    return redirect('listarTipos')
