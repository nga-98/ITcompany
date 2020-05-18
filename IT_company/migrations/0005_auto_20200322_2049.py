# Generated by Django 2.2.4 on 2020-03-22 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0004_auto_20200322_2040'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='Department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IT_company.Department', verbose_name='Отдел'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='EmpEmail',
            field=models.CharField(max_length=50, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='EmpPhone',
            field=models.CharField(max_length=20, verbose_name='Телефон'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='EmpPost',
            field=models.CharField(max_length=200, verbose_name='Доложность'),
        ),
    ]