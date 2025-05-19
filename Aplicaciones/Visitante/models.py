from django.db import models

# Create your models here.
class Visitante(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def _str_(self):
        return self.nombre
