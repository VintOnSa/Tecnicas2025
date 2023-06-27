from django.urls import path
from . import views


urlpatterns = [
    path('products', views.ObtainProduct.as_view()),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('get-cart/', views.get_cart, name='get_cart'),
]