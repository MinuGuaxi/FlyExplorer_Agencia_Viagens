
from django.urls import path
from Site import views

urlpatterns = [
    path('', views.Index),
    path('passagens/', views.passagens, name='passagens'),
    path('pacotes/', views.pacotes, name='pacotes'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('alugueis/', views.alugueis, name='alugueis'),
    path('seguros/', views.seguros, name='seguros'),
    path('redefinir/', views.redefinir, name='redefinir'),
]
 