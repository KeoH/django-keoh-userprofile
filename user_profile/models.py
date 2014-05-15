from .storage import OverwriteStorage
from cStringIO import StringIO 
from django.conf import settings
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.core.files.uploadedfile import SimpleUploadedFile
from django.db import models
from PIL import Image
from django.db.models.signals import post_save, pre_save
import os


class UserProfile(models.Model):

	user = models.OneToOneField(User)

	def save_avatar(self, filename):

		extension = filename[filename.rfind('.'):]
		new_path = 'user_profile/%s-avatar%s' %(self.user.username, extension)
		return new_path

	avatar = models.ImageField(storage=OverwriteStorage(), upload_to=save_avatar, blank=True)

	def __unicode__(self):
		return self.user.username

	def resize_avatar(self):
		# code from with some changes : http://www.yilmazhuseyin.com/blog/dev/create-thumbnails-imagefield-django/
		if not self.avatar:
			return

		try:
			AVATAR_SIZE = settings.AVATAR_SIZE
		except:
			AVATAR_SIZE = (200,200)

		DJANGO_TYPE = self.avatar.file.content_type 

		image = Image.open(StringIO(self.avatar.read()))
		image = image.resize(AVATAR_SIZE, Image.ANTIALIAS)

		temp_handle = StringIO()
		image.save(temp_handle, 'jpeg')
		temp_handle.seek(0)

		suf = SimpleUploadedFile(os.path.split(self.avatar.name)[-1],temp_handle.read(), content_type='image/jpeg')
		self.avatar.save('%s.%s' %(os.path.splitext(suf.name)[0], 'jpg'),suf, save=False)

	def save(self, *args, **kwargs):
		self.resize_avatar()
		super(UserProfile, self).save()

	def get_avatar(self):
		if self.avatar:
			avatar_url = self.avatar.url
		else:	
			avatar_url = '/static/img/default.png'
		return avatar_url

def create_user_profile(sender, instance, **kwargs):
	p = UserProfile.objects.get_or_create(user=instance)

post_save.connect(create_user_profile, sender=User,dispatch_uid="Userprofile created")
