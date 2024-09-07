from django import forms
from datetime import timedelta
from django.utils import timezone
from .models import Novedad, asignar, Contrato, Empleado, clientes, novedades_th, empresaAporte

#------------------------------------------------Servicio tecnico--------------------------------------------------------------
#Novedades
class NovedadesForm(forms.ModelForm):
    class Meta:
        model=Novedad
        fields = ['observaciones', 'descripcion', 'fecha_observacion', 'coordinador', 'tecnico', 'servicio']
        widgets = {
              'observaciones': forms.TextInput(attrs={'class': 'form-control'}),
              'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
              'fecha_observacion': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
              'coordinador': forms.TextInput(attrs={'class': 'form-control'}),
              'tecnico': forms.TextInput(attrs={'class': 'form-control'}),
              'servicio': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {            
            'observaciones': {
                'required': 'Las observaciones son obligatorias.',
                'max_length': 'Las observaciones no puden exceder los 100 caracteres.',
            },
            'descripcion': {
                'required': 'La descripcion es obligatoria.',
                'max_length': 'La descripcion no pude exceder los 100 caracteres.',
            },
            'fecha_observacion': {
                'required': 'La fecha de observacion es obligatoria.',
            },
            'coordinador': {
                'required': 'El coordinador es obligatoria.',
                'max_length': 'El coordinador no pude exceder los 100 caracteres.',
            },
            'tecnico': {
                'required': 'El tecnico es obligatoria.',
                'max_length': 'El tecnico no pude exceder los 100 caracteres.',
            },
            'servicio': {
                'required': 'El servicio es obligatorio.',
                'max_length': 'El servicio no pude exceder los 100 caracteres.',
            },
        }
        
    def clean_observaciones(self):
        data = self.cleaned_data.get('observaciones')
        if len(data) > 100:
            raise forms.ValidationError('Las observaciones no pueden superar los 100 caracteres.')
        return data
    
    def clean_descripcion(self):
        data = self.cleaned_data.get('descripcion')
        if len(data) > 100:
            raise forms.ValidationError('La descripcion no puede superar los 100 caracteres.')
        return data
    
    def clean_fecha_observacion(self):
        fecha_observacion = self.cleaned_data.get('fecha_observacion')
        if fecha_observacion and fecha_observacion < timezone.now().date():
            raise forms.ValidationError("La fecha de observacion no puede ser anterior a la fecha actual.")
        return fecha_observacion
      
    def clean_coordinador(self):
        data = self.cleaned_data.get('coordinador')
        if len(data) > 100:
            raise forms.ValidationError('El coordinador no puede superar los 100 caracteres.')
        return data
    
    def clean_tecnico(self):
        data = self.cleaned_data.get('tecnico')
        if len(data) > 100:
            raise forms.ValidationError('El tecnico no puede superar los 100 caracteres.')
        return data  
    
    def clean_servicio(self):
        data = self.cleaned_data.get('servicio')
        if len(data) > 100:
            raise forms.ValidationError('El servicio no puede superar los 100 caracteres.')
        return data  
    
#Asignar
class AsignarForm(forms.ModelForm):
    class Meta:
        model = asignar
        fields = [
            'glpi', 'caso_cliente', 'descripcion', 'cantidad_equipos',
            'fecha_solicitud', 'fecha_programacion', 'fecha_cierre',
            'tiempo_desplazamiento', 'direccion', 'unidad', 'municipio',
            'tipo_servicio', 'cliente'
        ]
        widgets = {
            'glpi': forms.TextInput(attrs={'class': 'form-control'}),
            'caso_cliente': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_equipos': forms.NumberInput(attrs={'class': 'form-control', 'min': '1', 'step': '1'}),
            'fecha_solicitud': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'fecha_programacion': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'fecha_cierre': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'tiempo_desplazamiento': forms.NumberInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'unidad': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_servicio': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {            
            'glpi': {
                'required': 'El caso GLPI es obligatorio.',
                'max_length': 'El caso GLPI no puede exceder los 100 caracteres.',
            },
            'caso_cliente': {
                'required': 'El Caso Cliente es obligatorio.',
                'max_length': 'Caso Cliente solo puede tener 45 caracteres.',
            },
            'descripcion': {
                'required': 'La descripción es obligatoria.',
                'max_length': 'La descripción solo puede tener 255 caracteres.',
            },
            'cantidad_equipos': {
                'required': 'La cantidad de equipos es obligatoria.',
            },
            'fecha_solicitud': {
                'required': 'La fecha de solicitud es obligatoria.',
            },
            'fecha_programacion': {
                'required': 'La fecha de programacion es obligatoria.',
            },
            ###############################################333
            'direccion': {
                'required': 'La direccion es obligatoria.',
                'max_length': 'La direccion solo puede tener 60 caracteres.',
            },
            'unidad': {
                'required': 'La unidad es obligatoria.',
                'max_length': 'La unidad solo puede tener 60 caracteres.',
            },
            'municipio': {
                'required': 'El municipio es obligatoria.',
                'max_length': 'El municipio solo puede tener 60 caracteres.',
            },
            'tipo_servicio': {
                'required': 'El tipo de servicio es obligatoria.',
                'max_length': 'El tipo de servicio solo puede tener 60 caracteres.',
            },
            'cliente': {
                'required': 'El cliente es obligatoria.',
                'max_length': 'El cliente solo puede tener 60 caracteres.',
            },
        }     

    def clean_glpi(self): 
        data = self.cleaned_data['glpi']
        try:
            glpi = int(data)
            if glpi < 0:
                raise forms.ValidationError('Caso GLPI debe ser un número positivo.')
            else:
                return int(data)
        except ValueError:
            raise forms.ValidationError('Caso GLPI debe ser un número entero.')
        
    def clean_caso_cliente(self):
        data = self.cleaned_data.get('caso_cliente')
        if len(data) > 45:
            raise forms.ValidationError('Caso Cliente no puede superar los 45 caracteres.')
        return data
    
    def clean_descripcion(self):
        data = self.cleaned_data.get('descripcion')
        if len(data) > 255:
            raise forms.ValidationError('La descripcion no puede superar los 255 caracteres.')
        return data
    
    def clean_cantidad_equipos(self):
        data = self.cleaned_data.get('cantidad_equipos')
        if data is not None:
            if data < 1:
                raise forms.ValidationError('La cantidad de equipos debe ser al menos 1.')
            elif data > 999:
                raise forms.ValidationError('La cantidad de equipos no puede exceder 999.')
        return data
    
    def clean_fecha_solicitud(self):
        fecha_solicitud = self.cleaned_data.get('fecha_solicitud')
        hoy = timezone.now().date()
        limite_dias = hoy - timedelta(days=30)  # Calcula la fecha límite para un mes antes
        if fecha_solicitud:
            if fecha_solicitud < limite_dias:
                raise forms.ValidationError("La fecha de solicitud no puede ser anterior a un mes antes de la fecha actual.")        
        return fecha_solicitud

    def clean_fecha_programacion(self):
        fecha_programacion = self.cleaned_data.get('fecha_programacion')
        if fecha_programacion and fecha_programacion < timezone.now().date():
            raise forms.ValidationError("La fecha de programación no puede ser anterior a la fecha actual.")
        return fecha_programacion

    def clean_fecha_cierre(self):
        fecha_cierre = self.cleaned_data.get('fecha_cierre')
        fecha_programacion = self.cleaned_data.get('fecha_programacion')  # Usamos cleaned_data para obtener fecha_programacion
        if fecha_cierre and fecha_programacion and fecha_cierre < fecha_programacion:
            raise forms.ValidationError("La fecha de cierre no puede ser anterior a la fecha de programación.")
        return fecha_cierre
    
    ############################################################################# tiempo desplazamiento 
    def clean_direccion(self):
        data = self.cleaned_data.get('direccion')
        if len(data) > 60:
            raise forms.ValidationError('La direccion no puede superar los 60 caracteres.')
        return data

    def clean_unidad(self):
        data = self.cleaned_data.get('unidad')
        if len(data) > 60:
            raise forms.ValidationError('La unidad no puede superar los 60 caracteres.')
        return data

    def clean_municipio(self):
        data = self.cleaned_data.get('municipio')
        if len(data) > 60:
            raise forms.ValidationError('El municipio no puede superar los 60 caracteres.')
        return data
    
    def clean_tipo_servicio(self):
        data = self.cleaned_data.get('tipo_servicio')
        if len(data) > 60:
            raise forms.ValidationError('El tipo de servicio no puede superar los 60 caracteres.')
        return data
    
    def clean_cliente(self):
        data = self.cleaned_data.get('cliente')
        if len(data) > 60:
            raise forms.ValidationError('El cliente no puede superar los 60 caracteres.')
        return data


#------------------------------------------------Talento humano--------------------------------------------------------------
#Contrato
class ContratoForm(forms.ModelForm):
    class Meta:
        model = Contrato
        fields = ['fecha_inicio','fecha_fin','fecha_pago', 'tipo_contrato','salario','numero_cuenta','funcion','cargo','estado','numero_caso','horario','entidad_financiera','cliente_empresa','aporte']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'fecha_fin': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'fecha_pago': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),            
            'tipo_contrato': forms.TextInput(attrs={'class': 'form-control'}),
            'salario': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_cuenta': forms.TextInput(attrs={'class': 'form-control'}),
            'funcion': forms.TextInput(attrs={'class': 'form-control'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'numero_caso': forms.TextInput(attrs={'class': 'form-control'}),
            'horario': forms.TextInput(attrs={'class': 'form-control'}),
            'entidad_financiera': forms.TextInput(attrs={'class': 'form-control'}),
            'cliente_empresa': forms.TextInput(attrs={'class': 'form-control'}),
            'aporte': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'fecha_inicio': {
                'required': 'La fecha de inicio es obligatorio.',
            },
            'fecha_fin': {
                'required': 'La fecha de fin es obligatorio.',
            },
            'fecha_pago': {
                'required': 'La fecha de pago es obligatorio.',
            },
            'tipo_contrato': {
                'required': 'El tipo de contrato es obligatorio.',
                'max_length': 'El tipo de contrato no puden exceder los 100 caracteres',
            },
            'numero_cuenta': {
                'required': 'El numero de cuenta es obligatoria.',
                'max_length': 'El numero de cuenta no puden exceder los 20 caracteres',
            },
            'funcion': {
                'required': 'La funcion es obligatoria.',
                'max_length': 'La funcion no puden exceder los 100 caracteres',
            },
            'cargo': {
                'required': 'El cargo es obligatoria.',
                'max_length': 'El cargo no puden exceder los 100 caracteres',
            },
            'estado': {
                'required': 'El estado es obligatoria.',
                'max_length': 'El estado no puden exceder los 50 caracteres',
            },
            'numero_caso': {
                'required': 'El numero de caso es obligatoria.',
                'max_length': 'El numero de caso no puden exceder los 50 caracteres',
            },
            'horario': {
                'required': 'El horario es obligatoria.',
                'max_length': 'El horario no puden exceder los 100 caracteres',
            },
            'entidad_financiera': {
                'required': 'La entidad financiera es obligatoria.',
                'max_length': 'La entidad financiera no puden exceder los 100 caracteres',
            },
            'cliente_empresa': {
                'required': 'El cliente es obligatorio',
                'max_length': 'El cliente no puden exceder los 100 caracteres',
            },
        }
    
    def clean_fecha_inicio(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        if fecha_inicio and fecha_inicio < timezone.now().date():
            raise forms.ValidationError("La fecha de inicio no puede ser anterior a la fecha actual.")
        return fecha_inicio
    
    def clean_fecha_fin(self):
        fecha_fin = self.cleaned_data.get('fecha_fin')
        fecha_inicio = self.cleaned_data.get('fecha_inicio')  # Usamos cleaned_data para obtener fecha_programacion
        if fecha_fin and fecha_inicio and fecha_fin < fecha_inicio:
            raise forms.ValidationError("La fecha de fin no puede ser anterior a la fecha de inicio.")
        return fecha_fin
    
    def clean_fecha_pago(self):
        fecha_pago = self.cleaned_data.get('fecha_pago')
        if fecha_pago and fecha_pago < timezone.now().date():
            raise forms.ValidationError("La fecha de pago no puede ser anterior a la fecha actual.")
        return fecha_pago
    
    def clean_tipo_contrato(self):
        data = self.cleaned_data.get('tipo_contrato')
        if len(data) > 100:
            raise forms.ValidationError('El tipo de contrato no pude exceder los 100 caracteres')
        return data 
    
    def clean_numero_cuenta(self):
        data = self.cleaned_data.get('numero_cuenta')
        if len(data) > 20:
            raise forms.ValidationError('El numero de cuenta no puden exceder los 20 caracteres')
        return data 
    
    def clean_funcion(self):
        data = self.cleaned_data.get('funcion')
        if len(data) > 100:
            raise forms.ValidationError('La funcion no puden exceder los 100 caracteres')
        return data 
    
    def clean_cargo(self):
        data = self.cleaned_data.get('cargo')
        if len(data) > 100:
            raise forms.ValidationError('El cargo no puden exceder los 100 caracteres')
        return data 
    
    def clean_estado(self):
        data = self.cleaned_data.get('cargo')
        if len(data) > 50:
            raise forms.ValidationError('El estado no puden exceder los 50 caracteres')
        return data 
    
    def clean_numero_caso(self):
        data = self.cleaned_data.get('numero_caso')
        if len(data) > 50:
            raise forms.ValidationError('El numero de caso no puden exceder los 50 caracteres')
        return data 
    
    def clean_horario(self):
        data = self.cleaned_data.get('horario')
        if len(data) > 100:
            raise forms.ValidationError('El horario no puden exceder los 100 caracteres')
        return data 
    
    def clean_entidad_financiera(self):
        data = self.cleaned_data.get('entidad_financiera')
        if len(data) > 100:
            raise forms.ValidationError('La entidad financiera no puden exceder los 100 caracteres')
        return data 
    
    def clean_cliente_empresa(self):
        data = self.cleaned_data.get('cliente_empresa')
        if len(data) > 100:
            raise forms.ValidationError('El cliente no puden exceder los 100 caracteres')
        return data 
    
#Empleado
class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado  # Asegúrate de tener este modelo en tu archivo models.py
        fields = [
            'tipo_documento', 'documento', 'nombre', 'apellido', 'telefono',
            'nombre_contacto_emergencia', 'telefono_emergencia', 'parentesco',
            'direccion', 'correo', 'estado', 'vinculacion', 'fecha_nacimiento',
            'contrasena', 'especialidad', 'municipio'
        ]
        widgets = {
            'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre_contacto_emergencia': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono_emergencia': forms.TextInput(attrs={'class': 'form-control'}),
            'parentesco': forms.TextInput(attrs={'class': 'form-control'}),
            'direccion': forms.TextInput(attrs={'class': 'form-control'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control'}),
            'estado': forms.Select(attrs={'class': 'form-control'}),
            'vinculacion': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),           
            'contrasena': forms.PasswordInput(attrs={'class': 'form-control'}),
            'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
            'municipio': forms.TextInput(attrs={'class': 'form-control'}),
        }
#Cliente
class ClienteForm(forms.ModelForm):
    class Meta:
        model=clientes
        fields = ['nombre', 'solicitante', 'telefono']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'solicitante': forms.TextInput(attrs={'class': 'form-control'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {            
            'nombre': {
                'required': 'El nombre es obligatorias.',
                'max_length': 'El nombre no puden exceder los 100 caracteres.',
            },
            'solicitante': {
                'required': 'El solicitante es obligatorias.',
                'max_length': 'El solicitante no puden exceder los 100 caracteres.',
            },
            'telefono': {
                'required': 'El telefono es obligatorias.',
                'max_length': 'El telefono no puden exceder los 15 caracteres.',
            },
        }
    
    def clean_nombre(self):
        data = self.cleaned_data.get('nombre')
        if len(data) > 100:
            raise forms.ValidationError('El nombre no pueden superar los 100 caracteres.')
        return data    
    
    def clean_solicitante(self):
        data = self.cleaned_data.get('solicitante')
        if len(data) > 100:
            raise forms.ValidationError('El solicitante no pueden superar los 100 caracteres.')
        return data  
    
    def clean_telefono(self):
        data = self.cleaned_data.get('telefono')
        if len(data) > 15:
            raise forms.ValidationError('El telefono no pueden superar los 15 caracteres.')
        return data  
    
#Novedades 
class novedades_thForm(forms.ModelForm):
    class Meta:
        model=novedades_th
        fields = ['tipo_novedad', 'fecha_inicio', 'descripcion', 'tipo_incapacidad']
        widgets = {
            'tipo_novedad': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_inicio': forms.DateInput(attrs={'class': 'datepicker', 'type': 'date'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_incapacidad': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {            
            'tipo_novedad': {
                'required': 'El tipo de novedad es obligatoria.',
                'max_length': 'El tipo de novedad no puden exceder los 100 caracteres.',
            },
            'fecha_inicio': {
                'required': 'El fecha de inicio es obligatoria.',
            },            
            'descripcion': {
                'required': 'La descripcion es obligatoria.',
                'max_length': 'La descripcion no puden exceder los 100 caracteres.',
            },
            'tipo_incapacidad': {
                'required': 'El tipo de incapacidad es obligatoria.',
                'max_length': 'El tipo de incapacidad no puden exceder los 100 caracteres.',
            },
        }
    
    def clean_tipo_novedad(self):
        data = self.cleaned_data.get('tipo_novedad')
        if len(data) > 100:
            raise forms.ValidationError('El tipo de novedad no pueden superar los 100 caracteres.')
        return data    
    
    def clean_fecha_inicio(self):
        fecha_inicio = self.cleaned_data.get('fecha_inicio')
        if fecha_inicio and fecha_inicio < timezone.now().date():
            raise forms.ValidationError("La fecha de programación no puede ser anterior a la fecha actual.")
        return fecha_inicio
    
    def clean_descripcion(self):
        data = self.cleaned_data.get('descripcion')
        if len(data) > 100:
            raise forms.ValidationError('La descripcion no puede superar los 100 caracteres.')
        return data
    
    def clean_tipo_incapacidad(self):
        data = self.cleaned_data.get('tipo_incapacidad')
        if len(data) > 100:
            raise forms.ValidationError('El tipo de incapacidad no pueden superar los 100 caracteres.')
        return data
    
#Empresa aporte
class EmpresaAporteForm(forms.ModelForm):
    class Meta:
        model = empresaAporte
        fields = ['entidad', 'nombre', 'estado']
        widgets = {
            'entidad': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'estado': forms.TextInput(attrs={'class': 'form-control'}),
        }
        error_messages = {            
            'entidad': {
                'required': 'La entidad es obligatorias.',
                'max_length': 'La entidad no puden exceder los 100 caracteres.',
            },
            'nombre': {
                'required': 'El nombre es obligatorias.',
                'max_length': 'El nombre no puden exceder los 100 caracteres.',
            },
            'estado': {
                'required': 'El estado es obligatorias.',
                'max_length': 'El estado no puden exceder los 50 caracteres.',
            },
        }
        
    def clean_entidad(self):
        data = self.cleaned_data.get('entidad')
        if len(data) > 100:
            raise forms.ValidationError('La entidad no pueden superar los 100 caracteres.')
        return data   
    
    def clean_nombre(self):
        data = self.cleaned_data.get('nombre')
        if len(data) > 100:
            raise forms.ValidationError('El nombre no pueden superar los 100 caracteres.')
        return data  
    
    def clean_estado(self):
        data = self.cleaned_data.get('estado')
        if len(data) > 50:
            raise forms.ValidationError('El estado no pueden superar los 50 caracteres.')
        return data