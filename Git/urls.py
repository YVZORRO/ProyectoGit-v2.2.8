from django.urls import path
from . import views

urlpatterns =[
    path('', views.inicio, name='inicio'),
    path('', views.VolverInicio, name='VolverInicio'),


    #Servicio tecnico
    #Asignar
    path('AsignarTabla', views.AsignarTabla, name='AsignarTabla'),
    path('Asignar', views.Asignar, name='Asignar'),
    path('eliminarAsignar/<int:id>', views.eliminarAsignar, name='eliminarAsignar'),
    path('editarAsignar/<int:id>', views.editarAsignar, name='editarAsignar'),
    path('verAsignar/<int:id>', views.verAsignar, name='verAsignar'),
    
    #Novedades
    path('Novedades', views.Novedades, name='Novedades'),
    path('NovedadesTabla', views.NovedadesTabla, name='NovedadesTabla'),
    path('eliminarNovedades/<int:id>', views.eliminarNovedades, name='eliminarNovedades'),
    path('editarNovedades/<int:id>', views.editarNovedades, name='editarNovedades'),
    path('VerNovedades/<int:id>', views.VerNovedades, name='VerNovedades'),
 
    
    #Talento humano
    #Empleado
    path('empleado', views.empleado, name='empleado'),
    path('EmpleadoTabla', views.EmpleadoTabla, name='EmpleadoTabla'),
    path('eliminarEmpleado/<int:id>', views.eliminarEmpleado, name='eliminarEmpleado'),
    path('editarEmpleado/<int:id>', views.editarEmpleado, name='editarEmpleado'),
    path('VerEmpleado/<int:id>', views.VerEmpleado, name='VerEmpleado'),
    #Cliente
    path('cliente', views.cliente, name='cliente'),
    path('ClienteTabla', views.ClienteTabla, name='ClienteTabla'),
    path('eliminarCliente/<int:id>', views.eliminarCliente, name='eliminarCliente'),
    path('editarCliente/<int:id>', views.editarCliente, name='editarCliente'),
    path('VerCliente/<int:id>', views.VerCliente, name='VerCliente'),
    #Contrato
    path('contrato', views.contrato, name='contrato'),
    path('ContratoTabla', views.ContratoTabla, name='ContratoTabla'),
    path('eliminarContrato/<int:id>', views.eliminarContrato, name='eliminarContrato'),
    path('editarContrato/<int:id>', views.editarContrato, name='editarContrato'),
    path('VerContrato/<int:id>', views.VerContrato, name='VerContrato'),
    #Novedades
    path('novedades', views.novedades, name='novedades'),
    path('NovedadesTablaTh', views.NovedadesTablaTh, name='NovedadesTablaTh'),
    path('eliminarNovedad/<int:id>', views.eliminarNovedad, name='eliminarNovedad'),
    path('editarNovedadesTh/<int:id>', views.editarNovedadesTh, name='editarNovedadesTh'),
    path('VerNovedadesTh/<int:id>', views.VerNovedadesTh, name='VerNovedadesTh'),
    #Empresa Aporte
    path('EmpresaAporte', views.EmpresaAporte, name='EmpresaAporte'),
    path('eliminarEmpresaA/<int:id>', views.eliminarEmpresaA, name='eliminarEmpresaA'),
    path('editarEmpresaA/<int:id>', views.editarEmpresaA, name='editarEmpresaA'),
]
