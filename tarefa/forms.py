from django import forms
from .models import TarefasBd

class ConteudoForm(forms.ModelForm):
    class Meta:
        model=TarefasBd
        fields=('conteudo',)
