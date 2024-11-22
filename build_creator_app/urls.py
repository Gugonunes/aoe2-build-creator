from django.urls import path

from . import views

urlpatterns = [
    path("", views.resource_calculator, name="index"),
]
