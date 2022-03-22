from django.db import models

# Create your models here.
class TarefasBd(models.Model): #crio meu banco de dados
    conteudo = models.CharField(max_length=1000)
    data=models.DateField(auto_now_add=True) #adiciona a data que eu estou criando
    
    
    def __str__(self):
        return str(self.id)