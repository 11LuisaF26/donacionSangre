from django.contrib import admin
from django.urls import path, re_path, include
from app import views
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('campana', campanaViewSet)
router.register('hospital', hospitalViewSet)
router.register('incentivo', incentivoViewSet)
router.register('datos', datos_usuarioViewSet)

urlpatterns = [

    path('api/',include(router.urls)),

    #index
    path('', views.index, name='home'),

    # vistas sin consulta
    path('about', views.about, name='about'),
    path('menu', views.menu, name='menu'),
    path('requisito', views.requisito, name='requisito'),
    path('rh', views.rh, name='rh'),

    #consulta
    path('campana', views.campanas, name='campana'),
    path('hospital', views.hospitales, name='hospital'),
    path('incentivo', views.incentivos, name='incentivo'), 
    
   

    # registro
    path('registroCampana', views.registroCampana, name='registroCampana'),
    path('registroHospital', views.registroHospital, name='registroHospital'),
    path('registroIncentivo', views.registroIncentivo, name='registroIncentivo'),
    path('datos', views.registroDatos, name='datos'),   
    
    #no se 
    # path('login', views.login, name='login')

    #eliminar


]
