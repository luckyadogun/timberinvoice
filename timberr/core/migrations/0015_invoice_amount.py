# Generated by Django 2.1.15 on 2020-01-19 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200119_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='amount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]