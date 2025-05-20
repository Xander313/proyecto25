from django.db import models



# Create your models here.
class Genero(models.Model):
    nombre = models.CharField(max_length=255)
    descipcion = models.CharField(max_length=255)
    ejemplares = models.IntegerField()
    aorigen = models.IntegerField()
    autor = models.CharField(max_length=255)



    def _str_(self):
        return self.titulo
