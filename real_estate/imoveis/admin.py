from django.contrib import admin
from .models import Anuncio, ImagensAnuncio


# Register your models here.

class AnuncioAdmin(admin.ModelAdmin):
	list_display = ('id', 'tipo_anuncio', 'quartos' ,'get_user', 'pagamento', 'publicado' ,'tipo_imovel' ,'titulo' ,'cidade', 'preco_venda', 'preco_aluguel')

	def get_user(self, obj):
		return obj.user.first_name

class ImagemAdmin(admin.ModelAdmin):
	list_display = ('id', 'get_anuncio_id', 'get_anuncio_titulo', 'get_anuncio_user')

	def get_anuncio_id(self, obj):
		return obj.anuncio.id

	def get_anuncio_titulo(self, obj):
		return obj.anuncio.titulo

	def get_anuncio_user(self, obj):
		return obj.anuncio.user


admin.site.register(Anuncio, AnuncioAdmin)
admin.site.register(ImagensAnuncio, ImagemAdmin)


