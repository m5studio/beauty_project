from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Services(MPTTModel):
    name   = models.CharField('Название', max_length=255, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children', verbose_name='Родитель')

    price  = models.DecimalField('Цена', max_digits=10, decimal_places=2, blank=True, null=True)

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'

    def __str__(self):
        return self.name

"""
class Services(models.Model):
    name  = models.CharField('Название услуги', max_length=255)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)

    class Meta:
        # db_table = "services"
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
"""