from django import forms
from django.forms import ModelForm, Textarea
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django.core.validators import RegexValidator
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from .models import Anuncio, ImagensAnuncio


class ComprarBuscaForm(forms.Form):
    CIDADES = (('Macaé', 'Macaé'), ('Rio das Ostras', 'Rio das Ostras'),
               ('Campos', 'Campos'), ('Búzios', 'Búzios'))
    cidade = forms.ChoiceField(choices=CIDADES, label="", initial='Selecione a Cidade',
                               widget=forms.Select(attrs={'class': 'in-drop'}),
                               required=True)
    TIPOS_DE_IMOVEL = (('Casa', 'Casa'), ('Apartamento', 'Apartamento'),
                       ('Comercial', 'Comercial'), ('Fazendo', 'Fazenda'))
    tipo_imovel = forms.ChoiceField(choices=TIPOS_DE_IMOVEL, label="", initial='Selecione o Tipo',
                                    widget=forms.Select(
                                        attrs={'class': 'in-drop'}),
                                    required=True)
    QUARTOS = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), ('6', '5+'))
    quartos = forms.ChoiceField(choices=QUARTOS, label="", initial='Selecione o n° de quartos',
                                widget=forms.Select(
                                    attrs={'class': 'in-drop'}),
                                required=True)
    PRECOS_MINIMO = ((0, 'R$ 00,00'), (50000, 'R$ 50.000,00'), (100000, 'R$ 100.000,00'),
                     (200000, 'R$ 200.000,00'), (300000, 'R$ 300.000,00'), (400000, 'R$ 400.000,00'))
    preco_minimo = forms.ChoiceField(choices=PRECOS_MINIMO, label="", initial='Selecione o preço mínimo',
                                     widget=forms.Select(
                                         attrs={'class': 'in-drop'}),
                                     required=True)
    PRECOS_MAXIMO = ((1000000, 'R$ 1.000.000,00'), (50000, 'R$ 50.000,00'), (100000, 'R$ 100.000,00'),
                     (200000, 'R$ 200.000,00'), (300000, 'R$ 300.000,00'), (400000, 'R$ 400.000,00'))
    preco_maximo = forms.ChoiceField(choices=PRECOS_MAXIMO, label="", initial='Selecione o preço máximo',
                                     widget=forms.Select(
                                         attrs={'class': 'in-drop'}),
                                     required=True)
    AREA_MINIMA = ((0, '0m2'), (50, '50m2'), (70, '70m2'), (100, '100m2'))
    area_minima = forms.ChoiceField(choices=AREA_MINIMA, label="", initial='Selecione o preço mínimo',
                                    widget=forms.Select(
                                        attrs={'class': 'in-drop'}),
                                    required=True)
    AREA_MAXIMA = ((100, '100m2'), (300, '300m2'))
    area_maxima = forms.ChoiceField(choices=AREA_MAXIMA, label="", initial='Selecione o preço máximo',
                                    widget=forms.Select(
                                        attrs={'class': 'in-drop'}),
                                    required=True)


class AlugarBuscaForm(forms.Form):
    CIDADES = (('Macaé', 'Macaé'), ('Rio das Ostras', 'Rio das Ostras'),
               ('Campos', 'Campos'), ('Búzios', 'Búzios'))
    cidade = forms.ChoiceField(choices=CIDADES, label="", initial='Selecione a Cidade',
                               widget=forms.Select(attrs={'class': 'in-drop'}),
                               required=True)
    TIPOS_DE_IMOVEL = (('Casa', 'Casa'), ('Apartamento', 'Apartamento'),
                       ('Comercial', 'Comercial'), ('Fazendo', 'Fazenda'))
    tipo_imovel = forms.ChoiceField(choices=TIPOS_DE_IMOVEL, label="", initial='Selecione o Tipo',
                                    widget=forms.Select(
                                        attrs={'class': 'in-drop'}),
                                    required=True)
    QUARTOS = ((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), ('6', '5+'))
    quartos = forms.ChoiceField(choices=QUARTOS, label="", initial='Selecione o n° de quartos',
                                widget=forms.Select(
                                    attrs={'class': 'in-drop'}),
                                required=True)
    PRECOS_MINIMO = ((0, 'R$ 00,00'), (500, 'R$ 500,00'), (1000, 'R$ 1000,00'),
                     (2000, 'R$ 2000,00'), (3000, 'R$ 3000,00'), (4000, 'R$ 4000,00'))
    preco_minimo = forms.ChoiceField(choices=PRECOS_MINIMO, label="", initial='Selecione o preço mínimo',
                                     widget=forms.Select(
                                         attrs={'class': 'in-drop'}),
                                     required=True)
    PRECOS_MAXIMO = ((1000, 'R$ 1000,00'), (2000, 'R$ 2000,00'), (3000, 'R$ 3000,00'),
                     (4000, 'R$ 4000,00'), (6000, 'R$ 300.000,00'), (10000, 'R$ 10000,00'))
    preco_maximo = forms.ChoiceField(choices=PRECOS_MAXIMO, label="", initial='Selecione o preço máximo',
                                     widget=forms.Select(
                                         attrs={'class': 'in-drop'}),
                                     required=True)
    AREA_MINIMA = ((0, '0m2'), (50, '50m2'), (70, '70m2'), (100, '100m2'))
    area_minima = forms.ChoiceField(choices=AREA_MINIMA, label="", initial='Selecione o preço mínimo',
                                    widget=forms.Select(
                                        attrs={'class': 'in-drop'}),
                                    required=True)
    AREA_MAXIMA = ((100, '100m2'), (300, '300m2'))
    area_maxima = forms.ChoiceField(choices=AREA_MAXIMA, label="", initial='Selecione o preço máximo',
                                    widget=forms.Select(
                                        attrs={'class': 'in-drop'}),
                                    required=True)


class AnuncioForm(ModelForm):
    class Meta:
        model = Anuncio
        exclude = ['user', 'slug', 'pagamento', 'publicado', 'pais', 'estado', 'numero', 'destaque']
        labels = {
            'titulo': ('Título'),
            'nome_contato': ('Nome do contato'),
            'telefone_contato': ('Telefone'),
            'email_contato': ('E-mail'),
            'tipo_anuncio': ('Tipo do anúncio'),
            'descricao': ('Descrição'),
            'imagem_principal': ('Imagem de capa'),
            'banheiros': ('Banheiros'),
            'quartos': ('Quartos'),
            'suites': ('Suítes'),
            'area_construida': ('Área construída'),
            'area_total': ('Área total'),
            'tipo_imovel': ('Tipo do imóvel'),
            'preco_venda': ('Preço de venda'),
            'preco_aluguel': ('Preço do aluguel'),
            'pais': ('País'),
            'estado': ('Estado'),
            'cidade': ('Cidade'),
            'rua': ('Rua'),
            'bairro': ('Bairro'),
            'numero': ('Número'),
            'cep': ('CEP'),
        }
        help_texts = {
            'titulo': ('Insira o título do anúncio'),
            'nome_contato': ('Nome do contato que irá aparecer para o comprador'),
            'telefone_contato': ('Número do telefone para entrar em contato'),
            'email_contato': ('E-mail de contato'),
            'tipo_anuncio': ('O que deseja fazer com seu imóvel? Vender? Alugar? Ou qualquer?'),
            'descricao': ('Descreve com detalhes as características do imóvel'),
            'imagem_principal': ('Imagem de capa'),
            'banheiros': ('Banheiros'),
            'quartos': ('Quartos'),
            'suites': ('Suítes'),
            'area_construida': ('Área construída'),
            'area_total': ('Área total'),
            'tipo_imovel': ('Tipo do imóvel'),
            'preco_venda': ('Preço de venda'),
            'preco_aluguel': ('Preço do aluguel'),
            'estado': ('Estado'),
            'cidade': ('Cidade'),
            'rua': ('Rua'),
            'bairro': ('Bairro'),
            'numero': ('Número'),
            'cep': ('CEP'),
        }



class ImagensForm(forms.ModelForm):
	class Meta:
		model = ImagensAnuncio
		fields = ['imagem']
