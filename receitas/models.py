from distutils.command import upload
from email.policy import default
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User #Modelo de usuário do djangos

class Receita(models.Model):
    pessoa          = models.ForeignKey(User, on_delete = models.CASCADE)
    nome_da_receita = models.CharField(max_length = 200) #char é menor e com tamanho máximo
    ingredientes    = models.TextField() #caixinha de texto, como um long char
    modo_preparo    = models.TextField()
    rendimento      = models.CharField(max_length = 100)
    categoria       = models.CharField(max_length = 100) 
    data_receita    = models.DateTimeField(default = datetime.now, blank = True)
    publicada       = models.BooleanField(default=False)
    foto_receita    = models.ImageField(upload_to = 'fotos/%d/%m/%Y/', blank = True)
  
    def __str__(self): #retorna o nome da receita no admin
        return self.nome_da_receita