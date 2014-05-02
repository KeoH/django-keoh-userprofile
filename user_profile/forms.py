#encoding:utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import UserProfile

class EmailUserCreationForm(UserCreationForm):

	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':'Username'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder':'Email'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder':'Escribe una contraseña'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder':'Confirma contraseña'}))

	error_css_class = 'field-error'
	required_css_class = 'field-required'

	class Meta:
		model = UserProfile
		fields = ('username', 'email')
