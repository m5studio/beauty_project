from django.db import models


class Services(models.Model):
    name  = models.CharField('Название услуги', max_length=255)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    class Meta:
        # db_table = "services"
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'