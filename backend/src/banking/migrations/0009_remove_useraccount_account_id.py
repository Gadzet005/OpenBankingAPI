# Generated by Django 5.1.3 on 2024-11-08 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('banking', '0008_useraccount_delete_userbank'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraccount',
            name='account_id',
        ),
    ]