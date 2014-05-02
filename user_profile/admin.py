from django.contrib import admin

from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
	ordering = ('username',)
	list_display = ('username', 'email', 'avatar_admin')

admin.site.register(UserProfile, UserProfileAdmin)