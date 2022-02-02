from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from .models import User
from .serializers import UserSerializer

# Create your views here.

@csrf_exempt
def UserView(request, id=0):
    if request.method=='POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            if User.objects.filter(email=user_data['email']).exists():
                return JsonResponse("Email Already Exist", safe=False)
            user_serializer.save()
            return JsonResponse(user_data, safe=False)
        return JsonResponse("Failed to Add", safe=False)
