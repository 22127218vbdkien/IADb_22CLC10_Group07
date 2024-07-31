"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, re_path, path
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework import routers

from base.urls import router as base_router
from collection.urls import router as collection_router

API_TITLE = 'IADb API'
API_DESCRIPTION = 'A Web API for an online anime database.'
schema_view = get_schema_view(title=API_TITLE)

class DefaultRouter(routers.DefaultRouter):
    def extend(self, router):
        self.registry.extend(router.registry)

router = DefaultRouter()
router.extend(base_router)
router.extend(collection_router)

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^', include('authentication.urls')),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    re_path(r'^', include(router.urls)),
]