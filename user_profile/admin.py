from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe


class UserProfileAdmin(UserAdmin):

    list_display = UserAdmin.list_display + ('avatar_admin',)

    def avatar_admin(self, obj):
        temp = '<figure><img width="60px" height="60px" src="{url}"></figure>'
        return mark_safe(temp.format(url=obj.avatar.url))

    avatar_admin.allow_tags = True
    avatar_admin.short_description = 'Avatar'

    fieldsets = UserAdmin.fieldsets + (
        ('User Profile', {'fields': (
            'avatar',
        )}),
    )


admin.site.unregister(User)
admin.site.register(User, UserProfileAdmin)
