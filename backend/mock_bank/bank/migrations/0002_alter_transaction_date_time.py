# Generated by Django 5.1.2 on 2024-11-05 19:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date_time',
            field=models.DateTimeField(
                default=datetime.datetime(2024, 11, 5, 22, 47, 4, 664757)),
        ),
    ]
