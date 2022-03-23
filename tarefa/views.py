from django.shortcuts import render, redirect
from .models import TarefasBd
from .forms import ConteudoForm

def index(request):
    conteudo = TarefasBd.objects.all()
    form=ConteudoForm() 
    if request.method=="POST":
        form=ConteudoForm(request.POST)
        if form.is_valid():
            form=form.save()
            return redirect('/')
        
    context={
        'conteudos': conteudo,
        'form': form,
    }
    return render(request, 'lista.html', context)

# Create your views here.
