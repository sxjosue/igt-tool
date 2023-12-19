from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Apresentacao', views.Apresentacao, name='Apresentacao'),
    path('Monitoramento', views.Monitoramento, name='Monitoramento'),
    path('Dispositivos', views.Dispositivos, name='Dispositivos'),
    path('Controle', views.Controle, name='Controle'),
]
