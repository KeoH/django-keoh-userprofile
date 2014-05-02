#encoding:utf-8
from django.conf.urls import patterns, url
from .views import ProfilePageView, ProfileEditPageView

urlpatterns = patterns('',
	url(r'^$', ProfilePageView.as_view(), name='home'),
	url(r'edit/$', ProfileEditPageView.as_view(), name='edit'),
	url(r'signin/$', ProfileEditPageView.as_view(), name='edit'),
	url(r'success/$', ProfileEditPageView.as_view(), name='success'),
)