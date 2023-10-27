from django.urls import path
from . import views

urlpatterns = [
    path('validar_renda/', views.validar_renda, name='validar_renda'),
    path('calcular_emprestimo/', views.calcular_emprestimo, name='calcular_emprestimo'),
    path('', views.index, name='index'),
    path('renda_invalida/', views.renda_invalida, name='renda_invalida'),
    path('resultado_emprestimo/', views.resultado_emprestimo, name='resultado_emprestimo'),
]