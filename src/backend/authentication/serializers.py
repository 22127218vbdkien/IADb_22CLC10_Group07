from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(min_length=5,validators=[MinLengthValidator(5)],max_length=30,write_only=True,required=True)
    username = serializers.CharField(min_length=5,validators=[MinLengthValidator(5)],max_length=30,required=True)
    email = serializers.EmailField(required=True)
    
    def validate_email(self, value):
        if get_user_model().objects.filter(email=value).exists():
            raise serializers.ValidationError("Email already exists")
        return value

    def validate_username(self, value): 
        if get_user_model().objects.filter(username=value).exists():
            raise serializers.ValidationError("Username already exists") 
        return value
    
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']
