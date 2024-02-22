# models.py

from django.db import models
from django.contrib.auth.models import User

class Marca(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self): 
        return self.nome 

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    def __str__(self): 
        return self.nome 

class Auto(models.Model):
    nome = models.CharField(max_length=200)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    def __str__(self): 
        return self.nome 

class Concessionario(models.Model):
    nome = models.CharField(max_length=200)
    cognome = models.CharField(max_length=200)
    def __str__(self): 
        return self.nome 

class Acquisto(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE)
    data_acquisto = models.DateField()
    def __str__(self): 
        return self.nome 
