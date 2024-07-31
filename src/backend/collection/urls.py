from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from collection import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'temp', views.TempViewSet, basename='temp')