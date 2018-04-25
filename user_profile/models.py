from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class UserProfile(AbstractUser):

    twitter = models.CharField(max_length=100, blank=True)
    facebook_link = models.URLField(blank=True)

    def get_twitter_url(self):
        return 'https://twitter.com/{0}'.format(self.twitter)

    def save_avatar(self, filename):
        extension = filename[filename.rfind('.'):]
        new_path = 'user_profile/{}{}-avatar{}'.format(
            self.first_name, self.pk, extension)
        return new_path

    avatar = models.ImageField(upload_to=save_avatar, blank=True)

    @property
    def get_avatar(self):
        return self.avatar.url or '{}/static/img/default.png'.format(
            settings.STATIC_URL)

    def __str__(self):
        return self.username
