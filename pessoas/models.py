from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

class Pessoa(models.Model):
    nome = models.CharField(max_length = 200)
    idade = models.IntegerField()
    email = models.CharField(max_length=200)
    def __str__(self): #mostrar o nome da pessoa no admin
        return self.nome