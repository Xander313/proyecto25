from django.shortcuts import render, redirect
from .models import Reserva
from Aplicaciones.Visitante.models import Visitante
from Aplicaciones.Exposicion.models import Exposicion
from django.contrib import messages
import os
from django.conf import settings

# Create your views here.
def indexReserva(request):
    reservas = Reserva.objects.all()
    return render(request, 'Reserva/inicioReserva.html', {'reservas': reservas})

def nuevaReserva(request):
    visitantes = Visitante.objects.all()
    exposiciones = Exposicion.objects.all()
    
    return render(request, "Reserva/nuevaReserva.html", {
        'visitantes': visitantes,
        'exposiciones': exposiciones
    })


def guardarReserva(request):
    if request.method == "POST":
        visitante_id = request.POST["visitante"]
        exposicion_id = request.POST["exposicion"]
        observaciones = request.POST["observaciones"]
        fecha = request.POST["fecha"]

        visitante = Visitante.objects.get(id=visitante_id)
        exposicion = Exposicion.objects.get(id=exposicion_id)

        foto = request.FILES.get("foto")
        documento = request.FILES.get("documento")

        Reserva.objects.create(
            visitante=visitante,
            exposicion=exposicion,
            fecha_reserva = fecha,
            observaciones = observaciones,
            foto = foto,
            documento = documento
        )

        messages.success(request, "¡Reserva creada exitosamente!")
        return redirect('indexReserva')
    
    return redirect('indexReserva')


def eliminarReserva(request, id):
    obraEliminar = Reserva.objects.get(id=id)
    obra_foto = os.path.join(settings.MEDIA_ROOT, obraEliminar.foto.name)
    if os.path.isfile(obra_foto):
        os.remove(obra_foto)
    
    obra_documento = os.path.join(settings.MEDIA_ROOT, obraEliminar.documento.name)
    if os.path.isfile(obra_documento):
        os.remove(obra_documento)
    obraEliminar.delete()
    messages.success(request, "SE HA ELIMINADO LA RESERVA" )
    return redirect('indexReserva')



def editarReserva(request, id):
    reserva = Reserva.objects.get(id=id)
    visitantes = Visitante.objects.all()
    exposiciones = Exposicion.objects.all()
    return render(request, "Reserva/editarReserva.html", {
        'reserva': reserva,
        'visitantes': visitantes,
        'exposiciones': exposiciones
    })



def procesarEdicionReserva(request, id):
    if request.method == "POST":
        visitante = Visitante.objects.get(id=request.POST['visitante'])
        exposicion = Exposicion.objects.get(id=request.POST['exposicion'])
        observaciones = request.POST["observaciones"]
        fecha = request.POST["fecha"]

        reserva = Reserva.objects.get(id=id)
        reserva.visitante = visitante
        reserva.exposicion = exposicion
        reserva.fecha_reserva = fecha
        reserva.observaciones = observaciones

        if 'foto' in request.FILES:
                nueva_foto = request.FILES.get("foto")

                if reserva.foto:
                    ruta_foto_antiguo = os.path.join(settings.MEDIA_ROOT, reserva.foto.name)
                    if os.path.isfile(ruta_foto_antiguo):
                        os.remove(ruta_foto_antiguo)

                reserva.foto = nueva_foto

        if 'documento' in request.FILES:
            nuevo_documento = request.FILES.get("documento")
            if reserva.documento:
                ruta_doc_antiguo = os.path.join(settings.MEDIA_ROOT, reserva.documento.name)
                if os.path.isfile(ruta_doc_antiguo):
                    os.remove(ruta_doc_antiguo)
            reserva.documento = nuevo_documento



        reserva.save()

        messages.success(request, "¡Reserva actualizada correctamente!")
    return redirect('indexReserva')