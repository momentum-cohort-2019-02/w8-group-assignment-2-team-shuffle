from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# Create your models here.


class Deck(models.Model):
    """ Model representing a Deck. """
    title = models.CharField(max_length=100, null=False,
                             blank=False, unique=True)
    created_by = models.ForeignKey(
        'Profile', on_delete=models.SET_NULL, null=True)
    date_created = models.DateTimeField(
        'Date Created', auto_now_add=True, null=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    """review deck equals false for public decks, review deck equals true for private decks"""
    ownership = models.BooleanField('Ownership', default=False)
    # what other arguments need to go in here ^
    slug = models.SlugField(unique=True, null=True)


    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)


    def set_slug(self):
        if self.slug:
            return

        base_slug = slugify(self.title)
        slug = base_slug
        n = 0

        while Deck.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)


    def __str__(self):
        return str(self.title)


    def get_absolute_url(self):
        return reverse('deck_list', args=[str(self.slug)])


class Card(models.Model):
    """ Model representing a Card"""
    decks = models.ManyToManyField(to=Deck, related_name="cards")
    question = models.TextField(max_length=2000, help_text="Question")
    answer = models.TextField(max_length=2000, help_text="Answer")
    url = models.URLField(null=True, blank=True, help_text="Helpful link")
    answered_correctly = models.BooleanField("Answered correctly", default=False)



    def __str__(self):
        return str(self.question)


class Profile(models.Model):
    """ Model representing a Profile """
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return str(self.user)


    def get_absolute_url(self):
        return reverse('profile', args=[str(self.slug)])


class Category(models.Model):
    """ Model representing a Catergory"""
    deck_category = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        self.set_slug()
        super().save(*args, **kwargs)


    def set_slug(self):
        if self.slug:
            return

        base_slug = slugify(self.deck_category)
        slug = base_slug
        n = 0

        while Category.objects.filter(slug=slug).count():
            n += 1
            slug = base_slug + "-" + str(n)


    def __str__(self):
        return str(self.deck_category)


    def get_absolute_url(self):
        return reverse('home', args=[str(self.slug)])


class Rate(models.Model):
    """ Model representing the "was this helpful" """
    is_helpful = models.NullBooleanField()
    deck = models.ForeignKey(Deck, on_delete=models.CASCADE, null=True,
    related_name='deck_rates')
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='profile_rates')


# this is a comment