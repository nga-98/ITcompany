# Generated by Django 2.2.4 on 2020-03-24 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0008_itservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EquipmentName', models.CharField(max_length=200)),
                ('EquipmentQuantity', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='itservice',
            name='Equipment',
            field=models.ManyToManyField(to='IT_company.Equipment', verbose_name='Необходимое оборудование'),
        ),
    ]
