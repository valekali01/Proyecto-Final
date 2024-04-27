
from django.urls import path

from django.http import HttpResponse

from.views import mi_home

urlpatterns = [
    path("", mi_home)
]
