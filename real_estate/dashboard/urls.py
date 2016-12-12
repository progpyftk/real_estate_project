from django.conf.urls import url
from . import views


urlpatterns = [
	# post views
	url(r'^home/$', views.dashboard_home,  name='dashboard_home'),
	url(r'^meus-anuncios/$', views.dashboard_meus_anuncios,  name='dashboard_meus_anuncios'),
	url(r'^meus-dados/$', views.dashboard_meus_dados,  name='dashboard_meus_dados'),
	url(r'^delete-estate/$', views.dashboard_deletar_anuncio, name='dashboard_deleta_anuncio'),
	url(r'^editar-anuncio/(?P<id>\d+)/$', views.dashboard_editar_anuncio, name='dashboard_editar_anuncio'),
	url(r'^editar-perfil/$', views.dashboard_editar_perfil, name='dashboard_editar_perfil'),
]