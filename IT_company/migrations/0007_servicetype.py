# Generated by Django 2.2.4 on 2020-03-22 22:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IT_company', '0006_auto_20200322_2112'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TypeName', models.CharField(max_length=200)),
                ('TypeDescription', models.TextField()),
            ],
        ),
    ]
