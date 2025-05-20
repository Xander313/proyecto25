from django.shortcuts import render, redirect
from .models import ObraArte

# Renderizar listado de obras de arte
def inicioArte(request):
    listadoObras = ObraArte.objects.all()
    return render(request, "AbraArte/inicioArte.html", {'obras': listadoObras})

# Renderizar formulario para agregar una nueva obra de arte
def nuevaArte(request):
    return render(request, "ObraArte/nuevoArte.html")

# Almacenar datos de la obra en la BD
def guardarArte(request):
    if request.method == "POST":
        titulo = request.POST["titulo"]
        autor = request.POST["autor"]
        anio = request.POST["anio"]

        ObraArte.objects.create(titulo=titulo, autor=autor, anio=anio)
        return redirect('/inicioArte/')
    return redirect('/nuevoArte/')  

# Eliminar obra de arte por ID
def eliminarArte(request, id):
    obraEliminar = ObraArte.objects.get(id=id)
    obraEliminar.delete()
    return redirect('/inicioArte/')

# Renderizar formulario de edición de obra de arte
def editarArte(request, id):
    obra = ObraArte.objects.get(id=id)
    return render(request, "ObraArte/editarArte.html", {'obra': obra})

# Procesar la edición y actualizar en la BD
def procesarEdicionArte(request):
    id = request.POST["id"]
    titulo = request.POST["titulo"]
    autor = request.POST["autor"]
    anio = request.POST["anio"]

    obra = ObraArte.objects.get(id=id)
    obra.titulo = titulo
    obra.autor = autor
    obra.anio = anio
    obra.save()
    
    return redirect('/inicioArte/')
