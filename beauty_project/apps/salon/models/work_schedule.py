from datetime import datetime

from django.db import models
from .salon import Salon


class WorkSchedule(models.Model):
    WEEK_DAYS = (
        (1, 'Понедельник'),
        (1, 'Вторник'),
        (1, 'Среда'),
        (1, 'Четверг'),
        (1, 'Пятница'),
        (1, 'Суббота'),
        (1, 'Воскресенье'),
    )

    salon              = models.ForeignKey(Salon, verbose_name='Салон', on_delete=models.CASCADE)
    week_day           = models.CharField('День недели', max_length=1, choices=WEEK_DAYS)
    # working_hours_from = models.TimeField('Рабочие часы С', default=datetime.time(datetime.now()))
    working_hours_from = models.TimeField('Рабочие часы С', default='09:00')
    working_hours_to   = models.TimeField('Рабочие часы ДО', default='19:00')

    def __str__(self):
        return self.week_day

    class Meta:
        verbose_name = 'График работы'
        verbose_name_plural = 'График работы'