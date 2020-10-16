from django.forms import ModelForm
from django.db import models
from django import forms
from .models import *   


class campana_form(ModelForm): 
    class Meta():
        model = campana
        fields =('nombre', 'organizacion','fecha','ubicacion','celular','ciudad','correo')

class hospital_form(ModelForm): 
    class Meta():
        model = hospital
        fields =('nombre', 'ciudad','celular','ubicacion','correo')


class incentivo_form(ModelForm): 
    class Meta():
        model = incentivo
        fields =('nombre', 'empresa','fecha','tipo','celular','correo')


class usuario_form(ModelForm): 
    class Meta():
        model = usuario
        fields =('nombre', 'apellido','documento','numDocumento','grupo','rh','fecha','genero','ciudad','celular','correo','contrasena','confirmar')
