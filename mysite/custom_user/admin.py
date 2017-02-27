from django.contrib import admin
from django.db import models
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from .forms import EmailUserChangeForm, EmailUserCreationForm
from custom_user.models import EmailUser
from django.core.validators import RegexValidator



class EmailUserAdmin(UserAdmin):

    """EmailUser Admin model."""

    fieldsets = (
        (None, {'fields': ('email', 'username', 'password')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = ((
        None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password', )
        }
    ),
    )

    # The forms to add and change user instances
    form = EmailUserChangeForm
    add_form = EmailUserCreationForm
	
    def assign_group(self, email, password, **extra_fields):
        form = EmailUserCreationForm(data=request.POST)
        if form.is_valid():
                user = self.model(email=email, username=username, is_staff=is_staff, is_active=is_active,
                          is_superuser=is_superuser, last_login=now,
                          date_joined=now, **extra_fields)
                

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('username', 'email', 'Label')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'Label')
    search_fields = ('name', 'username',)
    ordering = ('email', 'username',)
    filter_horizontal = ('groups', 'user_permissions', )

# Register the new EmailUserAdmin
admin.site.register(EmailUser, EmailUserAdmin)


