from django.urls import path
from . import views
from django.db import models
from django.urls import reverse
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('createdeck/', views.createDeck, name='new_deck'),
    path('createcard/', views.createCard, name='new_card'),
    path('profile/', views.profile, name='profile'),
    path('category/<slug:slug>', views.category,name='category'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
