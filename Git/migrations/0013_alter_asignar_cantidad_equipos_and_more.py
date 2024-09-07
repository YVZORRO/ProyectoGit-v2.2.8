# Generated by Django 5.1 on 2024-08-29 17:06

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Git', '0012_alter_asignar_cantidad_equipos_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asignar',
            name='cantidad_equipos',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Cantidad Equipos'),
        ),
        migrations.AlterField(
            model_name='asignar',
            name='tiempo_desplazamiento',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Tiempo Desplazamiento (horas)'),
        ),
    ]
