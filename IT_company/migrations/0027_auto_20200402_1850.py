# Generated by Django 2.2.4 on 2020-04-02 15:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0026_auto_20200402_1821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='OrderDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 15, 50, 2, 485478, tzinfo=utc), verbose_name='Дата заказа'),
        ),
    ]
