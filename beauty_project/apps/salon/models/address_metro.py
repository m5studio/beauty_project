from django.db import models

from apps.salon.models.address_city import AddressCity


class AddressMetro(models.Model):
    city          = models.ForeignKey(AddressCity, verbose_name='Город', on_delete=models.CASCADE)
    metro_station = models.CharField('Станция метро', max_length=255, blank=True, null=True)