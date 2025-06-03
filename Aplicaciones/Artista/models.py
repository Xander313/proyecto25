from django.db import models
from Aplicaciones.Tipo.models import Tipo

class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    edad = models.CharField(max_length=5)
    genero = models.CharField(max_length=10)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)
    imagen = models.FileField(upload_to='Artistas', null=True, blank=True)  # ✅ Nueva imagen del artista
    documento = models.FileField(upload_to='Artistas', null=True, blank=True)  # ✅ Certificación en PDF

    def __str__(self):
        return f"{self.nombre} - {self.pais}"
