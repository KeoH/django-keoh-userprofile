from django.views.generic.base import TemplateView, View
from django.shortcuts import render

from .forms import EmailUserCreationForm

class ProfilePageView(TemplateView):
	template_name = 'profile.html'

class ProfileEditPageView(TemplateView):
	template_name = 'profile-edit.html'


