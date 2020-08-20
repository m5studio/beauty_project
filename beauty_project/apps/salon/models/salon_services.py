from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

from apps.salon.models.salon import Salon
from apps.services.models import Services


class SalonServices(models.Model):
# class SalonServices(MPTTModel):
    salon   = models.ForeignKey(Salon, verbose_name='Салон', on_delete=models.SET_NULL, null=True)

    service = models.ForeignKey(Services, on_delete=models.CASCADE, verbose_name="Услуга")
    # parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    price   = models.DecimalField('Цена', max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"{self.salon} {self.service}"

    class Meta:
        verbose_name = 'Услуга Салона'
        verbose_name_plural = 'Услуги Салонов'