from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def mi_home(xx):
    return HttpResponse ("<h1>Bienvenidos a la aplicaccion de reservas</h1>")
