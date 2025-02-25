from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from user.models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    list_display = UserAdmin.list_display + ("age", )
    fieldsets = UserAdmin.fieldsets +(("Additional info", {"fields": ("age", )}),)
    add_fieldsets = UserAdmin.add_fieldsets + (("Additional info", {"fields": ("first_name", "last_name", "age",)}),)
# admin.site.register(CustomUser, UserAdmin)
