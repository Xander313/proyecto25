from django.shortcuts import render, redirect
from .models import Visitante
from django.contrib import messages
from django.conf import settings
import os

# Renderizar listado de visitantes
def inicioVisitante(request):
    listadoVisitantes = Visitante.objects.all()
    return render(request, "Visitante/inicioVisitante.html", {'visitantes': listadoVisitantes})

# Renderizar formulario para agregar un nuevo visitante
def nuevoVisitante(request):
    return render(request, "Visitante/nuevoVisitante.html")

# Almacenar datos del visitante en la BD
def guardarVisitante(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        email = request.POST["email"]
        imagen = request.FILES.get("imagen")
        documento = request.FILES.get("documento")

        Visitante.objects.create(
            nombre=nombre, email=email, imagen=imagen, documento=documento
        )

        messages.success(request, "SE HA CREADO EL VISITANTE")
        return redirect('indexVisitante')
    return redirect('indexVisitante')

# Eliminar visitante por ID
def eliminarVisitante(request, id):
    visitanteEliminar = Visitante.objects.get(id=id)

    # Eliminando archivo de imagen si existe
    if visitanteEliminar.imagen:
        ruta_imagen = os.path.join(settings.MEDIA_ROOT, visitanteEliminar.imagen.name)
        if os.path.isfile(ruta_imagen):
            os.remove(ruta_imagen)
    
    # Eliminando archivo de documento si existe
    if visitanteEliminar.documento:
        ruta_documento = os.path.join(settings.MEDIA_ROOT, visitanteEliminar.documento.name)
        if os.path.isfile(ruta_documento):
            os.remove(ruta_documento)
    
    visitanteEliminar.delete()
    messages.success(request, "SE HA ELIMINADO EL VISITANTE")
    return redirect('indexVisitante')

# Renderizar formulario de edición de visitante
def editarVisitante(request, id):
    visitante = Visitante.objects.get(id=id)
    return render(request, "Visitante/editarVisitante.html", {'visitante': visitante})

# Procesar la edición y actualizar en la BD
def procesarEdicionVisitante(request, id):
    nombre = request.POST["nombre"]
    email = request.POST["email"]

    visitante = Visitante.objects.get(id=id)
    visitante.nombre = nombre
    visitante.email = email

    if 'imagen' in request.FILES:
        nueva_imagen = request.FILES.get("imagen")
        if visitante.imagen:
            ruta_imagen_antigua = os.path.join(settings.MEDIA_ROOT, visitante.imagen.name)
            if os.path.isfile(ruta_imagen_antigua):
                os.remove(ruta_imagen_antigua)
        visitante.imagen = nueva_imagen

    if 'documento' in request.FILES:
        nuevo_documento = request.FILES.get("documento")
        if visitante.documento:
            ruta_doc_antiguo = os.path.join(settings.MEDIA_ROOT, visitante.documento.name)
            if os.path.isfile(ruta_doc_antiguo):
                os.remove(ruta_doc_antiguo)
        visitante.documento = nuevo_documento

    visitante.save()
    messages.success(request, "SE HA EDITADO EL VISITANTE")

    return redirect('indexVisitante')
