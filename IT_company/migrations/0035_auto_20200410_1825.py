# Generated by Django 2.2.4 on 2020-04-10 15:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0034_auto_20200409_0056'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='branches',
            options={'verbose_name': 'Филиал', 'verbose_name_plural': 'Филиалы'},
        ),
        migrations.AlterField(
            model_name='branches',
            name='BranchAddress',
            field=models.TextField(verbose_name='Адрес филиала'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='BranchName',
            field=models.CharField(max_length=200, verbose_name='Название филиала'),
        ),
        migrations.AlterField(
            model_name='branches',
            name='BranchPhone',
            field=models.CharField(max_length=20, verbose_name='Телефон филиала'),
        ),
        migrations.AlterField(
            model_name='department',
            name='Branch',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IT_company.Branches', verbose_name='Филиал'),
        ),
        migrations.AlterField(
            model_name='department',
            name='DepartmentName',
            field=models.CharField(max_length=200, verbose_name='Название отдела'),
        ),
        migrations.AlterField(
            model_name='department',
            name='DepartmentNumber',
            field=models.IntegerField(verbose_name='Номер отдела'),
        ),
        migrations.AlterField(
            model_name='order',
            name='OrderDate',
            field=models.DateField(default=datetime.date(2020, 4, 10), verbose_name='Дата заказа'),
        ),
    ]