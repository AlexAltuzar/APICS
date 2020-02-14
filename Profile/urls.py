from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User
# from rest_framework import routers, serilizers, viewsets

from Profile import views

urlpatterns = [
    re_path(r'Profile_list/$', views.ProfileList.as_view()),
    #re_path(r'Profile_list/nombre', views.ProfileList.as_view()),
    #re_path(r'Profile_list/apellidoPaterno', views.ProfileList.as_view()),
    #re_path(r'Profile_list/apellidoMaterno', views.ProfileList.as_view()),
    #re_path(r'Profile_list/edad', views.ProfileList.as_view()),
    re_path(r'Profile_list/genero/$', views.GeneroList.as_view()),
    re_path(r'Profile_list/ocupacion/$', views.OcupacionList.as_view()),
    re_path(r'Profile_list/estado/$', views.EstadoList.as_view()),
    re_path(r'Profile_list/ciudad/$', views.CiudadList.as_view()),
    re_path(r'Profile_list/estadoCivil/$', views.EstadoCivilList.as_view())
    #Hola soy Alex
]