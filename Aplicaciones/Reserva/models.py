from django.db import models
from Aplicaciones.Visitante.models import Visitante
from Aplicaciones.Exposicion.models import Exposicion

# Create your models here.
class Reserva(models.Model):
    visitante = models.ForeignKey(Visitante, on_delete=models.CASCADE)  
    exposicion = models.ForeignKey(Exposicion, on_delete=models.CASCADE)  
    fecha_reserva = models.DateTimeField()
    observaciones = models.TextField(default="")
    foto = models.FileField(upload_to="Reserva", null=True, blank=True)
    documento = models.FileField(upload_to="Reserva", null=True, blank=True)


    def _str_(self):
        return f"{self.visitante} - {self.exposicion}"