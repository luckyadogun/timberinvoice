# Generated by Django 2.1.15 on 2020-01-19 20:29

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200116_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='vat',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
