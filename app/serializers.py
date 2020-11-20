from rest_framework import serializers
from .models import *

class campanaSerializers(serializers.ModelSerializer):
    class Meta:
        model=campana
        fields =('nombre', 'organizacion','fecha','ubicacion','celular','ciudad','correo')


class hospitalSerializers(serializers.ModelSerializer):
    class Meta:
        model=hospital
        fields =('nombre', 'ciudad','celular','ubicacion','correo')


class incentivoSerializers(serializers.ModelSerializer):
    class Meta:
        model=incentivo
        fields =('nombre', 'empresa','fecha','tipo','celular','correo')

