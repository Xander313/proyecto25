from django.shortcuts import render, redirect
from .models import Artista, Tipo
from django.contrib import messages

# Listar todos los artistas con su tipo asociado
def listarArtistas(request):
    artistas = Artista.objects.select_related('tipo').all()  # Optimización con select_related
    return render(request, "Artistas/listarArtistas.html", {'artistas': artistas})

# Mostrar formulario para agregar un nuevo artista
def nuevoArtista(request):
    tipos = Tipo.objects.all()  # Obtener todos los tipos disponibles
    return render(request, "Artistas/nuevoArtista.html", {'tipos': tipos})

# Guardar nuevo artista en la BD con su tipo asociado
def guardarArtista(request):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        pais = request.POST["pais"]
        telefono = request.POST["telefono"]
        edad = request.POST["edad"]
        genero = request.POST["genero"]
        tipo_id = request.POST["tipo"]  # Recibir el ID del tipo seleccionado

        tipo = Tipo.objects.get(id=tipo_id)
        Artista.objects.create(nombre=nombre, pais=pais, telefono=telefono, edad=edad, genero=genero, tipo=tipo)
        messages.success(request, "SE HA AGREGADO EL ARTISTA")

        return redirect('listarArtistas')
    return redirect('listarArtistas')

# Eliminar un artista por ID
def eliminarArtista(request, id):
    artistaEliminar = Artista.objects.get(id=id)
    artistaEliminar.delete()
    messages.success(request, "SE HA ELIMINADO EL ARTISTA")
    return redirect('listarArtistas')

# Mostrar formulario de edición para un artista, incluyendo su tipo
def editarArtista(request, id):
    artista = Artista.objects.get(id=id)
    tipos = Tipo.objects.all()  # Obtener todos los tipos disponibles
    return render(request, "Artistas/editarArtista.html", {'artista': artista, 'tipos': tipos})

# Procesar edición del artista y actualizar su tipo asociado
def procesarEdicionArtista(request, id):
    if request.method == "POST":
        nombre = request.POST["nombre"]
        pais = request.POST["pais"]
        telefono = request.POST["telefono"]
        edad = request.POST["edad"]
        genero = request.POST["genero"]
        tipo_id = request.POST["tipo"]  # Nuevo tipo seleccionado

        tipo = Tipo.objects.get(id=tipo_id)
        artista = Artista.objects.get(id=id)
        artista.nombre = nombre
        artista.pais = pais
        artista.telefono = telefono
        artista.edad = edad
        artista.genero = genero
        artista.tipo = tipo  # Actualizar relación
        artista.save()
        messages.success(request, "SE HA EDITADO EL ARTISTA")

    return redirect('listarArtistas')
