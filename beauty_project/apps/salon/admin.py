from django.contrib import admin

from .models.salon import Salon
from .models.employee import Employee
from .models.work_schedule import WorkSchedule


class WorkScheduleInline(admin.TabularInline):
    model = WorkSchedule
    extra = 7
    max_num = 7


@admin.register(Salon)
class SalonAdmin(admin.ModelAdmin):
    inlines = [
        WorkScheduleInline,
    ]


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(WorkSchedule)
class WorkScheduleAdmin(admin.ModelAdmin):
    pass