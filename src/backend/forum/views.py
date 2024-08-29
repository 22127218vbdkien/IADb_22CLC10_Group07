from rest_framework import permissions, renderers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly

import django_filters
from rest_framework import filters

from forum.models import *
from forum.serializers import *
from forum.permissions import *

class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerPermission]
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user)
    
    def get_queryset(self):
        user = self.request.user
        return Comment.objects.all().order_by('id')

class ThreadViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerPermission]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    search_fields = ['title', 'body']
    ordering_fields = ['updated_at', 'view_count', 'comment_count']

    def get_serializer_class(self):
        if self.action == 'list':
            return ThreadListSerializer
        return ThreadDetailSerializer

    def get_queryset(self):
        if self.action == 'list':
            return Thread.objects.all().order_by('updated_at').prefetch_related('owner_id')
        if self.action in ['retrieve', 'update', 'partial_update', 'destroy']:
            return Thread.objects.all().prefetch_related('comment_set')

    def perform_create(self, serializer):
        serializer.save(owner_id=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        obj = self.get_object()
        obj.view_count += 1
        obj.save(update_fields=("view_count",))
        return super().retrieve(request, *args, **kwargs)