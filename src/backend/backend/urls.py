"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from rest_framework.urlpatterns import format_suffix_patterns
from base import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    re_path('signup', views.SignupView.as_view()), 
    re_path('login', views.LoginView.as_view()),
    
    path('anime/', views.AnimeList.as_view()),
    path('anime/<int:pk>/', views.AnimeDetails.as_view()),
    
    path('animeSynonym/', views.AnimeSynonymList.as_view()),
    path('animeSynonym/<int:pk>/', views.AnimeSynonymDetails.as_view()),

    path('studio/', views.StudioList.as_view()),
    path('studio/<int:pk>/', views.StudioDetails.as_view()),
    
    path('character/', views.CharacterList.as_view()),
    path('character/<int:pk>/', views.CharacterDetails.as_view()),  

    path('staff/', views.StaffList.as_view()),
    path('staff/<int:pk>/', views.StaffDetails.as_view()),
    
    path('staffInAnime/', views.StaffInAnimeList.as_view()),
    path('staffInAnime/<int:pk>/', views.StaffInAnimeDetails.as_view()),  
    
    path('staffVoiceCharacter/', views.StaffVoiceCharacterList.as_view()),
    path('staffVoiceCharecter/<int:pk>/', views.StaffVoiceCharacterDetails.as_view()),    

    path('animeProducedByStudio/', views.AnimeProducedByStudioList.as_view()),
    path('animeProducedByStudio/<int:pk>/', views.AnimeProducedByStudioDetails.as_view()),  

    path('animeRelation/', views.AnimeRelationList.as_view()),
    path('animeRelation/<int:pk>/', views.AnimeRelationDetails.as_view()),  

    path('tag/', views.TagList.as_view()),
    path('tag/<int:pk>/', views.TagDetails.as_view()),  

    path('animeTag/', views.AnimeTagList.as_view()),
    path('animeTag/<int:pk>/', views.AnimeTagDetails.as_view()), 

    path('externalSite/', views.ExternalSiteList.as_view()),
    path('externalSite/<int:pk>/', views.ExternalSiteDetails.as_view()), 

    path('animeExternalLink/', views.AnimeExternalLinkList.as_view()),
    path('animeExternalLink/<int:pk>/', views.AnimeExternalLinkDetails.as_view()), 

    path('staffExternalLink/', views.StaffExternalLinkList.as_view()),
    path('staffExternalLink/<int:pk>/', views.StaffExternalLinkDetails.as_view()), 
]

urlpatterns = format_suffix_patterns(urlpatterns)