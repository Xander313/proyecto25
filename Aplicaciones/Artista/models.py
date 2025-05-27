from django.db import models

# Create your models here.
class Artista(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    pais = models.CharField(max_length=30)
    telefono = models.CharField(max_length=10)
    edad = models.CharField(max_length=5)
    genero = models.CharField(max_length=10)
    tipo = models.ForeignKey(Tipo, on_delete=models.CASCADE)  # Relación directa
