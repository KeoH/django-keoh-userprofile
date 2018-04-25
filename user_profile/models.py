from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from .storage import OverwriteStorage


class UserProfile(User):

    twitter = models.CharField(max_length=100, blank=True)
    facebook_link = models.URLField(blank=True)

    def get_twitter_url(self):
        return 'https://twitter.com/{0}'.format(self.twitter)

    def save_avatar(self, filename):
        extension = filename[filename.rfind('.'):]
        new_path = 'user_profile/%s%s-avatar%s' % (
            self.first_name, self.pk, extension)
        return new_path

    _avatar = models.ImageField(
        storage=OverwriteStorage(), upload_to=save_avatar, blank=True)

    @property
    def avatar(self):
        return self._avatar.url or '{}/static/img/default.png'.format(
            settings.STATIC_URL)

    def __str__(self):
        return self.username
