from django.shortcuts import render
from .models import Anuncio
from .forms import ComprarBuscaForm, AlugarBuscaForm, AnuncioForm
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
import random


def busca_comprar(request):
    if request.method == 'POST':
        form = ComprarBuscaForm(request.POST)
        request.session['tipo_anuncio'] = 'Venda'
        if form.is_valid():
            cidade = form.cleaned_data['cidade']
            request.session['cidade'] = form.cleaned_data['cidade']
            request.session['quartos'] = form.cleaned_data['quartos']
            request.session['tipo_imovel'] = form.cleaned_data['tipo_imovel']
            request.session['preco_minimo'] = form.cleaned_data['preco_minimo']
            request.session['preco_maximo'] = form.cleaned_data['preco_maximo']
            request.session['area_minima'] = form.cleaned_data['area_minima']
            request.session['area_maxima'] = form.cleaned_data['area_maxima']
            return HttpResponseRedirect(reverse('imoveis:resultado_busca_comprar'))
    else:
        form = ComprarBuscaForm()
    return render(request, 'imoveis/busca_comprar.html', {'form': form})


def busca_alugar(request):
    if request.method == 'POST':
        request.session['tipo_anuncio'] = 'Aluguel'
        form = AlugarBuscaForm(request.POST)
        if form.is_valid():
            cidade = form.cleaned_data['cidade']
            request.session['cidade'] = form.cleaned_data['cidade']
            request.session['quartos'] = form.cleaned_data['quartos']
            request.session['tipo_imovel'] = form.cleaned_data['tipo_imovel']
            request.session['preco_minimo'] = form.cleaned_data['preco_minimo']
            request.session['preco_maximo'] = form.cleaned_data['preco_maximo']
            request.session['area_minima'] = form.cleaned_data['area_minima']
            request.session['area_maxima'] = form.cleaned_data['area_maxima']
            return HttpResponseRedirect(reverse('imoveis:resultado_busca_alugar'))
    else:
        form = AlugarBuscaForm()
    return render(request, 'imoveis/busca_alugar.html', {'form': form})


def resultado_busca_comprar(request):
    if 'quartos' in request.session:
        anuncios = Anuncio.objects.filter(tipo_anuncio=request.session['tipo_anuncio'],
                                          quartos=request.session['quartos'],
                                          cidade=request.session['cidade'],
                                          tipo_imovel=request.session[
                                              'tipo_imovel'],
                                          preco_venda__gte=request.session[
                                              'preco_minimo'],
                                          preco_venda__lte=request.session[
                                              'preco_maximo'],
                                          area_construida__gte=request.session[
                                              'area_minima'],
                                          area_construida__lte=request.session[
                                              'area_maxima'],
                                          )
    else:
        anuncios = Anuncio.objects.all()
    anuncios_destaque = anuncio_aleatorio(5, 'Venda')
    print(anuncios_destaque)
    return render(request, 'imoveis/resultado_busca_comprar.html', {'anuncios': anuncios,
                                                                    'anuncios_destaque': anuncios_destaque})


def resultado_busca_alugar(request):
    if 'quartos' in request.session:
        anuncios = Anuncio.objects.filter(tipo_anuncio=request.session['tipo_anuncio'],
                                          quartos=request.session['quartos'],
                                          cidade=request.session['cidade'],
                                          tipo_imovel=request.session[
                                              'tipo_imovel'],
                                          preco_venda__gte=request.session[
                                              'preco_minimo'],
                                          preco_venda__lte=request.session[
                                              'preco_maximo'],
                                          area_construida__gte=request.session[
                                              'area_minima'],
                                          area_construida__lte=request.session[
                                              'area_maxima'],
                                          )
    else:
        anuncios = Anuncio.objects.all()
    anuncios_destaque = anuncio_aleatorio(5, 'Aluguel')
    print(anuncios_destaque)
    return render(request, 'imoveis/resultado_busca_alugar.html', {'anuncios': anuncios,
                                                                   'anuncios_destaque': anuncios_destaque})


def anuncio(request, slug):
    anuncio = get_object_or_404(Anuncio, slug=slug)
    if anuncio.tipo_anuncio == 'Venda':
        anuncios_destaque = anuncio_aleatorio(5, 'Venda')
    else:
        anuncios_destaque = anuncio_aleatorio(5, 'Aluguel')
    print("#############3")
    print(anuncios_destaque)
    return render(request, 'imoveis/anuncio.html', {'anuncio': anuncio,
                                                    'anuncios_destaque': anuncios_destaque})


def anuncio_aleatorio(numero_anuncios, tipo_anuncio):
    # essa é a funcao que retorna anúncios aleatórios que são exibidos ao longo do site
    # ela irá retornar uma lista com o numero_anuncios desejado, depois posso
    # adicionar alguns parametros se eu quiser
    i = 0
    anuncios_aleatorios = list()

    while i <= numero_anuncios:
        random_idx = random.randint(0, Anuncio.objects.count() - 1)
        # aqui eu posso aplicar alguns filtros, falta aplicar o filtro dos que
        # estão a venda e alugando
        random_obj = Anuncio.objects.all()[random_idx]
        # qunaod tiver mais que 5 anuncios colocar o incremento do i dentro do
        # if
        i = i + 1
        if random_obj not in anuncios_aleatorios:
            anuncios_aleatorios.append(random_obj)
    return anuncios_aleatorios


def anunciar_imovel(request):
    if request.method == 'POST':
        form = AnuncioForm(request.POST)
        if form.is_valid():
            novo_anuncio = form.save(commit=False)
            novo_anuncio.user = request.user
            novo_anuncio.save()
            return render(request, 'account/index.html')
    else:
        print("Renderizei o GET")
        form = AnuncioForm()
    return render(request, 'imoveis/anunciar.html', {'form': form})
