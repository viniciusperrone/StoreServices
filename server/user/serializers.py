from rest_framework import serializers
from .models import User
from  django.core.exceptions import ValidationError

class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField()    
    class Meta: 
        model = User
        fields = '__all__'