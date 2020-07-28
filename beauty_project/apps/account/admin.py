from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.account.models import Account

"""
@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ('username', 'phone', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_superuser')
    search_fields = ('phone', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
"""