from django.shortcuts import render, redirect
from .models import Genero
from django.contrib import messages

def inicioGenero(request):
    listadoObras = Genero.objects.all()
    return render(request, 'inicioGenero.html', {'obras': listadoObras})






def nuevaGenero(request):
    return render(request, "nuevoGenero.html")


def eliminarGenero(request, id):
    obraEliminar = Genero.objects.get(id=id)
    obraEliminar.delete()
    messages.success(request, "SE HA ELIMINADO el genero" )
    return redirect('indexGenero')




def editarGenero(request, id):
    obra = Genero.objects.get(id=id)
    return render(request, "editarGenero.html", {'obra': obra})








def procesarEdicionGenero(request, id):
    nombre = request.POST["nombre"]
    descipcion = request.POST["descipcion"]
    ejemplares = request.POST["ejemplares"]
    aorigen = request.POST["aorigen"]
    autor = request.POST["autor"]



    obra = Genero.objects.get(id=id)
    obra.nombre = nombre
    obra.descipcion = descipcion
    obra.ejemplares = ejemplares

    obra.aorigen = aorigen

    obra.autor = autor
    obra.save()
    messages.success(request, "SE HA EDITADO EL GENERO" )


    return redirect('indexGenero')




def guardarGenero(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        descipcion = request.POST["descipcion"]
        ejemplares = request.POST["ejemplares"]
        aorigen = request.POST["aorigen"]
        autor = request.POST["autor"]

        Genero.objects.create(descipcion=descipcion, nombre=nombre, autor=autor, ejemplares=ejemplares, aorigen=aorigen)
        messages.success(request, "SE HA guardado el genero" )

        return redirect('indexGenero')
    return redirect('indexGenero')  













