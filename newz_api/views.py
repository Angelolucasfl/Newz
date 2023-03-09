from django.shortcuts import render
import requests
API_KEY = '8871678ec272463da9a836475aa1ff26'

def home(request):
    topico = request.GET.get('category')
    fonte = request.GET.get('fonte')

    artigos = []

    url = f'https://newsapi.org/v2/top-headlines?country=us&apikey={API_KEY}'
    print(url)
    resposta = requests.get(url)
    dados = resposta.json()
    artigos = dados['articles']  # atualizar a lista de artigos com os valores obtidos na API

    
    if topico:
        url = f'https://newsapi.org/v2/top-headlines?category={topico}&country=us&apikey={API_KEY}'
        resposta = requests.get(url)
        dados = resposta.json()
        artigos = dados['articles']  # substituir a lista de artigos com os valores obtidos na API
        


    if fonte:
        url = f'https://newsapi.org/v2/everything?sources={fonte}&apiKey={API_KEY}'
        resposta = requests.get(url)
        dados = resposta.json()
        artigos = dados['articles']  # substituir a lista de artigos com os valores obtidos na API
        
    
    
    context = {'artigos':artigos}

    return render(request, 'newz_api/home.html', context)

