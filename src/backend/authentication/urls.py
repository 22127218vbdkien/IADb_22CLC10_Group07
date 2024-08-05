from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from authentication import views

router = DefaultRouter()
router.register(r'user', views.UserViewSet, basename='user')
router.register(r'userprofiles', views.UserProfileViewSet, basename='userprofile')