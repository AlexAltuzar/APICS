#from django.shortcuts import render

# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
#from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

#Importar modelo
from Profile.models import Profile, Genero, Ocupacion, Estado, Ciudad, EstadoCivil
#Importar Serializer
from Profile.serializer import ProfileSerializers, GeneroSerializers, OcupacionSerializers, EstadoSerializers, CiudadSerializers, EstadoCivilSerializers

class ProfileList(APIView):
    #Metodo GET para solicitar INFO
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Profile.objects.filter(delete=False)
        #many = True Si aplica si retorno multiples objetos
        serializer = ProfileSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = ProfileSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class GeneroList(APIView):
    #Metodo GET para solicitar INFO
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Genero.objects.filter(delete=False)
        #many = True Si aplica si retorno multiples objetos
        serializer = GeneroSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class OcupacionList(APIView):
    #Metodo GET para solicitar INFO
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Ocupacion.objects.filter(delete=False)
        #many = True Si aplica si retorno multiples objetos
        serializer = OcupacionSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = OcupacionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoList(APIView):
    #Metodo GET para solicitar INFO
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Estado.objects.filter(delete=False)
        #many = True Si aplica si retorno multiples objetos
        serializer = EstadoSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class CiudadList(APIView):
    #Metodo GET para solicitar INFO
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = Ciudad.objects.filter(delete=False)
        #many = True Si aplica si retorno multiples objetos
        serializer = CiudadSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

class EstadoCivilList(APIView):
    #Metodo GET para solicitar INFO
    def get(self, request, format=None):
        print("Metodo get filter")
        queryset = EstadoCivil.objects.filter(delete=False)
        #many = True Si aplica si retorno multiples objetos
        serializer = EstadoCivilSerializers(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = EstadoCivilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)



