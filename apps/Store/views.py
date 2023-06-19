from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
import os
from django.http import HttpResponse
import json

# Create your views here.

def cargarInicio(request):
    products = Product.objects.all()
    return render(request, "index.html", {"Prod": products})


def cAddProd(request):
    return render(request, "AddProd.html")



def salesCart(request):
    #print("texto",request.body)

    data = json.loads(request.body)

    for i in data:
        print("Sku:",i['sku'])
        print("Name:",i['name'])
        print("Amount:",i['amount'])

    return HttpResponse("Texto")