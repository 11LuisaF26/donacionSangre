from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('usuario', UserViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout")
]
