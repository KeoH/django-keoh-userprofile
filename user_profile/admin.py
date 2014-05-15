from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import UserProfile

class UserProfileInline(admin.StackedInline):
	model = UserProfile
	can_delete = False

class UserAdmin(UserAdmin):

	list_display = UserAdmin.list_display + ('avatar_admin',)
	inlines = (UserProfileInline,)

	def avatar_admin(self, obj):
		if obj.userprofile.avatar:
			html = '<figure><img width="60px" height="60px" src="%s"></figure>' % (obj.userprofile.avatar.url)
		else:	
			html = '<figure><img width="60px" height="60px" src="%s"></figure>' % ('/static/img/default.png')
		return html

	avatar_admin.allow_tags = True
	avatar_admin.short_description = 'Avatar'

admin.site.unregister(User)
admin.site.register(User, UserAdmin)