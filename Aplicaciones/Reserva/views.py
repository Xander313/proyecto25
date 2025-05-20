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

        visitante = Visitante.objects.get(id=visitante_id)
        exposicion = Exposicion.objects.get(id=exposicion_id)

        Reserva.objects.create(
            visitante=visitante,
            exposicion=exposicion
        )

        messages.success(request, "¡Reserva creada exitosamente!")
        return redirect('indexReserva')
    
    return redirect('indexReserva')