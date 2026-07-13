from django.urls import path
from . import views

urlpatterns = [
    path("", views.liste_clients, name="liste_clients"),
    path("ajouter/", views.ajouter_client, name="ajouter_client"),
]