from django import forms
from django.contrib.auth import authenticate, login
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout
from django.core.validators import RegexValidator
from django.contrib import messages
from django.contrib.auth.models import User
from django.conf import settings
from .models import Perfil


class LoginForm(forms.Form):
    help_text = 'Insira aqui o seu password'
    alphanumeric = RegexValidator(
        r'^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')
    username = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Username or Email'}))
    password = forms.CharField(label='', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'has-popover', 'data-content': 'Insira seu password', 'data-placement': 'right', 'data-container': 'body'}))
    #password = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    name = forms.CharField(label='',
                           required=True,
                           validators=[alphanumeric],
                           widget=forms.TextInput(attrs={'placeholder': 'Name'}))

    # Not working - Colocar para mostrar o erro no popover
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        if self.errors:
            print('TEM ERROR NESSA POHAAAAAAAAAAAAAAAAAAA')
            for f_name in self.fields:
                print(f_name)
                print(self.errors)
                if f_name in self.errors:
                    print('AQUIIIIIIIIIIIIIIIIIIIIIIIIIII')
                    classes = self.fields[f_name].widget.attrs.get('class', '')
                    classes += 'has-popover'
                    self.fields[f_name].widget.attrs['class'] = classes
                    self.fields[f_name].widget.attrs[
                        'data-content'] = 'Vai dar merda essa poha hein'
                    self.fields[f_name].widget.attrs[
                        'data-placement'] = 'right'
                    self.fields[f_name].widget.attrs['data-container'] = 'body'

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Login Inválido. Tente Novamente.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class UserRegistrationForm(forms.Form):
    username = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    email = forms.EmailField(label='', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'E-mail'}))
    password = forms.CharField(label='', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'has-popover', 'data-content': 'Insira seu password', 'data-placement': 'right', 'data-container': 'body'}))
    password_2 = forms.CharField(label='', required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password', 'class': 'has-popover', 'data-content': 'Insira seu password', 'data-placement': 'right', 'data-container': 'body'}))
    first_name = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(label='', required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Last Name'}))

    def clean_username(self):
        try:
            user = User.objects.get(
                username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError("Usuário já existe, escolha outro.")

    def clean_email(self):
        try:
            user = User.objects.get(email__iexact=self.cleaned_data['email'])
        except User.DoesNotExist:
            return self.cleaned_data['email']
        raise forms.ValidationError("Email já registrado.")

    def clean(self):
        if 'password' in self.cleaned_data and 'password_2' in self.cleaned_data:
            if self.cleaned_data['password'] != self.cleaned_data['password_2']:
                raise forms.ValidationError(
                    "Os dois passwirds deven ser idênticos")
        return self.cleaned_data


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class PerfilEditForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ('cidade', 'estado', 'telefone', 'foto', 'data_nascimento')



