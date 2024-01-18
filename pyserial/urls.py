"""pyserial urls definitions"""
from django.urls import path

from . import views

app_name = "pyserial"

urlpatterns = [
    path("", views.index, name="index"),
]
