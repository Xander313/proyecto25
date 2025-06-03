from django.shortcuts import render, redirect
from Aplicaciones.Genero.models import Genero
from .models import Pelicula
from django.contrib import messages
import os
from django.conf import settings



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
        foto = request.FILES.get("foto")
        documento = request.FILES.get("documento")
        genero = Genero.objects.get(id=generoid)

        Pelicula.objects.create(
            titulo=titulo,
            autor=autor,
            anio=anio,
            genero=genero,
            presupuesto=presupuesto,
            foto = foto,
            documento = documento
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

    if 'foto' in request.FILES:
        nueva_foto = request.FILES.get("foto")
        if obraEliminar.foto:
            ruta_foto_antiguo = os.path.join(settings.MEDIA_ROOT, obraEliminar.foto.name)
            if os.path.isfile(ruta_foto_antiguo):
                os.remove(ruta_foto_antiguo)
    if 'documento' in request.FILES:
        nuevo_documento = request.FILES.get("documento")
        if obraEliminar.documento:
            ruta_doc_antiguo = os.path.join(settings.MEDIA_ROOT, obraEliminar.documento.name)
            if os.path.isfile(ruta_doc_antiguo):
                os.remove(ruta_doc_antiguo)
    obraEliminar.delete()
    messages.success(request, "SE HA ELIMINADO pelicula ")
    return redirect('indexPelicula')






def editarPelicula(request, id):
    obra = Pelicula.objects.get(id=id)
    genero = Genero.objects.all()
    presup = obra.presupuesto


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

    if 'foto' in request.FILES:
        nueva_foto = request.FILES.get("foto")
        if obra.foto:
            ruta_foto_antiguo = os.path.join(settings.MEDIA_ROOT, obra.foto.name)
            if os.path.isfile(ruta_foto_antiguo):
                os.remove(ruta_foto_antiguo)
        obra.foto = nueva_foto
    if 'documento' in request.FILES:
        nuevo_documento = request.FILES.get("documento")
        if obra.documento:
            ruta_doc_antiguo = os.path.join(settings.MEDIA_ROOT, obra.documento.name)
            if os.path.isfile(ruta_doc_antiguo):
                os.remove(ruta_doc_antiguo)
        obra.documento = nuevo_documento


    obra.save()
    messages.success(request, "SE HA EDITADO la pelicula" )


    return redirect('indexPelicula')










