# Generated by Django 5.1.2 on 2024-11-03 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0005_transaction_subtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='date',
            field=models.DateTimeField(),
        ),
    ]