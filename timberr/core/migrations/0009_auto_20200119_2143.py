# Generated by Django 2.1.15 on 2020-01-19 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20200119_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='office_telephone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]