from rest_framework import permissions, renderers, viewsets
from base.models import *
from base.serializers import *
from collection.models import *
from collection.serializers import *
import django_filters
from rest_framework import filters

# Create your views here.
class TempViewSet(viewsets.ModelViewSet):
    queryset = FavoriteCharacter.objects.all()
    serializer_class = TempSerializer