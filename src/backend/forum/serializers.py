from rest_framework import serializers
from django.contrib.auth.models import User
from forum.models import *
from authentication.serializers import *

class ThreadListSerializer(serializers.HyperlinkedModelSerializer):
    owner = UserDetailsSerializer(source='owner_id', read_only=True)
    class Meta:
        model = Thread
        fields = ['url', 'id', 'title', 'body', 'view_count', 'comment_count', 'created_at', 'updated_at', 'owner']

class ThreadDetailSerializer(serializers.HyperlinkedModelSerializer):
    class CommentDetailSer(serializers.HyperlinkedModelSerializer):
        user = UserDetailsSerializer(source='user_id')
        class Meta:
            model = Comment
            fields = ['url', 'id', 'user', 'reply_to', 'content', 'created_at', 'updated_at']
    
    owner = UserDetailsSerializer(source='owner_id', read_only=True)
    comments = CommentDetailSer(many=True, read_only=True, source='comment_set')
    view_count = serializers.ReadOnlyField()
    comment_count = serializers.ReadOnlyField()
    class Meta:
        model = Thread
        fields = ['url', 'id', 'title', 'body', 'view_count', 'comment_count', 'created_at', 'updated_at', 'owner', 'comments']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = [field.name for field in model._meta.fields]
        fields += ['url']