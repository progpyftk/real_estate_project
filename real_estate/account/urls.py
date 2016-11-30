from django.conf.urls import url
from . import views

urlpatterns = [
	# post views
	url(r'^base/$', views.base,  name='base'),
	url(r'^index/$', views.index,  name='index'),
	url(r'^login/$', views.user_login,  name='login'),
	# quando fizer o logout joga pro login de novo
	url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'account/logout_sucess.html'}, name='logout'),

	# change password urls
	url(r'^password-change/$','django.contrib.auth.views.password_change', {'template_name': 'account/password_change_form.html'}, name='password_change'),
	url(r'^password-change/done/$','django.contrib.auth.views.password_change_done', {'template_name': 'account/password_change_done.html'}, name='password_change_done'),

	# restore password urls
	url(r'^password-reset/$', 'django.contrib.auth.views.password_reset', {'template_name':'account/password_reset_form.html'}, name='password_reset'),
	url(r'^password-reset/done/$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'account/password_reset_done.html'} , name='password_reset_done'),
	url(r'^password-reset/confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$', 'django.contrib.auth.views.password_reset_confirm', {'template_name': 'account/password_reset_confirm.html'}, name='password_reset_confirm'),
	url(r'^password-reset/complete/$', 'django.contrib.auth.views.password_reset_complete', {'template_name':'account/password_reset_complete.html'}, name='password_reset_complete'),

	# Register
	url(r'^register/$', views.register, name='register'),

	
]