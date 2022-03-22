from django.contrib import admin
from .models import TarefasBd

@admin.register(TarefasBd)

class TarefaAdmin(admin.ModelAdmin):
    list_display= ['id', 'conteudo', 'data']
    

# Register your models here.
