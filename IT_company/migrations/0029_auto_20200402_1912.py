# Generated by Django 2.2.4 on 2020-04-02 16:12

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('IT_company', '0028_auto_20200402_1850'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='User',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='OrderDate',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 2, 16, 12, 36, 158553, tzinfo=utc), verbose_name='Дата заказа'),
        ),
    ]
