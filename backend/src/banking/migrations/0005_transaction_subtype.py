# Generated by Django 5.1.2 on 2024-11-03 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0004_alter_userbank_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='subtype',
            field=models.CharField(max_length=30, null=True),
        ),
    ]