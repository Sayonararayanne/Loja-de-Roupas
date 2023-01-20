from django.db import models

# Create your models here.
class Roupa(models.Model):
    tipo_de_roupa = models.CharField(max_length=300)
    cor = models.CharField(max_length=200)
    tamanho = models.CharField(max_length=20)  
    preco = models.FloatField()  
    quantidade = models.IntegerField()
