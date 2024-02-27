from rest_framework import serializers
from .models import Comida, Bebida

class ComidaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comida
        fields='__all__'

class BebidaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bebida
        fields='__all__'
        