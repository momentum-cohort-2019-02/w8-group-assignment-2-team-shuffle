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
    path('createdeck/card/', views.createCard, name='new_card'),
    path('profile/', views.profile, name='profile'),
    path('viewcard/', views.viewcard, name='view_card'),
    path('category/<slug:slug>', views.category,name='category'),
    path('viewdeck/<int:deck_id>/', views.viewdeck, name='view_deck'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
