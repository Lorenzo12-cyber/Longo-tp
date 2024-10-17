from django.db import models


class Pesas(models.Model):
    marca = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    peso = models.IntegerField()


    def __str__(self):
        return f"{self.marca} {self.peso}"
    