from dataclasses import fields
from socket import fromshare
from django.forms import ModelForm
from django.db import models
from .models import TarefasBd

class ConteudoForm(ModelForm):
    class Meta:
        model=TarefasBd
        fields=['conteudo',]
