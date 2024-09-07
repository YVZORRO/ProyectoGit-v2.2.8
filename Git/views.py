from django.shortcuts import render,redirect
from .models import Novedad,asignar, Contrato, Empleado, clientes,novedades_th,empresaAporte
from .forms import NovedadesForm, AsignarForm, ContratoForm, EmpleadoForm, ClienteForm, novedades_thForm, EmpresaAporteForm
from django.core.paginator import Paginator  #paginacion

#Inicio
def inicio(request):
    return render(request, 'menu.html')
def VolverInicio(request):
    return render(request, 'menu.html')

#Talento Humano
#--------------------------------------Empleado---------------------------------------------------------------
def EmpleadoTabla(request):
    EmpleadoTabla = Empleado.objects.all()
    paginacion = Paginator(EmpleadoTabla, 3)
    num_pagina = request.GET.get('page')
    EmpleadoTabla = paginacion.get_page(num_pagina)
    return render(request, 'talento_humano/EmpleadoTabla.html', {'EmpleadoTabla': EmpleadoTabla})
def empleado(request):
    formularioEmpleado = EmpleadoForm(request.POST or None, request.FILES or None)
    if formularioEmpleado.is_valid():
        formularioEmpleado.save()
        return redirect('EmpleadoTabla')
    return render(request, 'talento_humano/empleado.html', {'formularioEmpleado': formularioEmpleado})
def eliminarEmpleado(request, id):
    EmpleadoTabla=Empleado.objects.get(id=id)
    EmpleadoTabla.delete()
    return redirect('EmpleadoTabla')
def editarEmpleado(request, id):
    empleado_editar=Empleado.objects.get(id=id)
    formularioEmpleado=EmpleadoForm(request.POST or None, request.FILES or None, instance=empleado_editar)
    if formularioEmpleado.is_valid() and request.POST:
        formularioEmpleado.save()
        return redirect('EmpleadoTabla')
    return render(request, 'talento_humano/empleado.html', {'formularioEmpleado': formularioEmpleado})
def VerEmpleado(request, id):
    empleado_ver = Empleado.objects.get(id=id)
    formularioEmpleado = EmpleadoForm(instance=empleado_ver)
    return render(request, 'talento_humano/VerEmpleado.html', {'formularioEmpleado': formularioEmpleado})

#--------------------------------------Cliente---------------------------------------------------------------
def ClienteTabla(request):
    ClienteTabla = clientes.objects.all()
    paginacion = Paginator(ClienteTabla, 3)
    num_pagina = request.GET.get('page')
    ClienteTabla = paginacion.get_page(num_pagina)
    return render(request, 'talento_humano/ClienteTabla.html', {'ClienteTabla': ClienteTabla})
def cliente(request):
    formularioCliente = ClienteForm(request.POST or None, request.FILES or None)
    if formularioCliente.is_valid():
        formularioCliente.save()
        return redirect('ClienteTabla')
    return render(request, 'talento_humano/cliente.html', {'formularioCliente': formularioCliente})
def eliminarCliente(request, id):
    ClienteTabla=clientes.objects.get(id=id)
    ClienteTabla.delete()
    return redirect('ClienteTabla')
def editarCliente(request, id):
    cliente_editar=clientes.objects.get(id=id)
    formularioCliente=ClienteForm(request.POST or None, request.FILES or None, instance=cliente_editar)
    if formularioCliente.is_valid() and request.POST:
        formularioCliente.save()
        return redirect('ClienteTabla')
    return render(request, 'talento_humano/cliente.html', {'formularioCliente': formularioCliente})
def VerCliente(request, id):
    cliente_ver = clientes.objects.get(id=id)
    formularioCliente = ClienteForm(instance=cliente_ver)
    return render(request, 'talento_humano/VerCliente.html', {'formularioCliente': formularioCliente})

#--------------------------------------Contrato---------------------------------------------------------------
def ContratoTabla(request):
    ContratoTabla = Contrato.objects.all()  
    paginacion = Paginator(ContratoTabla, 1)
    num_pagina = request.GET.get('page')
    ContratoTabla = paginacion.get_page(num_pagina)
    return render(request, 'talento_humano/ContratoTabla.html', {'ContratoTabla': ContratoTabla})  
def contrato(request):
    formularioContrato = ContratoForm(request.POST or None, request.FILES or None)
    if formularioContrato.is_valid():
        formularioContrato.save()
        return redirect('ContratoTabla')
    return render(request, 'talento_humano/contrato.html', {'formularioContrato': formularioContrato})
def eliminarContrato(request, id):
    ContratoTabla=Contrato.objects.get(id=id)
    ContratoTabla.delete()
    return redirect('ContratoTabla')
def editarContrato(request, id):
    contrato_editar=Contrato.objects.get(id=id)
    formularioContrato=ContratoForm(request.POST or None, request.FILES or None, instance=contrato_editar)
    if formularioContrato.is_valid() and request.POST:
        formularioContrato.save()
        return redirect('ContratoTabla')
    return render(request, 'talento_humano/contrato.html', {'formularioContrato': formularioContrato})
def VerContrato(request, id):
    contrato_ver = Contrato.objects.get(id=id)
    formularioContrato = ContratoForm(instance=contrato_ver)
    return render(request, 'talento_humano/VerContrato.html', {'formularioContrato': formularioContrato})

#--------------------------------------Novedades---------------------------------------------------------------
def NovedadesTablaTh(request):
    NovedadesTablaTh = novedades_th.objects.all()  
    paginacion = Paginator(NovedadesTablaTh, 3)
    num_pagina = request.GET.get('page')
    NovedadesTablaTh = paginacion.get_page(num_pagina)    
    return render(request, 'talento_humano/NovedadesTablaTh.html', {'NovedadesTablaTh': NovedadesTablaTh})
def novedades(request):
    formularioNovedades = novedades_thForm(request.POST or None, request.FILES or None)
    if formularioNovedades.is_valid():
        formularioNovedades.save()
        return redirect('NovedadesTablaTh')
    return render(request, 'talento_humano/novedades.html', {'formularioNovedades': formularioNovedades})
def eliminarNovedad(request, id):
    NovedadesTablaTh=novedades_th.objects.get(id=id)
    NovedadesTablaTh.delete()
    return redirect('NovedadesTablaTh')
def editarNovedadesTh(request, id):
    novedades_editar=novedades_th.objects.get(id=id)
    formularioNovedades=novedades_thForm(request.POST or None, request.FILES or None, instance=novedades_editar)
    if formularioNovedades.is_valid() and request.POST:
        formularioNovedades.save()
        return redirect('NovedadesTablaTh')
    return render(request, 'talento_humano/novedades.html', {'formularioNovedades': formularioNovedades})
def VerNovedadesTh(request, id):
    novedadesTh_ver = novedades_th.objects.get(id=id)
    formularioNovedades = novedades_thForm(instance=novedadesTh_ver)
    return render(request, 'talento_humano/VerNovedadesTh.html', {'formularioNovedades': formularioNovedades})

#--------------------------------------Empresa Aporte---------------------------------------------------------------

def EmpresaAporte(request):
    formularioEmpresaA = EmpresaAporteForm(request.POST or None, request.FILES or None)
    if formularioEmpresaA.is_valid():
        formularioEmpresaA.save()
        return redirect('EmpleadoTabla')
    return render(request, 'talento_humano/empresaAporte.html', {'formularioEmpresaA': formularioEmpresaA})
def eliminarEmpresaA(request, id):
    EmpleadoTabla=empresaAporte.objects.get(id=id)
    EmpleadoTabla.delete()
    return redirect('EmpleadoTabla')
def editarEmpresaA(request, id):
    empresaA_editar=empresaAporte.objects.get(id=id)
    formularioEmpresaA=EmpresaAporteForm(request.POST or None, request.FILES or None, instance=empresaA_editar)
    if formularioEmpresaA.is_valid() and request.POST:
        formularioEmpresaA.save()
        return redirect('EmpleadoTabla')
    return render(request, 'talento_humano/empresaAporte.html', {'formularioEmpresaA': formularioEmpresaA})



#Servicio Tecnico
#--------------------------------------Asignar---------------------------------------------------------------
def AsignarTabla(request):
    # AsignarTabla = asignar.objects.all()
    AsignarTabla = asignar.objects.all()
    paginacion = Paginator(AsignarTabla, 3)
    num_pagina = request.GET.get('page')
    AsignarTabla = paginacion.get_page(num_pagina)
    return render(request, 'servicio_tecnico/AsignarTabla.html', {'AsignarTabla': AsignarTabla})
def Asignar(request):
    formularioAsignar = AsignarForm(request.POST or None, request.FILES or None)
    if formularioAsignar.is_valid():
        formularioAsignar.save()
        return redirect('AsignarTabla')
    return render(request, 'servicio_tecnico/Asignar.html', {'formularioAsignar': formularioAsignar})
def eliminarAsignar(request, id):
    AsignarTabla=asignar.objects.get(id=id)
    AsignarTabla.delete()
    return redirect('AsignarTabla')
def editarAsignar(request, id):
    asignar_editar=asignar.objects.get(id=id)
    formularioAsignar=AsignarForm(request.POST or None, request.FILES or None, instance=asignar_editar)
    if formularioAsignar.is_valid() and request.POST:
        formularioAsignar.save()
        return redirect('AsignarTabla')
    return render(request, 'servicio_tecnico/Asignar.html', {'formularioAsignar': formularioAsignar})
def verAsignar(request, id):
    asignar_ver = asignar.objects.get(id=id)
    formularioAsignar = AsignarForm(instance=asignar_ver)
    return render(request, 'servicio_tecnico/VerAsignar.html', {'formularioAsignar': formularioAsignar})


#--------------------------------------Novedades---------------------------------------------------------------
def NovedadesTabla(request):
    NovedadesTabla = Novedad.objects.all()
    
    paginacion = Paginator(NovedadesTabla, 3)
    num_pagina = request.GET.get('page')
    NovedadesTabla = paginacion.get_page(num_pagina)
       
    return render(request, 'servicio_tecnico/NovedadesTabla.html', {'NovedadesTabla': NovedadesTabla})
def Novedades(request):
    formularioNovedades = NovedadesForm(request.POST or None, request.FILES or None)
    if formularioNovedades.is_valid():
        formularioNovedades.save()
        return redirect('NovedadesTabla')
    return render(request, 'servicio_tecnico/Novedades.html', {'formularioNovedades': formularioNovedades})
def eliminarNovedades(request, id):
    NovedadesTabla=Novedad.objects.get(id=id)
    NovedadesTabla.delete()
    return redirect('NovedadesTabla')
def editarNovedades(request, id):
    novedades_editar=Novedad.objects.get(id=id)
    formularioNovedades=NovedadesForm(request.POST or None, request.FILES or None, instance=novedades_editar)
    if formularioNovedades.is_valid() and request.POST:
        formularioNovedades.save()
        return redirect('NovedadesTabla')
    return render(request, 'servicio_tecnico/Novedades.html', {'formularioNovedades': formularioNovedades})
def VerNovedades(request, id):
    novedades_ver = Novedad.objects.get(id=id)
    formularioNovedades = NovedadesForm(instance=novedades_ver)
    return render(request, 'servicio_tecnico/VerNovedades.html', {'formularioNovedades': formularioNovedades})
