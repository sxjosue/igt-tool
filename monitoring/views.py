from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Apresentacao(request):
    return render(request, 'Apresentacao.html')

def Monitoramento(request):
    return render(request, "monitoramento.html")

def Dispositivos(request):
    return render(request, "dispositivos.html")

def Controle(request):
    return render(request, "controle_rede.html")