from typing import Any
from django.db import models
from django.core.validators import MinValueValidator

class Novedad(models.Model):
    id = models.AutoField(primary_key=True)
    observaciones = models.TextField(max_length=100,verbose_name='Observaciones', null=True)
    descripcion = models.TextField(max_length=100,verbose_name='Descripción', null=True)
    fecha_observacion = models.DateField(verbose_name='Fecha observación', null=True)
    coordinador = models.CharField(max_length=100, verbose_name='Coordinador', null=True)
    tecnico = models.CharField(max_length=100, verbose_name='Técnico', null=True)
    servicio = models.CharField(max_length=100, verbose_name='Servicio', null=True)

    def __str__(self):
        return f"Observaciones: {self.observaciones} _ Descripción: {self.descripcion}"

class asignar(models.Model):
    id = models.AutoField(primary_key=True)
    glpi = models.CharField(max_length=100, verbose_name='GLPI', null=True)
    caso_cliente = models.CharField(max_length=45, verbose_name='Caso Cliente', null=True)
    descripcion = models.TextField(max_length=255, verbose_name='Descripción', null=True)
    cantidad_equipos = models.SmallIntegerField(verbose_name='Cantidad Equipos', null=True, validators=[MinValueValidator(1)])
    fecha_solicitud = models.DateField(verbose_name='Fecha Solicitud', null=True)
    fecha_programacion = models.DateField(verbose_name='Fecha Programación', null=True)
    fecha_cierre = models.DateField(verbose_name='Fecha Cierre', null=True)
    tiempo_desplazamiento = models.DecimalField(verbose_name='Tiempo Desplazamiento (horas)', max_digits=5, decimal_places=2, null=True, validators=[MinValueValidator(0)])
    direccion = models.CharField(max_length=60, verbose_name='Direccion', null=True)
    unidad = models.CharField(max_length=60, verbose_name='Unidad', null=True)
    municipio = models.CharField(max_length=60, verbose_name='Municipio', null=True)
    tipo_servicio = models.CharField(max_length=60, verbose_name='Tipo Servicio', null=True)
    cliente = models.CharField(max_length=60, verbose_name='Cliente', null=True)

    def __str__(self):
        return f"Caso Cliente: {self.caso_cliente} _ Descripción: {self.descripcion}"
    

#Talento Humano
#Empleado formulario
class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_documento = models.CharField(max_length=50, verbose_name='Tipo de Documento', null=True)
    documento = models.CharField(max_length=50, verbose_name='Documento', null=True, unique=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre', null=True)
    apellido = models.CharField(max_length=100, verbose_name='Apellido', null=True)
    telefono = models.CharField(max_length=15, verbose_name='Teléfono', null=True)
    nombre_contacto_emergencia = models.CharField(max_length=100, verbose_name='Nombre Contacto Emergencia', null=True)
    telefono_emergencia = models.CharField(max_length=15, verbose_name='Teléfono Emergencia', null=True)
    parentesco = models.CharField(max_length=50, verbose_name='Parentesco', null=True)
    direccion = models.CharField(max_length=255, verbose_name='Dirección', null=True)
    correo = models.EmailField(max_length=100, verbose_name='Correo', null=True)
    estado = models.CharField(max_length=50, verbose_name='Estado', null=True)
    vinculacion = models.CharField(max_length=100, verbose_name='Vinculación', null=True)
    fecha_nacimiento = models.DateField(verbose_name='Fecha de Nacimiento', null=True)
    contrasena = models.CharField(max_length=128, verbose_name='Contraseña', null=True)
    especialidad = models.CharField(max_length=100, verbose_name='Especialidad', null=True)
    municipio = models.CharField(max_length=100, verbose_name='Municipio', null=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.tipo_documento}: {self.documento}"

#Contrato formulario
class Contrato(models.Model):
    fecha_inicio = models.DateField(verbose_name='Fecha Inicio')
    fecha_fin = models.DateField(verbose_name='Fecha Fin')
    tipo_contrato = models.CharField(max_length=100, verbose_name='Tipo de Contrato')
    salario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Salario')
    fecha_pago = models.DateField(verbose_name='Fecha de Pago')
    numero_cuenta = models.CharField(max_length=20, verbose_name='Número de Cuenta')
    funcion = models.CharField(max_length=100, verbose_name='Función')
    cargo = models.CharField(max_length=100, verbose_name='Cargo')
    estado = models.CharField(max_length=50, verbose_name='Estado')
    numero_caso = models.CharField(max_length=50, verbose_name='Número de Caso')
    horario = models.CharField(max_length=100, verbose_name='Horario')
    entidad_financiera = models.CharField(max_length=100, verbose_name='Entidad Financiera')
    cliente_empresa = models.CharField(max_length=100, verbose_name='Cliente Empresa')
    aporte = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Aporte')

    def __str__(self):
        return f"Contrato {self.numero_caso} - {self.cliente_empresa}"

#Cliente formulario
class clientes(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombres', null=True)
    solicitante = models.CharField(max_length=100, verbose_name='Solicitante', null=True)
    telefono = models.CharField(max_length=15, verbose_name='Telefono', null=True)

    def __str__(self):
        return f"Nombres: {self.nombre}"
    

#Novedades formulario
class novedades_th(models.Model):
    id = models.AutoField(primary_key=True)
    tipo_novedad = models.TextField(max_length=100, verbose_name='Tipo Novedad', null=True)
    fecha_inicio = models.DateField(verbose_name='Fecha Inicio', null=True)
    descripcion = models.TextField(max_length=100, verbose_name='Descripción', null=True)
    tipo_incapacidad = models.CharField(max_length=100, verbose_name='Tipo Incapacidad', null=True)

    def __str__(self):
        return f"Tipo Novedad: {self.tipo_novedad}"

# Empresa Aporte Modelo
class empresaAporte(models.Model):
    id = models.AutoField(primary_key=True)
    entidad = models.CharField(max_length=100, verbose_name='Entidad', null=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre', null=True)
    estado = models.CharField(max_length=50, verbose_name='Estado', null=True)

    def __str__(self):
        return f"Entidad: {self.entidad} - Nombre: {self.nombre}"
    