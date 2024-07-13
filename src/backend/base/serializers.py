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
    class AnimeTagSer(serializers.HyperlinkedModelSerializer):
        class TagSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Tag
                fields = ['name', 'description', 'is_general_spoiler']
        tag = TagSer(source='tag_id')
        class Meta:
            model = AnimeTag
            fields = ['tag', 'rank', 'is_spoiler']
        
        def to_representation(self, instance):
            data = super().to_representation(instance)
            tag_data = data.pop('tag')
            for key in tag_data:
                data[key] = tag_data[key]
            return data

    class AnimeRelationSer(serializers.HyperlinkedModelSerializer):
        class AnimeSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Anime
                fields = ['url', 'romaji_title', 'format', 'status', 'cover_img_med']
        anime = AnimeSer(source='senior_anime_id')

        class Meta:
            model = AnimeRelation
            fields = ['anime', 'relation']
        
        def to_representation(self, instance):
            data = super().to_representation(instance)
            anime_data = data.pop('anime')
            for key in anime_data:
                data[key] = anime_data[key]
            return data
        
    class CharacterInAnimeSer(serializers.HyperlinkedModelSerializer):
        class CharacterSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Character
                fields = ['name', 'img_med']
        
        class VoiceStaffSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Staff
                fields = ['name', 'img_med']

        character = CharacterSer(source='char_id')
        staff = VoiceStaffSer(source='staff_id')

        class Meta:
            model = CharacterInAnime
            fields = ['character', 'staff', 'char_role']

        def to_representation(self, instance):
            data = super().to_representation(instance)
            char_data = data.pop('character')
            staff_data = data.pop('staff')
            for key in char_data:
                data['char_' + key] = char_data[key]
            for key in staff_data:
                data['staff_' + key] = staff_data[key]
            return data

    tags = AnimeTagSer(many=True, source='animetag_set', read_only=True)
    relations = AnimeRelationSer(many=True, source='animerelation_set', read_only=True)
    characters = CharacterInAnimeSer(many=True, source='characterinanime_set', read_only=True)
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