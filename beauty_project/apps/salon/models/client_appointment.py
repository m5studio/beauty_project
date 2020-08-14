from django.db import models

from apps.account.models import Account
from apps.services.models import Services

from apps.salon.models.salon import Salon
from apps.salon.models.employee import Employee


class ClientAppointment(models.Model):
    client   = models.ForeignKey(Account, verbose_name='Клиент', on_delete=models.SET_NULL, null=True)
    employee = models.ForeignKey(Employee, verbose_name='Мастер', on_delete=models.SET_NULL, null=True)
    services = models.ManyToManyField(Services, verbose_name='Услуга', blank=True)
    datetime = models.DateTimeField('Дата и время записи', blank=True, null=True)
    comment  = models.TextField('Комментарий', blank=True, null=True)

    created  = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated  = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.client.first_name

    class Meta:
        verbose_name = 'Запись Клиента'
        verbose_name_plural = 'Записи Клиентов'