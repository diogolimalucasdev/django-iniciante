from django.shortcuts import render
from .models import TarefasBd

def index(request):
    conteudo = TarefasBd.objects.all()
    context={
        'conteudos': conteudo
    }
    return render(request, 'lista.html', context)

# Create your views here.
