# Generated by Django 4.1.3 on 2024-08-30 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Git', '0015_contratos'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('tipo_documento', models.CharField(max_length=50, null=True, verbose_name='Tipo de Documento')),
                ('documento', models.CharField(max_length=50, null=True, unique=True, verbose_name='Documento')),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=100, null=True, verbose_name='Apellido')),
                ('telefono', models.CharField(max_length=15, null=True, verbose_name='Teléfono')),
                ('nombre_contacto_emergencia', models.CharField(max_length=100, null=True, verbose_name='Nombre Contacto Emergencia')),
                ('telefono_emergencia', models.CharField(max_length=15, null=True, verbose_name='Teléfono Emergencia')),
                ('parentesco', models.CharField(max_length=50, null=True, verbose_name='Parentesco')),
                ('direccion', models.CharField(max_length=255, null=True, verbose_name='Dirección')),
                ('correo', models.EmailField(max_length=100, null=True, verbose_name='Correo')),
                ('estado', models.CharField(max_length=50, null=True, verbose_name='Estado')),
                ('vinculacion', models.CharField(max_length=100, null=True, verbose_name='Vinculación')),
                ('fecha_nacimiento', models.DateField(null=True, verbose_name='Fecha Nacimiento')),
                ('contrasena', models.CharField(max_length=128, null=True, verbose_name='Contraseña')),
                ('especialidad', models.CharField(max_length=100, null=True, verbose_name='Especialidad')),
                ('municipio', models.CharField(max_length=100, null=True, verbose_name='Municipio')),
            ],
        ),
    ]
