from django.urls import path
from . import views

urlpatters = [
    path('', views.super_types_list)
]