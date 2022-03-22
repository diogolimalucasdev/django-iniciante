from django.shortcuts import render
from .models import TarefasBd
from .forms import ConteudoForm

def index(request):
    conteudo = TarefasBd.objects.all()
    form=ConteudoForm()
    context={
        'conteudos': conteudo,
        'form': form,
    }
    return render(request, 'lista.html', context)

# Create your views here.
