# Generated by Django 5.1 on 2024-08-29 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Git', '0007_rename_coordinador_novedades_coordinador_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='novedades',
            name='fecha_observacion',
            field=models.DateTimeField(null=True, verbose_name='Fecha observación'),
        ),
    ]
