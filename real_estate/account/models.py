from django.db import models
from django.conf import settings

# cada usuário vai ter um perfil, toda vez que o usuário for criado, um perfil tb será criado, ver no view.

class Perfil(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	data_nascimento = models.DateField(blank=True, null=True)
	foto = models.ImageField(upload_to='users/%Y/%m/%d', blank=True)
	estado =  models.CharField(max_length=2, blank=True)
	cidade  = models.CharField(max_length=50, blank=True)
	telefone = models.CharField(max_length=50, blank=True)
	def __str__(self):
		return 'Profile for user {}'.format(self.user.username)


