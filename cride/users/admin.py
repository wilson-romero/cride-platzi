from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from cride.users.models import User, Profile

# Register your models here.


class CustomuserAdmin(UserAdmin):
    list_display = ('email', 'username', 'first_name', 'last_name', 'is_staff', 'is_client')
    list_filter = ('is_staff', 'is_client', 'created', 'modified')


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'reputation', 'rides_taken', 'rides_offered')
    list_filter = ('reputation',)
    search_fields = ('user__username', 'user__email', 'user__first_name', 'user__last_name')


admin.site.register(User, CustomuserAdmin)
