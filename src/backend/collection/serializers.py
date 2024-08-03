from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import *
from collection.models import *

# FAVORITE CHARACTER
class FavoriteCharacterListSerializer(serializers.HyperlinkedModelSerializer):
    class CharacterSer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Character
            fields = ['url', 'name', 'img_large', 'img_med']

    character = CharacterSer(source='char_id', read_only=True)
    
    class Meta:
        model = FavoriteCharacter
        fields = ['url', 'character']

class FavoriteCharacterSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.name')
    class Meta:
        model = FavoriteCharacter
        fields = ['user_id', 'char_id']

# FAVORITE STUDIO
class FavoriteStudioListSerializer(serializers.HyperlinkedModelSerializer):
    class StudioSer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Studio
            fields = ['url', 'name']

    studio = StudioSer(source='studio_id', read_only=True)
    
    class Meta:
        model = FavoriteStudio
        fields = ['url', 'studio']

class FavoriteStudioSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.name')
    class Meta:
        model = FavoriteStudio
        fields = ['user_id', 'studio_id']

# FAVORITE STAFF
class FavoriteStaffListSerializer(serializers.HyperlinkedModelSerializer):
    class StaffSer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Staff
            fields = ['url', 'name', 'img_large', 'img_med']

    staff = StaffSer(source='staff_id', read_only=True)
    
    class Meta:
        model = FavoriteStaff
        fields = ['url', 'staff']

class FavoriteStaffSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.id')
    class Meta:
        model = FavoriteStaff
        fields = ['user_id', 'staff_id']

# ANIME COLLECTION
class AnimeInCollectionListSerializer(serializers.HyperlinkedModelSerializer):
    class AnimeSer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Anime
            fields = ['url', 'romaji_title', 'format', 'status', 'start_date', 'end_date', 'episodes', 'duration', 'cover_img_large', 'cover_img_med', 'weighted_score', 'anilist_score', 'mean_score', 'popularity', 'trending', 'favorites']
    
    anime = AnimeSer(source='anime_id', read_only=True)
    class Meta:
        model = AnimeInCollection
        fields = ['url', 'is_favorite', 'in_list', 'score', 'progress', 'start_date', 'finish_date', 'notes', 'anime']

class AnimeInCollectionSerializer(serializers.HyperlinkedModelSerializer):
    user_id = serializers.ReadOnlyField(source='user_id.id')
    class Meta:
        model = AnimeInCollection
        fields = '__all__'