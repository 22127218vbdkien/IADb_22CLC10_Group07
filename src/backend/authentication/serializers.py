from rest_framework import serializers
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.contrib.auth import get_user_model
from authentication.models import *

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

class PasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'})
    new_password = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'})
    class Meta:
        model = User

class UserLoginSerializer(serializers.ModelSerializer):
            password = serializers.CharField(min_length=5,validators=[MinLengthValidator(5)],max_length=30,write_only=True,required=True)
            username = serializers.CharField(min_length=5,validators=[MinLengthValidator(5)],max_length=30,required=True)
            class Meta:
                model = User
                fields = ['password', 'username']

class UserDetailsSerializer(serializers.HyperlinkedModelSerializer):
    class UserProfileSer(serializers.ModelSerializer):
        class Meta:
            model = UserProfile
            fields = ['url', 'about', 'avatar']
    
    profile = UserProfileSer(read_only=True)
    class Meta:
        model = User
        fields = ['url', 'username', 'profile']

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.user_id')
    class Meta:
        model = UserProfile
        fields = '__all__'