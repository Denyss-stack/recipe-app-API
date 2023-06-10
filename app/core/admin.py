"""
Djnago admin customization
"""
from django.contrib import admin  # noqa
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from django.utils.translation import gettext_lazy as _


class UserAdmin(BaseUserAdmin):
    """Define admin pages for uses"""

    ordering = ["id"]
    list_display = ["email", "name"]
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                )
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]


admin.site.register(User, UserAdmin)
