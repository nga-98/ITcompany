# Generated by Django 2.2.4 on 2020-04-05 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0032_employee_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='EmpPost',
        ),
        migrations.AlterField(
            model_name='employee',
            name='Post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IT_company.Post', verbose_name='Должность'),
        ),
    ]