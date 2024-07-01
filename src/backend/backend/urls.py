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
from django.urls import path, include, re_path
from rest_framework.urlpatterns import format_suffix_patterns
from base.views import *
from authentication.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    
    re_path('register', UserRegisterView.as_view()),
    re_path('login', UserLoginView.as_view()),
    
    path('anime/', AnimeList.as_view()),
    path('anime/<int:pk>/', AnimeDetails.as_view()),
    
    path('animeSynonym/', AnimeSynonymList.as_view()),
    path('animeSynonym/<int:pk>/', AnimeSynonymDetails.as_view()),

    path('studio/', StudioList.as_view()),
    path('studio/<int:pk>/', StudioDetails.as_view()),
    
    path('character/', CharacterList.as_view()),
    path('character/<int:pk>/', CharacterDetails.as_view()),  

    path('staff/', StaffList.as_view()),
    path('staff/<int:pk>/', StaffDetails.as_view()),
    
    path('staffInAnime/', StaffInAnimeList.as_view()),
    path('staffInAnime/<int:pk>/', StaffInAnimeDetails.as_view()),  
    
    path('staffVoiceCharacter/', StaffVoiceCharacterList.as_view()),
    path('staffVoiceCharecter/<int:pk>/', StaffVoiceCharacterDetails.as_view()),    

    path('animeProducedByStudio/', AnimeProducedByStudioList.as_view()),
    path('animeProducedByStudio/<int:pk>/', AnimeProducedByStudioDetails.as_view()),  

    path('animeRelation/', AnimeRelationList.as_view()),
    path('animeRelation/<int:pk>/', AnimeRelationDetails.as_view()),  

    path('tag/', TagList.as_view()),
    path('tag/<int:pk>/', TagDetails.as_view()),  

    path('animeTag/', AnimeTagList.as_view()),
    path('animeTag/<int:pk>/', AnimeTagDetails.as_view()), 

    path('externalSite/', ExternalSiteList.as_view()),
    path('externalSite/<int:pk>/', ExternalSiteDetails.as_view()), 

    path('animeExternalLink/', AnimeExternalLinkList.as_view()),
    path('animeExternalLink/<int:pk>/', AnimeExternalLinkDetails.as_view()), 

    path('staffExternalLink/', StaffExternalLinkList.as_view()),
    path('staffExternalLink/<int:pk>/', StaffExternalLinkDetails.as_view()), 
]

urlpatterns = format_suffix_patterns(urlpatterns)