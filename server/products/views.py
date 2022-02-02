from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import Products
from .serializers import ProductsSerializer

# Create your views here.

# READ ALL
@csrf_exempt
def get(request):
    if request.method=='GET':
        products = Products.objects.all()
        products_serializer = ProductsSerializer( products, many=True)
        return JsonResponse(products_serializer.data , safe=False)

# Registro
@csrf_exempt
def post(request):
    if request.method=='POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductsSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_data, safe=False)
        return JsonResponse("Failed to Add", safe=False)