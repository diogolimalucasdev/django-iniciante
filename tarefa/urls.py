from django.urls import path
from . import views
from django.views.generic.base import RedirectView

urlpatterns = [
    path("tarefas/", views.index),
    path('tarefas/delete/<slug:id>', views.delete_tarefa ),
    path('', RedirectView.as_view(url='/tarefas/')) #quando eu for na url principal ele vai me redirecionar para tarefas
]