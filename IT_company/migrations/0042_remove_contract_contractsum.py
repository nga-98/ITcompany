# Generated by Django 2.2.4 on 2020-05-01 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0041_auto_20200501_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='ContractSum',
        ),
    ]
