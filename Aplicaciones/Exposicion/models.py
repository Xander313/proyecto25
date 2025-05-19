from django.db import models
from Aplicaciones.AbraArte.models import ObraArte

# Create your models here.
class Exposicion(models.Model):
    nombre = models.CharField(max_length=255)
    fecha = models.DateField()
    sala = models.CharField(max_length=100)
    obras = models.ManyToManyField(ObraArte, related_name="exposiciones")  # Relación M:M con obras

    def _str_(self):
        return self.nombre
