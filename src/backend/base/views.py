from django.contrib.auth.models import User
from rest_framework import permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from base.models import *
from base.serializers import *

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeViewSerializer

class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioViewSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StaffViewSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer