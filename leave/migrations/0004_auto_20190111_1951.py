# Generated by Django 2.0.10 on 2019-01-11 14:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leave', '0003_auto_20190111_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='time',
            field=models.TimeField(default=datetime.time(14, 21, 17, 668827), null=True, verbose_name='Time'),
        ),
    ]