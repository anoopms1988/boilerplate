from django.contrib import admin
from django.contrib.auth.models import User
from .models import AccessApiKey


# from core.admin import admin_site


class UserAdmin(admin.ModelAdmin):
    pass


class AccessApiKeyAdmin(admin.ModelAdmin):
    list_display = ['type', 'key']


admin.site.register(AccessApiKey, AccessApiKeyAdmin)
