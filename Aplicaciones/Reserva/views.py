from django.shortcuts import render, redirect
from .models import Reserva
from Aplicaciones.Visitante.models import Visitante
from Aplicaciones.Exposicion.models import Exposicion
from django.contrib import messages

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

        Reserva.objects.create(
            visitante=visitante,
            exposicion=exposicion,
            fecha_reserva = fecha,
            observaciones = observaciones
        )

        messages.success(request, "¡Reserva creada exitosamente!")
        return redirect('indexReserva')
    
    return redirect('indexReserva')


def eliminarReserva(request, id):
    obraEliminar = Reserva.objects.get(id=id)
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

        reserva = Reserva.objects.get(id=id)
        reserva.visitante = visitante
        reserva.exposicion = exposicion
        reserva.save()

        messages.success(request, "¡Reserva actualizada correctamente!")
    return redirect('indexReserva')