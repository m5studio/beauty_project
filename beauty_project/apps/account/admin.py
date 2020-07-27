from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from apps.account.models import Account


# @admin.register(Account)
# class AccountAdmin(admin.ModelAdmin):
#     fieldsets = (
#         (None, {
#             'fields': ('username', 'phone', 'email')
#         }),
#         (None, {
#             'fields': ('password',)
#         }),
#         ('Служебная информаци', {
#             'fields': ('is_active', 'is_staff', 'is_admin', 'is_superuser')
#         }),
#     )


@admin.register(Account)
class AccountAdmin(UserAdmin):
    list_display = ('email', 'phone', 'username', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username',)
    readonly_fields = ('date_joined', 'last_login')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()