from django.shortcuts import render
from authentication.serializers import *
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class UserRegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

class UserLoginView(APIView):
    def post(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response("missing user", status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data})
    

# The following is the custom permission for authenticated user and admin user, will be used later
class AuthenticatedUserView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        pass
        # Your authenticated user action

class AdminView(APIView):
    permission_classes = [IsAdminUser]

    def post(self, request):
        pass
        # Your admin-specific action
        
        
