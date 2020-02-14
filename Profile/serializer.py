from rest_framework import routers, serializers, viewsets

from Profile.models import Profile, Genero, Ocupacion, Estado, Ciudad, EstadoCivil

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('__all__')

class GeneroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ['genero']

class OcupacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ocupacion
        fields = ['ocupacion']

class EstadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ['estado']

class CiudadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('__all__')

class EstadoCivilSerializers(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = ['estado_civil']

