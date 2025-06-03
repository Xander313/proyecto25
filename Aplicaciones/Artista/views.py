from django.shortcuts import render, redirect
from .models import Artista, Tipo
from django.contrib import messages
from django.conf import settings
from django.conf.urls.static import static
import os

# Renderizar listado de artistas
def listarArtistas(request):
    artistas = Artista.objects.select_related('tipo').all()  # Optimización con select_related
    return render(request, "Artista/inicioArtista.html", {'artistas': artistas})

# Renderizar formulario para agregar un nuevo artista
def nuevoArtista(request):
    tipos = Tipo.objects.all()  # Obtener todos los tipos disponibles
    return render(request, "Artista/nuevoArtista.html", {'tipos': tipos})

# Almacenar datos del artista en la BD
def guardarArtista(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        pais = request.POST["pais"]
        telefono = request.POST["telefono"]
        edad = request.POST["edad"]
        genero = request.POST["genero"]
        tipo_id = request.POST["tipo"]

        imagen = request.FILES.get("imagen")
        documento = request.FILES.get("documento")

        tipo = Tipo.objects.get(id=tipo_id)
        Artista.objects.create(
            nombre=nombre, pais=pais, telefono=telefono, edad=edad, genero=genero, tipo=tipo,
            imagen=imagen, documento=documento
        )

        messages.success(request, "SE HA AGREGADO EL ARTISTA")
        return redirect('listarArtistas')
    return redirect('listarArtistas')

# Eliminar artista por ID
def eliminarArtista(request, id):
    artistaEliminar = Artista.objects.get(id=id)

    if artistaEliminar.imagen:
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, artistaEliminar.imagen.name)
        if os.path.isfile(ruta_imagen):
            os.remove(ruta_imagen)
    
    if artistaEliminar.documento:
        ruta_documento = os.path.join(settings.MEDIA_ROOT, artistaEliminar.documento.name)
        if os.path.isfile(ruta_documento):
            os.remove(ruta_documento)
    
    artistaEliminar.delete()
    messages.success(request, "SE HA ELIMINADO EL ARTISTA")
    return redirect('listarArtistas')

# Renderizar formulario de edición de artista
def editarArtista(request, id):
    artista = Artista.objects.get(id=id)
    tipos = Tipo.objects.all()  # Obtener todos los tipos disponibles
    return render(request, "Artista/editarArista.html", {'artista': artista, 'tipos': tipos})

# Procesar la edición y actualizar en la BD
def procesarEdicionArtista(request, id):
    nombre = request.POST["nombre"]
    pais = request.POST["pais"]
    telefono = request.POST["telefono"]
    edad = request.POST["edad"]
    genero = request.POST["genero"]
    tipo_id = request.POST["tipo"]

    artista = Artista.objects.get(id=id)
    artista.nombre = nombre
    artista.pais = pais
    artista.telefono = telefono
    artista.edad = edad
    artista.genero = genero
    artista.tipo = Tipo.objects.get(id=tipo_id)  # Actualizar la relación con Tipo

    if 'imagen' in request.FILES:
        nueva_imagen = request.FILES.get("imagen")
        if artista.imagen:
            ruta_imagen_antigua = os.path.join(settings.MEDIA_ROOT, artista.imagen.name)
            if os.path.isfile(ruta_imagen_antigua):
                os.remove(ruta_imagen_antigua)
        artista.imagen = nueva_imagen

    if 'documento' in request.FILES:
        nuevo_documento = request.FILES.get("documento")
        if artista.documento:
            ruta_doc_antiguo = os.path.join(settings.MEDIA_ROOT, artista.documento.name)
            if os.path.isfile(ruta_doc_antiguo):
                os.remove(ruta_doc_antiguo)
        artista.documento = nuevo_documento

    artista.save()
    messages.success(request, "SE HA EDITADO EL ARTISTA")

    return redirect('listarArtistas')
