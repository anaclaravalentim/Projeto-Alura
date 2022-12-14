from ctypes import Union
from pyexpat import model
from typing import Dict
from django.contrib import admin
from .models import Pessoa

class ListandoPessoas(admin.ModelAdmin):
   list_display = ('id','nome','email') 
   list_display_links = ('id','nome') 
   search_fields = ('nome',)


admin.site.register(Pessoa,ListandoPessoas)

