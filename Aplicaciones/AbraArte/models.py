from django.db import models

# Create your models here.
class ObraArte(models.Model):
    titulo = models.CharField(max_length=255)
    autor = models.CharField(max_length=255)
    anio = models.IntegerField()
    foto = models.FileField(upload_to='AbraArte', null=True, blank=True)
    documento = models.FileField(upload_to='AbraArte', null=True, blank=True)

    def _str_(self):
        return self.titulo
