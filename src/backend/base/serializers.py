from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import *

#Anime view serializers
class AnimeViewSerializer(serializers.HyperlinkedModelSerializer):
    # Tag Serializer in anime view
    class AnimeTagSer(serializers.HyperlinkedModelSerializer):
        class TagSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Tag
                fields = ['url', 'name', 'description', 'is_general_spoiler']
        tag = TagSer(source='tag_id')
        class Meta:
            model = AnimeTag
            fields = ['url', 'tag', 'rank', 'is_spoiler']

    # Anime relation serializer in anime view
    class AnimeRelationSer(serializers.HyperlinkedModelSerializer):
        class AnimeSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Anime
                fields = ['url', 'romaji_title', 'format', 'status', 'cover_img_med']
        anime = AnimeSer(source='senior_anime_id')

        class Meta:
            model = AnimeRelation
            fields = ['url', 'anime', 'relation']
    
    # Character in anime serializer in anime view
    class CharacterInAnimeSer(serializers.HyperlinkedModelSerializer):
        class CharacterSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Character
                fields = ['url', 'name', 'img_med']
        
        class VoiceStaffSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Staff
                fields = ['url', 'name', 'img_med']

        character = CharacterSer(source='char_id')
        staff = VoiceStaffSer(source='staff_id')

        class Meta:
            model = CharacterInAnime
            fields = ['url', 'character', 'staff', 'char_role']
        
    # staff in anime serializer
    class StaffInAnimeSer(serializers.HyperlinkedModelSerializer):
        class StaffSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Staff
                fields = ['url', 'name', 'img_med']

        staff = StaffSer(source='staff_id')

        class Meta:
            model = StaffInAnime
            fields = ['url', 'staff', 'staff_role']

    # studio made anime serializer
    class AnimeProducedByStudioSer(serializers.HyperlinkedModelSerializer):
        class StudioSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Studio
                fields = ['url', 'name']
            
        studio = StudioSer(source='studio_id')

        class Meta:
            model = AnimeProducedByStudio
            fields = ['url', 'studio', 'is_main']
        
    class AnimeExternalLinkSer(serializers.HyperlinkedModelSerializer):
        class ExternalSiteSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = ExternalSite
                fields = ['name', 'icon', 'language']
        
        site = ExternalSiteSer(source='site_id')

        class Meta:
            model = AnimeExternalLink
            fields = ['site', 'url']

    tags = AnimeTagSer(many=True, source='animetag_set', read_only=True)
    relations = AnimeRelationSer(many=True, source='animerelation_set', read_only=True)
    characters = CharacterInAnimeSer(many=True, source='characterinanime_set', read_only=True)
    staffs = StaffInAnimeSer(many=True, source='staffinanime_set', read_only=True)
    studios = AnimeProducedByStudioSer(many=True, source='animeproducedbystudio_set', read_only=True)
    links = AnimeExternalLinkSer(many=True, source='animeexternallink_set', read_only=True)
    
    class Meta:
        model = Anime
        fields = [field.name for field in Anime._meta.fields]
        fields += ['tags', 'relations', 'characters', 'staffs', 'studios', 'links']


class AnimeListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Anime
        fields = ['url', 'id', 'id_anilist', 'romaji_title', 'format', 'status', 'start_date', 'end_date', 'episodes', 'duration', 'cover_img_large', 'cover_img_med', 'weighted_score', 'anilist_score', 'mean_score', 'popularity', 'trending', 'favorites']
    
class StudioViewSerializer(serializers.HyperlinkedModelSerializer):
    animes = AnimeListSerializer(many=True, read_only=True)
    class Meta:
        model = Studio
        fields = ['url', 'name', 'favorites', 'animes']

class StudioListSerializer(serializers.HyperlinkedModelSerializer):
    #animes = AnimeListSerializer(many=True, read_only=True)
    class Meta:
        model = Studio
        fields = ['url', 'name', 'favorites']

class StaffListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Staff
        fields = ['url', 'id', 'name', 'name_native', 'img_large', 'img_med']

class StaffViewSerializer(serializers.HyperlinkedModelSerializer):
    class VoicedCharacterSer(serializers.HyperlinkedModelSerializer):
        class AnimeSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Anime
                fields = ['url', 'romaji_title', 'cover_img_large', 'cover_img_med']
        class CharacterSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Character
                fields = ['url', 'name', 'img_large', 'img_med']

        character = CharacterSer(source='char_id')
        anime = AnimeSer(source='anime_id')
        class Meta:
            model = CharacterInAnime
            fields = ['character', 'anime', 'char_role']

    class StaffRoleSer(serializers.HyperlinkedModelSerializer):
        class AnimeSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Anime
                fields = ['url', 'romaji_title', 'cover_img_large', 'cover_img_med']

        anime = AnimeSer(source='anime_id')
        class Meta:
            model = StaffInAnime
            fields = ['anime', 'staff_role']

    staff_roles = StaffRoleSer(many=True, source='staffinanime_set', read_only=True)
    voiced_characters = VoicedCharacterSer(many=True, source='characterinanime_set', read_only=True)
    class Meta:
        model = Staff
        fields = [field.name for field in Staff._meta.fields]
        fields += ['staff_roles', 'voiced_characters']

class CharacterListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Character
        fields = ['url', 'name', 'name_native', 'img_large', 'img_med', 'favorites']

class CharacterViewSerializer(serializers.HyperlinkedModelSerializer):
    class CharInAnimeSer(serializers.HyperlinkedModelSerializer):
        class AnimeSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Anime
                fields = ['url', 'romaji_title', 'cover_img_large', 'cover_img_med']
        
        class StaffSer(serializers.HyperlinkedModelSerializer):
            class Meta:
                model = Staff
                fields = ['url', 'name', 'img_large', 'img_med']

        anime = AnimeSer(source='anime_id')
        staff = StaffSer(source='staff_id')
        class Meta:
            model = CharacterInAnime
            fields = ['char_role', 'anime', 'staff']

    in_animes = CharInAnimeSer(many=True, source='characterinanime_set', read_only=True)

    class Meta:
        model = Character
        fields = [field.name for field in Character._meta.fields]
        fields += ['in_animes']

class TagListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class AnimeProducedByStudioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimeProducedByStudio
        fields = '__all__'

class StaffInAnimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = StaffInAnime
        fields = '__all__'

class AnimeTagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimeTag
        fields = '__all__'

class AnimeRelationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AnimeRelation
        fields = '__all__'

class CharacterInAnimeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CharacterInAnime
        fields = '__all__'