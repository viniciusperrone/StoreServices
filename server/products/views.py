from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse


from .models import Products
from .serializers import ProductsSerializer

from user.models import User

# Create your views here.

# READ ALL

class ProductsView(APIView):
    @csrf_exempt
    def get(request):
        if request.method=='GET':
            products = Products.objects.all()
            products_serializer = ProductsSerializer(products, many=True)
            return JsonResponse(products_serializer.data, safe=False)
    @csrf_exempt
    def show(request, id):
        product = Products.objects.get(id=id)
        if product is None:
            JsonResponse('Produto encontrado!', safe=False)
    @csrf_exempt
    def create(request, id):
        user = User.objects.get(id=id)
        product = JSONParser().parse(request)
        product_serializer = ProductsSerializer(data=product)
        print(product_serializer)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse(product_serializer.data, safe=False)
        return JsonResponse('Error na criação!', safe=False)
    @csrf_exempt
    def update(request, id):
        if request.method=='PUT':
            product = Products.objects.get(id=id)
            product_data = JSONParser().parse(request)
            product_serializer = ProductsSerializer(product, data=product_data)
            if product_serializer.is_valid():
                product_serializer.save()
                return JsonResponse(product_serializer.data, safe=False)
            return JsonResponse("Failed to Update!!", safe=False)
    @csrf_exempt
    def delete(request, id):
        if request.method=='DELETE':
            product = Products.objects.get(id=id)
            product.delete()
            return JsonResponse("Deleted Succefully", safe=False)
