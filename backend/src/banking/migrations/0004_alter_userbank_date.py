# Generated by Django 5.1.2 on 2024-11-02 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0003_remove_userbank_access_remove_userbank_refresh_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userbank',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
