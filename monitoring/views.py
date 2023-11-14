from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def Apresentacao(request):
    return render(request, 'Apresentacao.html')

def Monitoramento(request):
    return render(request, "monitoramento.html")