from django.db import models

# Create your models here.
class Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=255)
    anio = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)
    popularidad = models.IntegerField()