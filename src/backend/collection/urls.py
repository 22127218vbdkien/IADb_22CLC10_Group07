from django.urls import include, re_path
from rest_framework.routers import DefaultRouter

from collection import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'favoritecharacters', views.FavoriteCharacterViewSet, basename='favoritecharacter')
router.register(r'favoritestudios', views.FavoriteStudioViewSet, basename='favoritestudio')
router.register(r'favoritestaffs', views.FavoriteStaffViewSet, basename='favoritestaff')
router.register(r'animeincollection', views.AnimeInCollectionViewSet, basename='animeincollection')