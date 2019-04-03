from django.contrib import admin
from core.models import Deck, Card, Profile, Rate, Review, Category 
# Register your models here.
@admin.register(Deck)
class DeckAdmin(admin.ModelAdmin):
    pass

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    pass

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Rate)
class RateAdmin(admin.ModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
