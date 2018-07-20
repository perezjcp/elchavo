from django.urls import path
from django.contrib.auth.views import LoginView

from . import views

urlpatterns = [
    path("", views.index, name = "index"),
    path("logout", views.log_out, name="log_out"),
    path("login", LoginView.as_view(), name='login'),
    path("getsales", views.msales, name = "msales"),
    path("getinfo", views.getinfo, name = "getinfo"),
    path("update", views.update, name = "update"),
    path("inputsales", views.inputsales, name = "input")

  
]