from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import *

# Anime Serializer
class AnimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'

#Anime synonym serializers 
class AnimeSynonymSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimeSynonym
        fields = '__all__'

#Studio serializers
class StudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'

#Character serializers
class CharacterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
        
#Staff serializers
class StaffSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

#Staff in anime serializers
class StaffInAnimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaffInAnime
        fields = '__all__'

#Anime produced by Studio serializers
class AnimeProducedByStudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimeProducedByStudio
        fields = '__all__'

#Anime relation serializers 
class AnimeRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimeRelation
        fields = '__all__'

#Tag serializers 
class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

#Anime tag serializers  
class AnimeTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimeTag
        fields = '__all__'

#External site serializers 
class ExternalSiteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ExternalSite
        fields = '__all__'

#Anime External link serializers 
class AnimeExternalLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimeExternalLink
        fields = '__all__'

#Staff External link serializers
class StaffExternalLinkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaffExternalLink
        fields = '__all__'
    

# ACTUAL VIEW SERIALIZERS
#Anime view serializers
class AnimeViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'

    studios = StudioSerializer(many=True)
    staffs = StaffSerializer(many=True)
    tags = TagSerializer(many=True)
    relations = AnimeSerializer(many=True)
    animeexternallinks = serializers.SlugRelatedField(many=True, read_only=True, slug_field='url')

class StudioViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'

    animes = AnimeSerializer(many=True)

class StaffViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

    animes = AnimeSerializer(many=True)