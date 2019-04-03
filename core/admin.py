from django.contrib import admin
from core.models import Deck, Card, Profile, Rate, Category 
# Register your models here.

admin.site.register(Deck)

admin.site.register(Card)

admin.site.register(Profile)

admin.site.register(Rate)

admin.site.register(Category)
