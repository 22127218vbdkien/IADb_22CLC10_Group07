from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import *
from collection.models import *

class TempSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FavoriteCharacter
        fields = '__all__'