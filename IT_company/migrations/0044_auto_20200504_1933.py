# Generated by Django 2.2.4 on 2020-05-04 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0043_auto_20200504_1920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='ClientEmail',
            field=models.EmailField(max_length=50, verbose_name='E-mail'),
        ),
    ]
