from django.contrib import admin

from apps.salon.models.salon import Salon
from apps.salon.models.employee import Employee
from apps.salon.models.work_schedule import WorkSchedule


class EmployeeInline(admin.TabularInline):
    model = Employee
    extra = 1
    max_num = 100


class WorkScheduleInline(admin.TabularInline):
    model = WorkSchedule
    extra = 7
    max_num = 7


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    inlines = [
        EmployeeInline,
        WorkScheduleInline,
    ]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    pass