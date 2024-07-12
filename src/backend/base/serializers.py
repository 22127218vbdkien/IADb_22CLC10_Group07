from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import *

# # Anime Serializer
# class AnimeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Anime
#         fields = '__all__'

# #Anime synonym serializers 
# class AnimeSynonymSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AnimeSynonym
#         fields = '__all__'

# #Studio serializers
# class StudioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Studio
#         fields = '__all__'

# #Character serializers
# class CharacterSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Character
#         fields = '__all__'
        
# #Staff serializers
# class StaffSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Staff
#         fields = '__all__'

# #Staff in anime serializers
# class StaffInAnimeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StaffInAnime
#         fields = '__all__'

# #Anime produced by Studio serializers
# class AnimeProducedByStudioSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AnimeProducedByStudio
#         fields = '__all__'

# #Anime relation serializers 
# class AnimeRelationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AnimeRelation
#         fields = '__all__'

# # Anime tag serializers  
# class AnimeTagSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AnimeTag
#         fields = '__all__'

# #External site serializers 
# class ExternalSiteSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ExternalSite
#         fields = '__all__'

# #Anime External link serializers 
# class AnimeExternalLinkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = AnimeExternalLink
#         fields = '__all__'

# #Staff External link serializers
# class StaffExternalLinkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StaffExternalLink
#         fields = '__all__'
    

# ACTUAL VIEW SERIALIZERS
#Anime view serializers
class AnimeViewSerializer(serializers.HyperlinkedModelSerializer):
    class AnimeTagSerializer(serializers.ModelSerializer):
        class TagSerializer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Tag
                fields = ['name', 'description', 'is_general_spoiler']
        tag = TagSerializer(source='tag_id')
        class Meta:
            model = AnimeTag
            fields = ['tag', 'rank', 'is_spoiler']

    tags = AnimeTagSerializer(many=True, source='animetag_set', read_only=True)
    class Meta:
        model = Anime
        fields = '__all__'

class AnimeListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = ['url', 'id', 'id_anilist', 'romaji_title', 'format', 'status', 'start_date', 'end_date', 'episodes', 'cover_img_large', 'cover_img_med', 'weighted_score', 'anilist_score', 'mean_score', 'popularity', 'trending', 'favorites']
    

class StudioViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Studio
        fields = ['url']

class StaffViewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = ['url', 'id', 'name', 'name_native']