# Generated by Django 3.1 on 2020-08-19 15:03

import apps.actions.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('salon', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Опубликован на сайте?', verbose_name='Активный')),
                ('action_type', models.CharField(blank=True, choices=[(0, 'Скидка на услугу'), (1, 'Скидка на услуги в определенные часы/дни'), (2, 'Скидка на первое посещение'), (3, 'Подарок'), (4, 'Подарок за первое посещение')], max_length=1, null=True, verbose_name='Тип акции')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок акции')),
                ('image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=apps.actions.models.image_upload_path)),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('discount', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('salon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salon.salon', verbose_name='Салон')),
                ('services', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.services', verbose_name='Услуги')),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
        ),
    ]
