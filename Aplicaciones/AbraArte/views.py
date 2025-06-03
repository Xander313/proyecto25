from django.shortcuts import render, redirect
from .models import ObraArte
from django.contrib import messages
from django.conf import settings
from django.conf.urls.static import static
import os

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

        foto = request.FILES.get("foto")
        documento = request.FILES.get("documento")

        ObraArte.objects.create(titulo=titulo, autor=autor, anio=anio, foto=foto, documento = documento)
        messages.success(request, "SE HA AGREGADO LA OBRA" )

        return redirect('indexArte')
    return redirect('indexArte')  

# Eliminar obra de arte por ID
def eliminarArte(request, id):
    obraEliminar = ObraArte.objects.get(id=id)

    obra_foto = os.path.join(settings.MEDIA_ROOT, obraEliminar.foto.name)
    if os.path.isfile(obra_foto):
        os.remove(obra_foto)
    
    obra_documento = os.path.join(settings.MEDIA_ROOT, obraEliminar.documento.name)
    if os.path.isfile(obra_documento):
        os.remove(obra_documento)
    
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
    messages.success(request, "SE HA EDITADO LA OBRA" )


    return redirect('indexArte')
