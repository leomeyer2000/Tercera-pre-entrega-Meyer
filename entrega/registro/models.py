from django.db import models

# Create your models here.
class Documento(models.Model):
    registro = models.CharField(max_length=40)
    codigo = models.IntegerField()
    pin = models.IntegerField()
    fecha = models.DateField()
    observaciones = models.BooleanField()
    
class Escribano(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=40)
    email = models.EmailField()
    
class Observacion(models.Model):
    documento = models.IntegerField()
    tipo = models.CharField(max_length=40)

