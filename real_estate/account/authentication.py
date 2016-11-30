from django.contrib.auth.models import User

class EmailAuthBackend(object):
	def authenticate(self, username=None, password=None):
		try:
			user = User.objects.get(email=username)
			# auth built in method user.check_password(password)
			if user.check_password(password):
				return user
			return None
		except User.DoesNotExist:
			return None
	
	def get_user(self, user_id):
		#  We get a user by the ID set in the user_id parameter
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None