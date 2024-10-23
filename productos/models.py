from django.db import models

class Barra(models.Model):
    marca = models.CharField(max_length=20)
    modelo = models.CharField(max_length=20)
    peso = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.modelo}"