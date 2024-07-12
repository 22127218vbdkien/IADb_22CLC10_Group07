from rest_framework import permissions, renderers, viewsets
from rest_framework.pagination import PageNumberPagination

from base.models import *
from base.serializers import *

class AnimeViewSet(viewsets.ModelViewSet):
    queryset = Anime.objects.all()
    serializer_class = AnimeViewSerializer
    
    def get_serializer_class(self):
        if self.action == 'list':
            return AnimeListSerializer
        return AnimeViewSerializer

class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioViewSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffViewSerializer

# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer

# class AnimeTagViewSet(viewsets.ModelViewSet):
#     queryset = AnimeTag.objects.all()
#     serializer_class = AnimeTagSerializer