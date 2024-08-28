from rest_framework import permissions, renderers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from base.models import *
from base.serializers import *
from collection.models import *
from collection.serializers import *

import django_filters
from rest_framework import filters

from collection.permissions import *

class FavoriteCharacterViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated or IsOwnerPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return FavoriteCharacterListSerializer
        return FavoriteCharacterSerializer

    def get_queryset(self):
        user = self.request.user
        return FavoriteCharacter.objects.filter(user_id=user).order_by('id').prefetch_related('char_id')
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class FavoriteStudioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated or IsOwnerPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return FavoriteStudioListSerializer
        return FavoriteStudioSerializer

    def get_queryset(self):
        user = self.request.user
        return FavoriteStudio.objects.filter(user_id=user).order_by('id').prefetch_related('studio_id')
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)


class FavoriteStaffViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated or IsOwnerPermission]

    def get_serializer_class(self):
        if self.action == 'list':
            return FavoriteStaffListSerializer
        return FavoriteStaffSerializer

    def get_queryset(self):
        user = self.request.user
        return FavoriteStaff.objects.filter(user_id=user).order_by('id').prefetch_related('staff_id')
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)

class AnimeInCollectionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated or IsOwnerPermission]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=anime_id__id']

    @action(detail=False)
    def Favorite(self, request):
        user = self.request.user
        anime_list = AnimeInCollection.objects.filter(
            user_id=user, is_favorite=True
        ).prefetch_related('anime_id')

        page = self.paginate_queryset(anime_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(anime_list, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def Watching(self, request):
        user = self.request.user
        anime_list = AnimeInCollection.objects.filter(
            user_id=user, in_list='WATCHING'
        ).prefetch_related('anime_id')

        page = self.paginate_queryset(anime_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(anime_list, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def Completed(self, request):
        user = self.request.user
        anime_list = AnimeInCollection.objects.filter(
            user_id=user, in_list='COMPLETED'
        ).prefetch_related('anime_id')

        page = self.paginate_queryset(anime_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(anime_list, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def Paused(self, request):
        user = self.request.user
        anime_list = AnimeInCollection.objects.filter(
            user_id=user, in_list='PAUSED'
        ).prefetch_related('anime_id')

        page = self.paginate_queryset(anime_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(anime_list, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def Dropped(self, request):
        user = self.request.user
        anime_list = AnimeInCollection.objects.filter(
            user_id=user, in_list='DROPPED'
        ).prefetch_related('anime_id')

        page = self.paginate_queryset(anime_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(anime_list, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def Planning(self, request):
        user = self.request.user
        anime_list = AnimeInCollection.objects.filter(
            user_id=user, in_list='PLANNING'
        ).prefetch_related('anime_id')

        page = self.paginate_queryset(anime_list)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(anime_list, many=True)
        return Response(serializer.data)

    def get_serializer_class(self):
        if self.action in ['list', 'Watching', 'Completed', 'Paused', 'Dropped', 'Planning']:
            return AnimeInCollectionListSerializer
        return AnimeInCollectionSerializer

    def get_queryset(self):
        user = self.request.user
        return AnimeInCollection.objects.filter(user_id=user).order_by('id').prefetch_related('anime_id')
    
    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)