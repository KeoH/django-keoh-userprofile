from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class UserProfileAdmin(UserAdmin):

    list_display = UserAdmin.list_display + ('avatar_admin',)

    def avatar_admin(self, obj):
        return '<figure><img width="60px" height="60px" src="{}"></figure>'.format(obj.avatar)  # noqa

    avatar_admin.allow_tags = True
    avatar_admin.short_description = 'Avatar'


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
