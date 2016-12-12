from django.contrib import admin
from .models import Perfil

class PerfilAdmin(admin.ModelAdmin):
	list_display = ['user', 'data_nascimento', 'foto']


admin.site.register(Perfil, PerfilAdmin)
