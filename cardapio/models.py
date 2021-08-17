from django.db import models
from datetime import datetime
from pessoas.models import Pessoa

class Prato(models.Model):
    pessoa = models.ForeignKey(Pessoa, on_delete=models.CASCADE)
    nome_prato = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    preco = models.FloatField()
    rendimento = models.TextField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_prato = models.DateTimeField(default=datetime.now, blank=True)
    foto_prato = models.ImageField(upload_to="fotos/%d/%m/%Y", blank=True)
    publicada = models.BooleanField(default=False)
