from django.urls import path, re_path
from app import views

urlpatterns = [

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
    path('registroUsuario', views.registroUsuario, name='registroUsuario'),
    
    #no se 
    # path('login', views.login, name='login')

    #eliminar


]
