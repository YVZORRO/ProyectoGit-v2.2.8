# Generated by Django 5.1 on 2024-08-29 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Git', '0004_alter_novedades_fechaobservacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novedades',
            name='Coordinador',
        ),
        migrations.RemoveField(
            model_name='novedades',
            name='Descripcion',
        ),
        migrations.RemoveField(
            model_name='novedades',
            name='FechaObservacion',
        ),
        migrations.RemoveField(
            model_name='novedades',
            name='Observaciones',
        ),
        migrations.RemoveField(
            model_name='novedades',
            name='Servicio',
        ),
        migrations.RemoveField(
            model_name='novedades',
            name='Tecnico',
        ),
        migrations.AddField(
            model_name='novedades',
            name='fecha_observacion',
            field=models.DateField(blank=True, null=True, verbose_name='Fecha observación'),
        ),
        migrations.AddField(
            model_name='novedades',
            name='coordinador',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Coordinador'),
        ),
        migrations.AddField(
            model_name='novedades',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AddField(
            model_name='novedades',
            name='observaciones',
            field=models.TextField(blank=True, null=True, verbose_name='Observaciones'),
        ),
        migrations.AddField(
            model_name='novedades',
            name='servicio',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Servicio'),
        ),
        migrations.AddField(
            model_name='novedades',
            name='tecnico',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Técnico'),
        ),
    ]
