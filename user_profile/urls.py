#encoding:utf-8

from django.conf.urls import patterns, include, url

from .views import LoginView, LogoutView, CreateUserView, ProfileView

urlpatterns = patterns('',
    url(r'^login/$', LoginView.as_view(), name='LogIn'),
    url(r'^signup/$', CreateUserView.as_view(), name='SignUp'),
    url(r'^logout/$', LogoutView.as_view(), name='Logout'),

    url(r'^profile/$', ProfileView.as_view(), name='Profile'),
)
