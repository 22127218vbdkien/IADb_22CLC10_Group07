from authentication.serializers import *
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly, DjangoModelPermissionsOrAnonReadOnly, IsAdminUser, IsAuthenticated
from django.contrib.auth.models import User
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import action
from authentication.permissions import IsOwnerPermission
from rest_framework import serializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        permission_classes = []
        if self.action in ['list', 'create']:
            permission_classes = [IsAdminUser]
        elif self.action in ['retrieve', 'update', 'destroy']:
            permission_classes = [IsAdminUser, IsOwnerPermission]
        elif self.action in ['signup', 'login', 'changePassword']:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    
    
    @action(detail=False, methods=['post'], url_path='signup')
    def signup(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=request.data['username'])
            user.set_password(request.data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        user = get_object_or_404(User, username=request.data['username'])
        if not user.check_password(request.data['password']):
            return Response("missing user", status=status.HTTP_404_NOT_FOUND)
        token, created = Token.objects.get_or_create(user=user)
        serializer = UserSerializer(user)
        return Response({'token': token.key, 'user': serializer.data})

    @action(detail=False, methods=['post'], url_path='changePassword')
    def changePassword(self, request):
        class PasswordSerializer(serializers.Serializer):
            old_password = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'})
            new_password = serializers.CharField(required=True, write_only=True, style={'input_type': 'password'})
            class Meta:
                model = User
        
        if not request.user.is_authenticated:
            return Response({'detail': 'Authentication credentials are not provided.'}, status=status.HTTP_401_UNAUTHORIZED)
        if request.user.username != request.data['username']:
            return Response({'detail': 'Invalid password changing request'}, status=status.HTTP_401_UNAUTHORIZED)
        
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = get_object_or_404(User, username=request.data['username'])
            if not user.check_password(serializer.validated_data['old_password']):
                return Response({'old_password': 'Wrong password.'}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(serializer.validated_data['new_password'])
            user.save()
            return Response({'status':'password changed successfully.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

        
