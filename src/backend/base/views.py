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

    queryset = Anime.objects.all().order_by('id')
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
    
    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.trending += 1
        obj.save(update_fields=("trending",))
        return super().retrieve(request, *args, **kwargs)

class StudioViewSet(viewsets.ModelViewSet):
    queryset = Studio.objects.all().order_by('id')
    serializer_class = StudioViewSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    search_fields = ['name']
    ordering_fields = ['name', 'favorites']

    def get_serializer_class(self):
        if self.action == 'list':
            return StudioListSerializer
        return StudioViewSerializer

class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all().order_by('id')
    serializer_class = StaffViewSerializer

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    search_fields = ['name', 'name_native']
    ordering_fields = ['name', 'favorites']

    def get_serializer_class(self):
        if self.action == 'list':
            return StaffListSerializer
        return StaffViewSerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = Character.objects.all().order_by('id')
    serializer_class = CharacterViewSerializer
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    search_fields = ['name', 'name_native']
    ordering_fields = ['name', 'favorites']

    def get_serializer_class(self):
        if self.action == 'list':
            return CharacterListSerializer
        return CharacterViewSerializer
    
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().order_by('id')
    serializer_class = TagListSerializer

class AnimeProducedByStudioViewSet(viewsets.ModelViewSet):
    queryset = AnimeProducedByStudio.objects.all().order_by('id')
    serializer_class = AnimeProducedByStudioSerializer

class StaffInAnimeViewSet(viewsets.ModelViewSet):
    queryset = StaffInAnime.objects.all().order_by('id')
    serializer_class = StaffInAnimeSerializer

class AnimeTagViewSet(viewsets.ModelViewSet):
    queryset = AnimeTag.objects.all().order_by('id')
    serializer_class = AnimeTagSerializer

class AnimeRelationViewSet(viewsets.ModelViewSet):
    queryset = AnimeRelation.objects.all().order_by('id')
    serializer_class = AnimeRelationSerializer

class CharacterInAnimeViewSet(viewsets.ModelViewSet):
    queryset = CharacterInAnime.objects.all().order_by('id')
    serializer_class = CharacterInAnimeSerializer