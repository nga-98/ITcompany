# Generated by Django 2.2.4 on 2020-04-02 10:34

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0024_order_itservice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='OrderDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 10, 34, 41, 35624, tzinfo=utc), verbose_name='Дата заказа'),
        ),
    ]
