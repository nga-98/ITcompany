# Generated by Django 2.2.4 on 2020-05-06 20:20

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0050_auto_20200506_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itservice',
            name='ServiceGaurantee',
            field=models.CharField(choices=[('6 месяцев', '6 месяцев'), ('12 месяцев', '12 месяцев'), ('24 месяца', '24 месяца'), ('36 месяцев', '36 месяцев')], max_length=100, verbose_name='Срок гарантии'),
        ),
        migrations.AlterField(
            model_name='itservice',
            name='ServicePeriod',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Период предоставления услуги'),
        ),
        migrations.AlterField(
            model_name='order',
            name='OrderDate',
            field=models.DateField(default=datetime.datetime(2020, 5, 6, 20, 20, 6, 537221, tzinfo=utc), verbose_name='Дата заказа'),
        ),
    ]
