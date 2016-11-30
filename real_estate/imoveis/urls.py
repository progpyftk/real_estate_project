from django.conf.urls import url
from . import views


urlpatterns = [
	# post views
	url(r'^imoveis-venda/$', views.busca_comprar,  name='busca_comprar'),
	url(r'^imoveis-aluguel/$', views.busca_alugar,  name='busca_alugar'),
	# url para um anuncio
	url(r'^imoveis-venda/(?P<slug>[-\w]+)/$',views.anuncio, name='anuncio'),
	#url(r'^imoveis-aluguel/(?P<slug>[-\w]+)/$',views.anuncio, name='anuncio'),
	# resultado busca
	url(r'^resultado-busca-comprar/$',views.resultado_busca_comprar, name='resultado_busca_comprar'),
	url(r'^resultado-busca-alugar/$',views.resultado_busca_alugar, name='resultado_busca_alugar'),
	#url(r'^imoveis-venda/rio-das-ostras$', views.rio_das_ostras,  name='base'),
	#url(r'^imoveis-venda/macae$', views.base,  name='base'),

	url(r'^anunciar-imovel/$',views.anunciar_imovel, name='anunciar_imovel'),
	
]