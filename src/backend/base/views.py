from rest_framework import permissions, renderers, viewsets
from base.models import *
from base.serializers import *
import django_filters
from rest_framework import filters


class AnimeViewSet(viewsets.ModelViewSet):
    class AnimeFilter(django_filters.FilterSet):
        anime_format = django_filters.ChoiceFilter(
            field_name= 'format',
            choices = Anime.FormatType
        )
        tags = django_filters.ModelMultipleChoiceFilter(
            field_name = 'tags',
            to_field_name = 'id',
            conjoined = True,
            queryset = Tag.objects.filter()
        )
        year = django_filters
        class Meta:
            model = Anime
            fields = ['tags', 'anime_format', 'status', 'source', 'studios']

    queryset = Anime.objects.all()
    serializer_class = AnimeViewSerializer

    # For filtering
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend, 
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    search_fields = ['romaji_title', 'english_title', 'native_title', 'hashtag']
    ordering_fields = ['start_date', 'popularity', 'trending', 'favorites', 'anilist_score']
    filterset_class = AnimeFilter
    
    def get_serializer_class(self):
        if self.action == 'list':
            return AnimeListSerializer
        return AnimeViewSerializer

class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all()
    serializer_class = StudioViewSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return StudioListSerializer
        return StudioViewSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffViewSerializer

    def get_serializer_class(self):
        if self.action == 'list':
            return StaffListSerializer
        return StaffViewSerializer

# class TagViewSet(viewsets.ModelViewSet):
#     queryset = Tag.objects.all()
#     serializer_class = TagSerializer

# class AnimeTagViewSet(viewsets.ModelViewSet):
#     queryset = AnimeTag.objects.all()
#     serializer_class = AnimeTagSerializer