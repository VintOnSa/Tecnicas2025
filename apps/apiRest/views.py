from django.shortcuts import render
from django.views import View
from apps.Store.models import Product
from django.http import JsonResponse
# Create your views here.


class ObtainProduct(View):
    def get(self,request):
        products = Product.objects.all()
        return JsonResponse(list(products.values()),safe=False)
    


def add_to_cart(request, product_id):
    
    return JsonResponse({"message": "Producto agregado al carrito correctamente."})

def get_cart(request):
    
    return JsonResponse({"cart": "Datos del carrito de compras"})