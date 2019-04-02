from django.contrib import admin
from core.models import Deck, Card, Profile, Rate, Review, Category 
# Register your models here.
admin.site.Register(Deck)
admin.site.Register(Card)
admin.site.Register(Profile)
admin.site.Register(Rate)
admin.site.Register(Review)
admin.site.Register(Category)
