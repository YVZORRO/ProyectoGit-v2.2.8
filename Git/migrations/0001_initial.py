# Generated by Django 5.1 on 2024-08-28 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='novedades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('Observaciones', models.TextField(null=True, verbose_name='Observaciones')),
                ('Descripcion', models.TextField(null=True, verbose_name='Descripción')),
                ('FechaObservacion', models.TextField(null=True, verbose_name='Fecha observación')),
                ('Coordinador', models.TextField(null=True, verbose_name='Coordinador')),
                ('Tecnico', models.TextField(null=True, verbose_name='Tecnico')),
                ('Servicio', models.TextField(null=True, verbose_name='Servicio')),
            ],
        ),
    ]
