from django.urls import path
from . import views

urlpatterns = [
    path('', views.cargarInicio),
    path('AddProduct', views.cAddProd),
    path('cart', views.salesCart)
]
