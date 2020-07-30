# Generated by Django 3.0.8 on 2020-07-30 13:06

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('salon', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Actions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, help_text='Опубликован на сайте?', verbose_name='Активный')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок акции')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('discount', models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Скидка')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('salon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='salon.Salon', verbose_name='Салон')),
            ],
            options={
                'verbose_name': 'Акция',
                'verbose_name_plural': 'Акции',
            },
        ),
    ]
