from django.shortcuts import render


def Index(request):
    return render(request, 'base.html')

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

"' REDEFINIR '"
def redefinir(request):
    return render(request, 'paginas/r_senha.html')