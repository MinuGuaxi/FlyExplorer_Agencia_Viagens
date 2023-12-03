from django.shortcuts import render
from Site.models import Hotel, Passagem, Pacotes, Ofertas, Alugueis, Seguros


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


"' FUNÇÕES DE REGISTRO '"


"' REGISTRAR UM HOTEL / HOSPEDAGEM '"
def c_hotel(request):
    return render(request, 'paginas/r_hoteis.html')

def R_hotel(request):
    id =request.POST['ID_h']
    nome=request.POST['n_h']
    telefone=request.POST['t_h']
    valor=request.POST['v_h']
    servicos=request.POST['s_h']
    imagem=request.POST, request.FILES['img_h']

    hotel = Hotel.objects.create(id=id, nome=nome, telefone=telefone, valor=valor, servicos=servicos, imagem=imagem)
    return redirect('c_hoteis')


"' REGISTRAR UMA COMPANHIA / PASSAGEM '"
def c_passagens(request):
    return render(request, 'paginas/r_passagens.html')

def R_passagem(request):
    id =request.POST['ID_psg']
    nome=request.POST['n_psg']
    telefone=request.POST['t_psg']
    valor=request.POST['v_psg']
    servicos=request.POST['s_psg']
    destinos=request.POST['d_psg']

    passagem = Passagem.objects.create(id=id, nome=nome, telefone=telefone, valor=valor, servicos=servicos, destinos=destinos)
    return redirect('c_passagens')


"' REGISTRAR UM PACOTE '"
def c_pacotes(request):
    return render(request, 'paginas/r_pacotes.html')

def R_pacotes(request):
    id =request.POST['ID_pct']
    nome=request.POST['n_pct']
    telefone=request.POST['t_pct']
    valor=request.POST['v_pct']
    expedicao=request.POST['e_pct']
    servicos=request.POST['s_pct']
    descricao=request.POST['dsc_pct']
    imagem=request.POST, request.FILES['img_pct']


    pacote = Pacotes.objects.create(id=id, nome=nome, telefone=telefone, valor=valor, expedicao=expedicao, servicos=servicos, descricao=descricao, imagem=imagem)
    return redirect('c_pacotes')



"' REGISTRAR UMA OFERTA '"
def c_ofertas(request):
    return render(request, 'paginas/r_ofertas.html')

def R_ofertas(request):
    id =request.POST['ID_oft']
    nome=request.POST['n_oft']
    telefone=request.POST['t_oft']
    valor=request.POST['v_oft']
    tipo=request.POST['t_oft']
    servicos=request.POST['s_oft']
    descricao=request.POST['dsc_oft']
    imagem=request.POST, request.FILES['img_oft']


    oferta = Ofertas.objects.create(id=id, nome=nome, telefone=telefone, valor=valor, tipo=tipo, servicos=servicos, descricao=descricao, imagem=imagem)
    return redirect('c_ofertas')




"' REGISTRAR UM ALUGUEL '"
def c_alugueis(request):
    return render(request, 'paginas/r_alugueis.html')

def R_alugueis(request):
    id =request.POST['ID_a']
    nome=request.POST['n_a']
    telefone=request.POST['t_a']
    valor=request.POST['v_a']
    tipo=request.POST['t_a']
    servicos=request.POST['s_a']
    descricao=request.POST['dsc_a']
    imagem=request.POST, request.FILES['img_a']


    aluguel = Alugueis.objects.create(id=id, nome=nome, telefone=telefone, valor=valor, tipo=tipo, servicos=servicos, descricao=descricao, imagem=imagem)
    return redirect('c_alugueis')



"' REGISTRAR UM SEGURO '"
def c_seguros(request):
    return render(request, 'paginas/r_seguros.html')

def R_seguros(request):
    id =request.POST['ID_s']
    nome=request.POST['n_s']
    telefone=request.POST['t_s']
    valor=request.POST['v_s']
    tipo=request.POST['t_s']
    descricao=request.POST['dsc_s']

    seguro = Seguros.objects.create(id=id, nome=nome, telefone=telefone, valor=valor, tipo=tipo, descricao=descricao)
    return redirect('c_seguros')