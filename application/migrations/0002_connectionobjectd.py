# Generated by Django 2.0.7 on 2018-07-08 15:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConnectionObjectd',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('obj_name', models.CharField(max_length=200)),
                ('obj_value', models.CharField(max_length=200)),
                ('obj_timestamp', models.TimeField(verbose_name=datetime.datetime(2018, 7, 8, 17, 57, 4, 934493))),
            ],
        ),
    ]