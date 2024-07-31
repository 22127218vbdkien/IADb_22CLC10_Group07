from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from base import views

# Create a router and register our viewsets with it.
router = DefaultRouter()

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    re_path(r'^collection/', include(router.urls))
]