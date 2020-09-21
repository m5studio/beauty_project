from django.db import models


class AddressCity(models.Model):
    city = models.CharField('Город', max_length=255)