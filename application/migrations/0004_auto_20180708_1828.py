# Generated by Django 2.0.7 on 2018-07-08 16:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_auto_20180708_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='connectionobject',
            name='obj_timestamp',
            field=models.TimeField(verbose_name=datetime.datetime(2018, 7, 8, 18, 28, 20, 721648)),
        ),
    ]
