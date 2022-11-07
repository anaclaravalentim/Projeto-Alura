from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Receita

def index(request):
    #filtro nas publicas e ordenação por última receita publicada
    receitas = Receita.objects.order_by('-data_receita').filter(publicada = True) 
   
    #receitas = Receita.objects.all   - Traz tudo

    dados = {
        'receitas' : receitas
    }

    return render(request,'index.html',dados)

def receita(request,receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)

    receita_a_exibir = {
        'receita' : receita
    }

    return render(request,'receita.html',receita_a_exibir)

def buscar(request):
    lista_receitas = Receita.objects.order_by('-data_receita').filter(publicada = True)

    if 'buscar' in request.GET:  #caso eu tenha um valor na busca
        nome_a_buscar = request.GET['buscar']
        if buscar:
            lista_receitas = lista_receitas.filter(nome_da_receita__icontains = nome_a_buscar) #buscar o que contem 

    dados = {
        'receitas' : lista_receitas
    }

    return render(request, 'buscar.html', dados)