from django.shortcuts import render
from django.views import View
from apps.Store.models import Product
from django.http import JsonResponse
# Create your views here.


class ObtainProduct(View):
    def get(self,request):
        products = Product.objects.all()
        return JsonResponse(list(products.values()),safe=False)