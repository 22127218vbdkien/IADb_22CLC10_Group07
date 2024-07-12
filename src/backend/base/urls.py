from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from base import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'animes', views.AnimeViewSet, basename='anime')
router.register(r'studios', views.StudioViewSet, basename='studio')
router.register(r'staffs', views.StaffViewSet, basename='staff')
# router.register(r'tags', views.TagViewSet, basename='tag')
# router.register(r'animetags', views.AnimeTagViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    re_path(r'^', include(router.urls))
]