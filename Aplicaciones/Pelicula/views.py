from django.shortcuts import render, redirect
from Aplicaciones.Genero.models import Genero
from .models import Pelicula
from django.contrib import messages



# Create your views here.

def inicioPelicula(request):
    listadoObras = Pelicula.objects.all()
    return render(request, 'inicioPelicula.html', {'obras': listadoObras})



def guardarPelicula(request):
    if request.method == "POST":


        titulo = request.POST["titulo"]
        autor = request.POST["autor"]
        anio = request.POST["anio"]



        generoid = request.POST["genero"]



        presupuesto = request.POST["presupuesto"].replace(',','.')

        
        genero = Genero.objects.get(id=generoid)

        Pelicula.objects.create(
            titulo=titulo,
            autor=autor,
            anio=anio,
            genero=genero,
            presupuesto=presupuesto

        )




        messages.success(request, "pelicula creada exitosamente!")
        return redirect('indexPelicula')
    
    return redirect('indexPelicula')





def nuevaPelicula(request):
    genreos = Genero.objects.all()
    return render(request, "nuevoPelicula.html", {
        'genero': genreos,
    })






def eliminarPelicula(request, id):
    obraEliminar = Pelicula.objects.get(id=id)
    obraEliminar.delete()
    messages.success(request, "SE HA ELIMINADO pelicula ")
    return redirect('indexPelicula')






def editarPelicula(request, id):
    obra = Pelicula.objects.get(id=id)
    genero = Genero.objects.all()
    presup = obra.presupuesto
    print(presup)
    return render(request, "editarPelicula.html", {
        'obra': obra,
        'genero': genero,
        'presformat': str(presup)})



def procesarEdicionPelicula(request, id):

    titulo = request.POST["titulo"]
    autor = request.POST["autor"]
    anio = request.POST["anio"]
    generoid=request.POST["genero"]
    genero = Genero.objects.get(id=generoid)
    presupuesto = request.POST["presupuesto"].replace(',','.')


    obra = Pelicula.objects.get(id=id)
    obra.titulo = titulo
    obra.anio = anio
    obra.genero = genero
    obra.presupuesto = presupuesto
    obra.autor = autor
    obra.save()
    messages.success(request, "SE HA EDITADO la pelicula" )


    return redirect('indexPelicula')










