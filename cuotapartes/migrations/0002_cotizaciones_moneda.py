# Generated by Django 4.2.13 on 2024-07-11 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cuotapartes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cotizaciones',
            name='moneda',
            field=models.CharField(choices=[('ARS', 'ARS'), ('USD', 'USD')], default='ARS', max_length=200),
        ),
    ]