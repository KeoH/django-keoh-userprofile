# -*- coding: utf-8 -*-

from django.views.generic import View, TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import login, logout
from django.core.urlresolvers import reverse

from .forms import UserLoginForm, EmailUserCreationForm

class LoginView(View):
    form_class = UserLoginForm
    template_name = "login.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return HttpResponseRedirect(reverse('userprofile:Profile'))
        return render(request, self.template_name, {'form' : form})

class CreateUserView(View):
    form_class = EmailUserCreationForm
    template_name = "signup.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form' : form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
        return render(request, self.template_name, {'form': form})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')

class ProfileView(TemplateView):
    template_name = 'profile.html'
