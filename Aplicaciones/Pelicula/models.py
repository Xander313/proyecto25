from django.db import models
from Aplicaciones.Genero.models import Genero

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    anio = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    presupuesto = models.DecimalField(max_digits=10, decimal_places=2)
    foto = models.FileField(upload_to='Pelicula', null=True, blank=True)
    documento = models.FileField(upload_to='Pelicula', null=True, blank=True)

    def _str_(self):
        return self.titulo
