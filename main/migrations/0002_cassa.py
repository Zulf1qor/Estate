# Generated by Django 5.0.2 on 2024-03-03 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cassa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('total_balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.location')),
            ],
        ),
    ]