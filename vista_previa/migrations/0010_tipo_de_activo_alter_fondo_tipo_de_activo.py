# Generated by Django 4.2.13 on 2024-07-10 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vista_previa', '0009_pais_sede_alter_fondo_pais_sede'),
    ]

    operations = [
        migrations.CreateModel(
            name='tipo_de_activo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('codigo_interno', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='fondo',
            name='tipo_de_activo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vista_previa.tipo_de_activo'),
        ),
    ]
