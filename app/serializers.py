from rest_framework import serializers
from .models import *

class campanaSerializers(serializers.ModelSerializer):
    class Meta:
        model=campana
        fields =('nombre', 'organizacion','fecha','ubicacion','celular','ciudad','correo')