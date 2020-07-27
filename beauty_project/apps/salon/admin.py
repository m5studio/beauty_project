from django.contrib import admin

from apps.salon.models.salon import Salon
from apps.salon.models.employee import Employee
from apps.salon.models.work_schedule import WorkSchedule


# class EmployeeInline(admin.TabularInline):
#     model = Employee
#     extra = 1
#     max_num = 100


class WorkScheduleInline(admin.TabularInline):
    model = WorkSchedule
    extra = 7
    max_num = 7


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    inlines = [
        # EmployeeInline,
        WorkScheduleInline,
    ]

    fieldsets = (
        (None, {
            'fields': ('active', 'name', 'description')
        }),
        ('Контакты салона', {
            'fields': ('phone', 'email', 'site_url')
        }),
        ('Владелец', {
            'fields': ('owner',)
        }),
    )

    search_fields = ['name']
    # autocomplete_fields = ['owner']


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    readonly_fields = ('image_admin_thumb',)
    # list_display = ('surname', 'name', 'patronymic', 'salon',)
    list_display = ('__str__', 'salon',)

    fieldsets = (
        (None, {
            'fields': ('active',)
        }),
        ('ФИО', {
            'fields': ('surname', 'name', 'patronymic')
        }),
        ('Фото сотрудника', {
            'fields': ('image_admin_thumb', 'image')
        }),
        ('Салон\Услуги', {
            'fields': ('salon', 'services',)
        }),
    )

    autocomplete_fields = ['salon', 'services']


@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('salon',)
        }),
        ('График работы', {
            'fields': ('week_day', 'working_hours_from', 'working_hours_to',)
        }),
    )

    autocomplete_fields = ['salon',]