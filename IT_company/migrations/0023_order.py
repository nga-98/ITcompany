# Generated by Django 2.2.4 on 2020-03-31 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0022_remove_itservice_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('OrderDate', models.DateField(verbose_name='Дата заказа')),
                ('OrderRequirement', models.TextField(verbose_name='Требования')),
                ('OrderStatus', models.CharField(choices=[('Создан', 'Создан'), ('Обрабатывается', 'Обрабатывается'), ('Выполнен', 'Выполнен')], default='Создан', max_length=50, verbose_name='Статус заказа')),
                ('Client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='IT_company.Client', verbose_name='Заказчик')),
                ('Employee', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='IT_company.Employee', verbose_name='Ответственный сотрудник')),
            ],
        ),
    ]
