from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User 

# Create your models here.


class Deck(models.Model):
    ''' Model representing a Deck. '''
    title = models.CharField(max_length=100, null=False, Blank=False unique=True)
    post_by = models.ForeignKey(
        'Profile', on_delete=models.SET_NULL, null=True)
    date_posted = models.DateTimeField(
        'Date Created', auto_now_add=True, null=true)
    date_edited = models.DateTimeField(null=True auto_now=True)
    deck_category = models.ManyToManyField(Category)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title


class Card(models.Model):
    ''' Model representing a Card ''' 
    decks = models.ForeignKey(Deck, on_delete=models.CASCADE)
    front = models.TextField(max_length=300)
    back = models.TextField(max_length=500)
    slug = models.SlugField(unique=True)



    def __str__(self):
        return self.front


class Profile(models.Model):
    ''' Model representing a Profile ''' 
    User = get_user_model()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    def get_absolute_url(self):
        return reverse('core-deck', args=(self.pk))


class Category(models.Model):
    ''' Model representing a Catergory''' 
        deck_category = models.CharField(max_length=200,)
        # find a way to make a drop menu to choose Category
        slug = models.SlugField(unique=True)
        

        def __str__(self):
            return self.deck_category

        def get_absolute_url(self):
            return self.deck_category
    


class Rate(models.Model):
    ''' Model representing the "was this helpful" '''
    post = models.ForeignKey(
        Deck,
        on_delete=models.CASCADE,
        null=True,
        related_name='my_deck_rates')
    profile = models.ForeignKey(
        'Profile',
        on_delete=models.CASCADE,
        null=True,
        related_name="my_profile_rates")


class Review(models.Model):
    ''' This Model represnts the review deck ''' 
    review_deck = models.ForeignKey(Profile, blank=True, null=True)
    review_card = models.ForeignKey(Card)
    review_title = models.CharField(max_length=200, unique=True)

