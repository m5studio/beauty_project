from django.db import models


class Address(models.Model):
    street   = models.CharField('Улица', max_length=255, blank=True, null=True)
    building = models.CharField('Номер дома', max_length=255, blank=True, null=True)