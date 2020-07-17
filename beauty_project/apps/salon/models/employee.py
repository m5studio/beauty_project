from django.db import models
from apps.salon.models.salon import Salon
from apps.services.models import Services


class Employee(models.Model):
    active     = models.BooleanField('Активный', default=True, help_text='Опубликован на сайте?')
    salon      = models.ForeignKey(Salon, verbose_name='Салон', on_delete=models.SET_NULL, null=True)

    name       = models.CharField('Имя', max_length=255)
    surname    = models.CharField('Фамилия', max_length=255, blank=True, null=True)
    patronymic = models.CharField('Отчество', max_length=255, blank=True, null=True)

    services   = models.ManyToManyField(Services, blank=True, verbose_name='Услуги')

    created    = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated    = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'