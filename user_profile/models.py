from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):

	avatar = models.ImageField(upload_to='media/user_profile/', blank=True, default="media/user_profile/default.png")

	def __unicode__(self):
		return self.username
