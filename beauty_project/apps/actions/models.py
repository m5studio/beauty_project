from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from apps.salon.models.salon import Salon


class Actions(models.Model):
    active      = models.BooleanField('Активный', default=True, help_text='Опубликован на сайте?')
    salon       = models.ForeignKey(Salon, on_delete=models.SET_NULL, null=True, verbose_name='Салон')
    title       = models.CharField('Заголовок акции', max_length=255)
    description = models.TextField('Описание', blank=True, null=True)

    discount    = models.PositiveIntegerField('Скидка', blank=True, null=True, \
                                                validators=[MinValueValidator(1), MaxValueValidator(100)])

    created     = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated     = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Акция'
        verbose_name_plural = 'Акции'
