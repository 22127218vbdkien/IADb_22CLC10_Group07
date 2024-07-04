from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import *

#Anime synonym serializers 
class AnimeSynonymSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimeSynonym
        fields = '__all__'

#Studio serializers
class StudioSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'

#Character serializers
class CharacterSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
        
#Staff serializers
class StaffSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

#Staff in anime serializers
class StaffInAnimeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaffInAnime
        fields = '__all__'

#Anime produced by Studio serializers
class AnimeProducedByStudioSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimeProducedByStudio
        fields = '__all__'

#Anime relation serializers 
class AnimeRelationSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimeRelation
        fields = '__all__'

#Tag serializers 
class TagSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

#Anime tag serializers  
class AnimeTagSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimeTag
        fields = '__all__'

#External site serializers 
class ExternalSiteSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExternalSite
        fields = '__all__'

#Anime External link serializers 
class AnimeExternalLinkSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimeExternalLink
        fields = '__all__'

#Staff External link serializers
class StaffExternalLinkSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaffExternalLink
        fields = '__all__'

#Anime serializers
class AnimeSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'