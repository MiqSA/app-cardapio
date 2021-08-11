from django.db import models
from datetime import datetime


class Prato(models.Model):
    nome_prato = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    preco = models.FloatField()
    rendimento = models.TextField(max_length=100)
    categria = models.CharField(max_length=100)
    date_prato = models.DateTimeField(default=datetime.now, blank=True)
