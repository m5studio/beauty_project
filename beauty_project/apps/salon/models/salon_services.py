from django.db import models

from apps.salon.models.salon import Salon
from apps.services.models import Services


class SalonServices(models.Model):
    salon   = models.ForeignKey(Salon, verbose_name='Салон', on_delete=models.SET_NULL, null=True)
    service = models.ForeignKey(Services, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Услуга")
    price   = models.DecimalField('Цена', max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.service.name

    class Meta:
        verbose_name = 'Услуга Салона'
        verbose_name_plural = 'Услуги Салонов'