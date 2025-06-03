from django.db import models

class Visitante(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    imagen = models.FileField(upload_to='Visitantes', null=True, blank=True)  # ✅ Nueva imagen del visitante
    documento = models.FileField(upload_to='Visitantes', null=True, blank=True)  # ✅ Certificación o documento

    def __str__(self):
        return self.nombre
