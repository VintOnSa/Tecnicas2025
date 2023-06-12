from django.shortcuts import render

# Create your views here.

def cargarInicio(request):
    return render(request, "index.html")