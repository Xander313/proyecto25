from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Exposicion, ObraArte

# Create your views here.


# Renderizar listado de exposiciones
def inicioExposicion(request):
    listadoExposiciones = Exposicion.objects.all()
    return render(request, "Exposicion/inicioExposicion.html", {'exposiciones': listadoExposiciones})

# Renderizar formulario para agregar una nueva exposición con las obras disponibles
def nuevaExposicion(request):
    obras = ObraArte.objects.all()  
    return render(request, "Exposicion/nuevaExposicion.html", {"obras": obras})

# Almacenar datos de la exposición en la BD con selección de obras
def guardarExposicion(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        fecha = request.POST["fecha"]
        sala = request.POST["sala"]
        obras_seleccionadas = request.POST.getlist("obras")  





        exposicion = Exposicion.objects.create(nombre=nombre, fecha=fecha, sala=sala, )
        exposicion.obras.set(obras_seleccionadas)  
        messages.success(request, "SE HA CREADO LA EXPOSICIÓN")

        return redirect('indexExposicion')
    return redirect('indexExposicion')

# Eliminar exposición por ID
def eliminarExposicion(request, id):
    exposicionEliminar = Exposicion.objects.get(id=id)
    exposicionEliminar.delete()
    messages.success(request, "SE HA ELIMINADO LA EXPOSICIÓN")
    return redirect('indexExposicion')

# Renderizar formulario de edición de exposición con obras asociadas
def editarExposicion(request, id):
    exposicion = Exposicion.objects.get(id=id)
    obras = ObraArte.objects.all()  
    obras_seleccionadas = exposicion.obras.all()  # Obtener las obras ya asociadas

    return render(
        request, 
        "Exposicion/editarExposicion.html", 
        {"exposicion": exposicion, "obras": obras, "obras_seleccionadas": obras_seleccionadas}
    )

# Procesar la edición y actualizar en la BD, incluyendo obras seleccionadas
def procesarEdicionExposicion(request, id):
    nombre = request.POST["nombre"]
    fecha = request.POST["fecha"]
    sala = request.POST["sala"]
    obras_seleccionadas = request.POST.getlist("obras")  

    exposicion = Exposicion.objects.get(id=id)
    exposicion.nombre = nombre
    exposicion.fecha = fecha
    exposicion.sala = sala
    exposicion.obras.set(obras_seleccionadas)  
    exposicion.save()
    messages.success(request, "SE HA EDITADO LA EXPOSICIÓN")

    return redirect('indexExposicion')

