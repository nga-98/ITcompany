# Generated by Django 2.2.4 on 2020-04-05 22:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0030_auto_20200404_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PostName', models.CharField(max_length=200, verbose_name='Название должности')),
                ('PostSalary', models.FloatField(verbose_name='Оклад')),
            ],
        ),
        migrations.AlterField(
            model_name='order',
            name='OrderDate',
            field=models.DateField(default=datetime.date(2020, 4, 6), verbose_name='Дата заказа'),
        ),
    ]
