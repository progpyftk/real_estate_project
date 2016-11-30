from requests import request
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from social.exceptions import AuthException
from django.contrib.auth.models import User


def check_email(request, backend, details, uid, user=None, *args, **kwargs):
	if backend.name == 'google-oauth2':


		# verifica se é um usuário jah existente pelo google, e que apenas vai fazer o login
		if uid and user:
			print("EU JA EXISTO")
			pass

		# se ele não existe é pq será registrado
		else:
			# pega o e-mail do cara que vai ser registado
			email = details.get('email', '')
			print("TO SENDO CRIADO")
			# procura na db se existe algum email parecido, se existir volta pro login
			count = User.objects.filter(email=email).count()
			if count>0:
				#messages.success(request, 'Domain Added.')
				#return HttpResponseRedirect(reverse('login'))
				print("LEVANTEI A EXCEPTION")
				raise AuthException(backend, 'Not unique email address.')

	