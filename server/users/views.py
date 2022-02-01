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
            user_serializer.save()
            return JsonResponse(
                "Successfully added user", 
                user_serializer.data,
                safe=False
            )
        return JsonResponse("Failed register")


