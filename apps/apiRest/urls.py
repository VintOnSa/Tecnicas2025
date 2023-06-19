from django.urls import path
from . import views


urlpatterns = [
    path('products', views.ObtainProduct.as_view())
]