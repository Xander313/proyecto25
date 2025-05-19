from django.db import models
from Aplicaciones.Visitante.models import Visitante
from Aplicaciones.Exposicion.models import Exposicion

# Create your models here.
class Reserva(models.Model):
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)  # Relación 1:M con Visitante
    exposicion = models.ForeignKey(Exposicion, on_delete=models.CASCADE)  # Relación 1:M con Exposición
    fecha_reserva = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.visitante} - {self.exposicion}"