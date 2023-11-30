
from django.urls import path
from Site import views

urlpatterns = [
    path('', views.Index),
    path('login/', views.tela_login, name='tela_login'),
    path('hoteis/', views.hoteis, name='hoteis'),
    path('passagens/', views.passagens, name='passagens'),
    path('pacotes/', views.pacotes, name='pacotes'),
    path('ofertas/', views.ofertas, name='ofertas'),
    path('alugueis/', views.alugueis, name='alugueis'),
    path('seguros/', views.seguros, name='seguros'),
    path('redefinir/', views.redefinir, name='redefinir'),
    path('registrar_hotel/', views.c_hotel, name='c_hoteis'),
    path('registrar_passagens/', views.c_passagens, name='c_passagens'),
    path('registrar_pacotes/', views.c_pacotes, name='c_pacotes'),
    path('registrar_alugueis/', views.c_alugueis, name='c_alugueis'),
    path('registrar_seguros/', views.c_seguros, name='c_seguros'),
    path('registrar_ofertas/', views.c_ofertas, name='c_ofertas')
]
 