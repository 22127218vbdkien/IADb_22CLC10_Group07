from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from base import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'animes', views.AnimeViewSet, basename='anime')
router.register(r'studios', views.StudioViewSet, basename='studio')
router.register(r'staffs', views.StaffViewSet, basename='staff')
router.register(r'characters', views.CharacterViewSet, basename='character')
router.register(r'tags', views.TagViewSet, basename='tag')

router.register(r'animeproducedbystudio', views.AnimeProducedByStudioViewSet, basename='animeproducedbystudio')
router.register(r'staffinanime', views.StaffInAnimeViewSet, basename='staffinanime')
router.register(r'animetag', views.AnimeTagViewSet, basename='animetag')
router.register(r'animerelation', views.AnimeRelationViewSet, basename='animerelation')
router.register(r'characterinanime', views.CharacterInAnimeViewSet, basename='characterinanime')