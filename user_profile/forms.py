#encoding:utf-8
from .models import UserProfile
from django import forms
from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

class EmailUserCreationForm(UserCreationForm):

	username = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder':_('Username')}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'input', 'placeholder':_('Email')}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder':_('Password')}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'input', 'placeholder':_('Repeat password')}))


	try:
		error_css_class = settings.ERROR_CSS_CLASS
	except:
		error_css_class = 'field-error'

	try:
		required_css_class = settings.REQUIRED_CSS_CLASS
	except:
		required_css_class = 'field-required'

	class Meta:
		model = UserProfile
		fields = ('username', 'email')
