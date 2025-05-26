from django.db import models
from Aplicaciones.Genero.models import Genero

# Create your models here.
class Pelicula(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    anio = models.IntegerField()
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    presupuesto = models.CharField()


    def _str_(self):
        return self.titulo
