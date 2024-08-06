from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from forum import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'threads', views.ThreadViewSet, basename='thread')
router.register(r'comments', views.CommentViewSet, basename='comment')