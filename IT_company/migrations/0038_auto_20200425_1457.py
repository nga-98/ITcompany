# Generated by Django 2.2.4 on 2020-04-25 11:57

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0037_auto_20200413_1333'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PaymentType', models.CharField(choices=[('Карта', 'Карта'), ('Электронный кошелёк', 'Электронный кошелёк'), ('Наличные', 'Наличные')], max_length=50, verbose_name='Тип оплаты')),
                ('PaymentName', models.CharField(max_length=100, verbose_name='Наименование оплаты')),
            ],
            options={
                'verbose_name': 'Способ оплаты',
                'verbose_name_plural': 'Способы оплаты',
            },
        ),
        migrations.RemoveField(
            model_name='client',
            name='ClientAccount',
        ),
        migrations.AlterField(
            model_name='order',
            name='OrderDate',
            field=models.DateField(default=datetime.date(2020, 4, 25), verbose_name='Дата заказа'),
        ),
        migrations.AddField(
            model_name='order',
            name='PaymentMethod',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IT_company.PaymentMethod', verbose_name='Способ оплаты'),
        ),
    ]
