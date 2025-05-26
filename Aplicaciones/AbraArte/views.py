from django.shortcuts import render, redirect
from .models import ObraArte
from django.contrib import messages

# Renderizar listado de obras de arte
def inicioArte(request):
    listadoObras = ObraArte.objects.all()

    return render(request, "AbraArte/inicioArte.html", {'obras': listadoObras})

# Renderizar formulario para agregar una nueva obra de arte
def nuevaArte(request):
    return render(request, "AbraArte/nuevoArte.html")

# Almacenar datos de la obra en la BD
def guardarArte(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        autor = request.POST["autor"]
        anio = request.POST["anio"]

        ObraArte.objects.create(titulo=titulo, autor=autor, anio=anio)
        messages.success(request, "SE HA AGREGADO LA OBRA" )

        return redirect('indexArte')
    return redirect('indexArte')  

# Eliminar obra de arte por ID
def eliminarArte(request, id):
    obraEliminar = ObraArte.objects.get(id=id)
    obraEliminar.delete()
    messages.success(request, "SE HA ELIMINADO LA OBRA" )
    return redirect('indexArte')

# Renderizar formulario de edición de obra de arte
def editarArte(request, id):
    obra = ObraArte.objects.get(id=id)
    return render(request, "AbraArte/editarArte.html", {'obra': obra})

# Procesar la edición y actualizar en la BD
def procesarEdicionArte(request, id):
    titulo = request.POST["titulo"]
    autor = request.POST["autor"]
    anio = request.POST["anio"]

    obra = ObraArte.objects.get(id=id)
    obra.titulo = titulo
    obra.autor = autor
    obra.anio = anio
    obra.save()
    messages.success(request, "SE HA EDITADO LA OBRA" )


    return redirect('indexArte')
