from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm
from rest_framework import viewsets
from .serializers import *

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("http://localhost:3000/menu")
            else:    
                msg = 'Credenciales Invalidas'    
        else:
            msg = 'Error validando el formulario'  

    return render(request, "login.html", {"form": form, "msg" : msg})

def register_user(request):
    msg     = None
    success = False

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")                                  
            user = authenticate(username=username, password=raw_password)
            

            msg     = 'Usuario creado - por favor <a href="/login">ingresa</a>.'
            success = True
            
            return redirect("/login/")

        else:
            msg = 'El formulario no es valido'    
    else:
        form = SignUpForm()
        
    return render(request, "registroUsuario.html", {"form": form, "msg" : msg, "success" : success })

# API's
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = usuariosSerializers