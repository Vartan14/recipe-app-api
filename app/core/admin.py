"""
Django Admin customization
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core.models import User, Recipe


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for the users."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (
            _('Personal info'),
            {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }

        ),
        (
            _('Important dates'),
            {
                'fields': ('last_login',)
            }

        )
    )
    add_fieldsets = (
        (
            'Personal info',
            {
                'classes': ('wide',),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
    )


admin.site.register(User, UserAdmin)
admin.site.register(Recipe)
