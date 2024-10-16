from django.db import models


class Pesas(models.Model):
    marca = models.CharField(max_length=20)
    material = models.CharField(max_length=20)
    peso = models.IntegerField()