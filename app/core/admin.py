"""
Djnago admin customization
"""
from django.contrib import admin  # noqa
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User


class UserAdmin(BaseUserAdmin):
    """Define admin pages for uses"""

    ordering = ["id"]
    list_display = ["email", "name"]


admin.site.register(User, UserAdmin)
