# Generated by Django 2.2.4 on 2020-05-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0040_auto_20200501_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='ContractSum',
            field=models.FloatField(blank=True, null=True, verbose_name='Сумма договора'),
        ),
    ]
