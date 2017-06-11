from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from chat_app.models import UserProfile, Messages


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'user status'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )
    list_display = ('username', 'first_name', 'user_status')

    def user_status(self, obj):
        return obj.userprofile.status

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Messages)
