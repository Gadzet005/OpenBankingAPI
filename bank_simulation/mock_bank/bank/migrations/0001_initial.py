# Generated by Django 5.1.2 on 2024-11-05 19:43

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=12, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.IntegerField(unique=True)),
                ('balance', models.FloatField()),
                ('bank', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, to='bank.bank')),
                ('user', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='bank.user')),
            ],
        ),
        migrations.CreateModel(
            name='Subscriptions',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField()),
                ('account_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE, to='bank.account')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('entertainment', 'Развлечения'), ('food', 'Еда'), (
                    'transport', 'Транспорт'), ('utilities', 'Коммунальные услуги'), ('transfer', 'Перевод')], max_length=30)),
                ('quantity', models.FloatField()),
                ('date_time', models.DateTimeField(
                    default=datetime.datetime(2024, 11, 5, 22, 43, 13, 561553))),
                ('account_from_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, related_name='account_from', to='bank.account')),
                ('account_to_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, related_name='account_to', to='bank.account')),
                ('bank_from_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, related_name='bank_from', to='bank.account')),
                ('bank_to_id', models.ForeignKey(
                    on_delete=django.db.models.deletion.PROTECT, related_name='bank_to', to='bank.account')),
            ],
        ),
    ]