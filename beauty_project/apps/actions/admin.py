from django.contrib import admin
from apps.actions.models import Actions


@admin.register(Actions)
class ActionsAdmin(admin.ModelAdmin):
    search_fields = ['username']