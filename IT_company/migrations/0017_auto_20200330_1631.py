# Generated by Django 2.2.4 on 2020-03-30 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0016_auto_20200329_2241'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ClientName', models.CharField(max_length=100, verbose_name='Имя')),
                ('ClientSurname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('ClientPatronymic', models.CharField(max_length=100, verbose_name='Отчество')),
                ('ClientPhone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('ClientEmail', models.CharField(max_length=50, verbose_name='E-mail')),
                ('ClientAccount', models.CharField(max_length=100, verbose_name='Счёт')),
            ],
        ),
        migrations.AddField(
            model_name='servicetype',
            name='slug',
            field=models.SlugField(default='', max_length=200),
        ),
    ]
