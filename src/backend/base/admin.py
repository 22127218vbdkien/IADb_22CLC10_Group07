from django.contrib import admin
from base.models import *

@admin.register(
    Anime, 
    AnimeSynonym, 
    Studio, 
    Character, 
    Staff,
    StaffInAnime,
    CharacterInAnime,
    AnimeProducedByStudio,
    AnimeRelation,
    Tag,
    AnimeTag,
    ExternalSite,
    AnimeExternalLink,
    StaffExternalLink
)
class UniversalAdmin(admin.ModelAdmin):
    def get_list_display(self, request):
        return [field.name for field in self.model._meta.concrete_fields]