from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
import os

# Create your views here.

def cargarInicio(request):
    products = Product.objects.all()
    return render(request, "index.html", {"Prod": products})


def cAddProd(request):
    return render(request, "AddProd.html")