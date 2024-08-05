from rest_framework import serializers
from django.contrib.auth.models import User
from forum.models import *

class ThreadListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Thread
        fields = ['']