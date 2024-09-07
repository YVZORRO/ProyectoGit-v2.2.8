# Generated by Django 4.1.3 on 2024-08-30 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Git', '0018_contrato'),
    ]

    operations = [
        migrations.CreateModel(
            name='clientes',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Nombres')),
                ('solicitante', models.CharField(max_length=100, null=True, verbose_name='Solicitante')),
                ('telefono', models.CharField(max_length=100, null=True, verbose_name='Telefono')),
            ],
        ),
        migrations.CreateModel(
            name='novedades_th',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_novedad', models.TextField(null=True, verbose_name='Tipo Novedad')),
                ('fecha_inicio', models.DateTimeField(null=True, verbose_name='Fecha Inicio')),
                ('descripcion', models.TextField(null=True, verbose_name='Descripción')),
                ('tipo_incapacidad', models.CharField(max_length=100, null=True, verbose_name='Tipo Incapacidad')),
            ],
        ),
        migrations.DeleteModel(
            name='contratos',
        ),
    ]
