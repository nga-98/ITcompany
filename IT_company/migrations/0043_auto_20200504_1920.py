# Generated by Django 2.2.4 on 2020-05-04 16:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0042_remove_contract_contractsum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='EmpEmail',
            field=models.EmailField(max_length=50, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='order',
            name='OrderDate',
            field=models.DateField(default=datetime.date(2020, 5, 4), verbose_name='Дата заказа'),
        ),
    ]
