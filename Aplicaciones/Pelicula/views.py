from django.shortcuts import render, redirect
from Aplicaciones.Genero.models import Genero
from .models import Pelicula
from django.contrib import messages



# Create your views here.

def inicioPelicula(request):
    listadoObras = Pelicula.objects.all()
    return render(request, 'Pelicula/iniciPelicula.html', {'obras': listadoObras})



def nuevaPelicula(request):

    genreos = Pelicula.objects.all()
    
    return render(request, "Reserva/nuevaReserva.html", {
        'genero': genreos,
    })


def eliminarPelicula(request, id):
    obraEliminar = Pelicula.objects.get(id=id)
    obraEliminar.delete()
    messages.success(request, "SE HA ELIMINADO el genero" )
    return redirect('indexGenero')






def editarPelicula(request, id):
    obra = Pelicula.objects.get(id=id)
    genero = Genero.objects.all()
    return render(request, "Reserva/editarReserva.html", {
        'reserva': obra,
        'genero': genero})



def procesarEdicionPelicula(request, id):
    titulo = request.POST["titulo"]
    autor = request.POST["autor"]
    anio = request.POST["anio"]
    genero = Genero.objects.get(id=request.POST["genero"])

    presupuesto = request.POST["presupuesto"]


    obra = Pelicula.objects.get(id=id)
    obra.titulo = titulo
    obra.anio = anio
    obra.genero = genero
    obra.presupuesto = presupuesto
    obra.autor = autor
    obra.save()
    messages.success(request, "SE HA EDITADO EL GENERO" )


    return redirect('indexGenero')










