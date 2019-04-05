from django.urls import path
from . import views
from django.db import models
from django.urls import reverse
from django.conf.urls import url


urlpatterns = [
    path('', views.home, name='home'),
    path('createdeck/', views.createDeck, name='new_deck'),
    path('createcard/', views.createCard, name='new_card'),
    path('profile/', views.profile, name='profile'),
]
