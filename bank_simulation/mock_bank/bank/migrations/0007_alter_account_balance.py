# Generated by Django 5.1.3 on 2024-11-19 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bank", "0006_alter_transaction_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="account",
            name="balance",
            field=models.FloatField(default=0),
        ),
    ]