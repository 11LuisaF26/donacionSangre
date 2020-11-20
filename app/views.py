from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect 
from django import template
from django.contrib import messages
from django.contrib.auth.models import Group, User
from django.template import RequestContext
from django.views.generic import CreateView, ListView
from django.urls import reverse
from django.core.exceptions import PermissionDenied
from .models import *
from .forms import *
from .serializers import *
from rest_framework import viewsets

# Create your views here.

# Index
def index(request):
    return render(request, "index.html")

# sin consulta 
def about(request):
    return render(request,"about.html")
def menu(request):
    return render(request,"menu.html")
def requisito(request):
    return render(request,"requisito.html")
def rh(request):
    return render(request,"rh.html")

# Consultas
def campanas(request):
    campanas_to_list = campana.objects.all()
    return render(request,"campana.html", {"campanas": campanas_to_list})
    

def hospitales(request):
    hospitales_to_list = hospital.objects.all()
    return render(request,"hospital.html",{"hospitales": hospitales_to_list})

def incentivos(request):
    incentivos_to_list = incentivo.objects.all()
    return render(request,"incentivo.html",{"incentivos": incentivos_to_list})


#Registro
def registroCampana(request):
    form = campana_form()
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = campana_form(request.POST) # Bound form
        if form.is_valid():
            new_campana = form.save() # Guardar los datos en la base de datos                              
            
        else:
            form = campana_form()
    return render(request,"registroCampana.html", {'form':form})

def registroHospital(request):
    form = hospital_form()
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = hospital_form(request.POST) # Bound form
        if form.is_valid():
            new_hospital = form.save() # Guardar los datos en la base de datos                              
            
        else:
            form = hospital_form()
    return render(request,"registroHospital.html", {"form": form})

def registroIncentivo(request):
    form = incentivo_form()
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = incentivo_form(request.POST) # Bound form
        if form.is_valid():
            new_incentivo = form.save() # Guardar los datos en la base de datos                              
            
        else:
            form = incentivo_form()
    return render(request,"registroIncentivo.html",{"form": form})

def registroUsuario(request):
    form = usuario_form()
    if request.method == 'POST': # si el usuario está enviando el formulario con datos
        form = usuario_form(request.POST) # Bound form
        if form.is_valid():
            new_usuario = form.save() # Guardar los datos en la base de datos                              
            
        else:
            form = usuario_form()
    return render(request,"registroUsuario.html",{"form": form})

# NO SE :v
def login(request):
    return render(request,"login.html")

 # API's

class campanaViewSet(viewsets.ModelViewSet):
     queryset = campana.objects.all()
     serializer_class = campanaSerializers

class hospitalViewSet(viewsets.ModelViewSet):
     queryset = hospital.objects.all()
     serializer_class = hospitalSerializers

class incentivoViewSet(viewsets.ModelViewSet):
     queryset = incentivo.objects.all()
     serializer_class = incentivoSerializers
 