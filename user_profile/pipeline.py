#encoding:utf-8
from requests import request, HTTPError
from django.core.files.base import ContentFile

def save_profile_picture(backend, user, response, details, is_new=False, *args, **kwargs):

    if backend.name == 'facebook':

        url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        user.userprofile.facebook_link = response.get('link')
        response = request('GET', url, params={'type': 'large'})
        user.userprofile.avatar.save('{0}_social.jpg'.format(user.first_name), ContentFile(response.content))
        user.userprofile.save()

    if backend.name == 'twitter':

        user.userprofile.twitter = response.get('screen_name')
        user.userprofile.save()
