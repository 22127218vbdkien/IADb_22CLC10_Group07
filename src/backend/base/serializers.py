from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import *

#Anime serializers
class AnimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Anime
        fields = '__all__'

#Anime synonym serializers 
class AnimeSynonymSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnimeSynonym
        fields = '__all__'

#Studio serializers
class StudioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Studio
        fields = '__all__'

#Character serializers
class CharacterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
        
#Staff serializers
class StaffSerializers(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'

#Staff in anime serializers
class StaffInAnimeSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffInAnime
        fields = '__all__'

#Staff voice character serializers 
class StaffVoiceCharacterSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffVoiceCharacter
        fields = '__all__'

#Anime produced by Studio serializers
class AnimeProducedByStudioSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnimeProducedByStudio
        fields = '__all__'

#Anime relation serializers 
class AnimeRelationSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnimeRelation
        fields = '__all__'

#Tag serializers 
class TagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

#Anime tag serializers  
class AnimeTagSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnimeTag
        fields = '__all__'

#External site serializers 
class ExternalSiteSerializers(serializers.ModelSerializer):
    class Meta:
        model = ExternalSite
        fields = '__all__'

#Anime External link serializers 
class AnimeExternalLinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = AnimeExternalLink
        fields = '__all__'

#Staff External link serializers
class StaffExternalLinkSerializers(serializers.ModelSerializer):
    class Meta:
        model = StaffExternalLink
        fields = '__all__'