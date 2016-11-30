from social.apps.django_app.middleware import SocialAuthExceptionMiddleware
from django.shortcuts import HttpResponse
from social import exceptions as social_exceptions
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages

class SocialAuthExceptionMiddleware(SocialAuthExceptionMiddleware):
	def process_exception(self, request, exception):
		print("### Entrei no Middleware")
		print(exception)
		print(request.user)
		print(self.backend)
		if hasattr(social_exceptions, 'AuthException'):
			print(social_exceptions)
			messages.success(request, 'deu certo')
			return HttpResponseRedirect(reverse('login'))
		else:
			raise exception