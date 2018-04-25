from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.safestring import mark_safe

from .models import UserProfile


class UserProfileAdmin(UserAdmin):

    list_display = UserAdmin.list_display + ('avatar_admin',)

    def avatar_admin(self, obj):
        return mark_safe('<figure><img width="60px" height="60px" src="{}"></figure>'.format(obj.avatar.url)) # noqa

    avatar_admin.allow_tags = True
    avatar_admin.short_description = 'Avatar'
    fieldsets = UserAdmin.fieldsets + (
        ('User Profile', {'fields': (
            'avatar',
        )}),
    )


admin.site.register(UserProfile, UserProfileAdmin)
