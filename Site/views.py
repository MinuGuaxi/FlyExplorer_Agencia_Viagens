from django.shortcuts import render


def Index(request):

    return render(request, 'base.html')
"' Tela de Login'"
def tela_login(request):
    return render(request, 'paginas/login.html')

" 'Redefinir Senha' "
def redefinir(request):
    return render(request, 'paginas/r_senha.html')

" 'HOTEIS' "
def hoteis(request):
    return render(request, 'paginas/hotel.html')

"' PASSAGENS '"
def passagens(request):
    return render(request, 'paginas/passagens.html')


"' PACOTES '"
def pacotes(request):
    return render(request, 'paginas/pacotes.html')


"' OFERTAS '"
def ofertas(request):
    return render(request, 'paginas/ofertas.html')


"' ALUGUEIS '"
def alugueis(request):
    return render(request, 'paginas/alugueis.html')


"' SEGUROS '"
def seguros(request):
    return render(request, 'paginas/seguros.html')

def c_hotel(request):
    return render(request, 'paginas/r_hoteis.html')

def c_passagens(request):
    return render(request, 'paginas/r_passagens.html')

def c_pacotes(request):
    return render(request, 'paginas/r_pacotes.html')

def c_ofertas(request):
    return render(request, 'paginas/r_ofertas.html')

def c_alugueis(request):
    return render(request, 'paginas/r_alugueis.html')

def c_seguros(request):
    return render(request, 'paginas/r_seguros.html')