# Generated by Django 2.2.4 on 2020-03-21 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branches',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BranchName', models.CharField(max_length=200)),
                ('BranchPhone', models.CharField(max_length=20)),
                ('BranchAddress', models.TextField()),
            ],
        ),
    ]