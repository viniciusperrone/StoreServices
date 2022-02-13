from rest_framework.views import APIView
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
import jwt, datetime

from .models import User
from .serializers import UserSerializer

# Create your views here.

class UserView(APIView):
    @csrf_exempt
    def create(request):
        if request.method=='POST':
            user_data = JSONParser().parse(request)
            user_serializer = UserSerializer(data=user_data)
            if user_serializer.is_valid():
                if User.objects.filter(email=user_data['email']).exists():
                    return JsonResponse('Email Already Exist', safe=False)
                user_serializer.save()
                return JsonResponse(user_data, safe=False)
            return JsonResponse('Failed to Add', safe=False)
    @csrf_exempt
    def login(request):
        if request.method=='POST':
            user = JSONParser().parse(request)
            email = user['email']
            password = user['password']

            user = User.objects.filter(email=email, password=password).first()
            user_serializer = UserSerializer(user)

            if user is None:
                return JsonResponse('Dados incorretos!', safe=False)

            payload = {
                'id': str(user.id),
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }


            token = jwt.encode(payload, 'secret', algorithm='HS256')

            print(token)

            response = {
                'token': token,
                'user': user_serializer.data
            }

            return JsonResponse(response, safe=False)
    