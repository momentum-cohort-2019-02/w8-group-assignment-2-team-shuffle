
from django.shortcuts import get_object_or_404, HttpResponseRedirect, render, redirect
from core.models import Deck, Card, Category, Rate, Profile
from core.forms import DeckForm, NewCardForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse
from django.db.models import Q
from django.views.generic.detail import DetailView


# Create your views here.
def home(request):
    decks = Deck.objects.filter()
    if request.user.is_authenticated:
        #if logged in, you see your owned decks (private to you) plus decks that are not owned by anyone else (public decks)
        decks = Deck.objects.filter((Q(created_by__user=request.user) & Q(ownership=True)) | Q(ownership=False))
    else:
        #if not logged in, you see all decks that are not owned (public decks only)
        decks = Deck.objects.filter(ownership=False)
    categories = Category.objects.all()
    rates = Rate.objects.all()
    profiles = Profile.objects.all()

    paginator = Paginator(decks, 10)
    page = request.GET.get('page', 1)
    decks = paginator.get_page(page)

    context = {
        'decks': decks,
        'categories': categories,
        'rates': rates,
        'profiles': profiles,
    }

    return render(request, 'index.html', context=context)

def createDeck(request):
    if request.method == "POST":
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            profile = Profile.objects.get(user=request.user)
            deck.created_by = profile
            deck.save()

            return HttpResponseRedirect(reverse('new_card'))
    else:
        form = DeckForm()
    return render(request, 'create_deck.html', {'form': form})

@login_required
def createCard(request):
    
    if request.method == "POST":
        form = NewCardForm(request.POST)
        if form.is_valid():
            card = form.save()
            # card.deck = 
            card.save()
            return HttpResponseRedirect(reverse('new_card'))
    else:
        form = NewCardForm()
        form.fields['deck'].queryset = Deck.objects.filter(created_by__user=request.user)
        context = {
            'form': form,
        }
    return render(request, 'card.html', context=context)

@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    decks = Deck.objects.filter(created_by=profile)
    paginator = Paginator(decks, 10)
    page = request.GET.get('page', 1)
    decks = paginator.get_page(page)

    context = {
        'decks': decks,
        'profile': profile,
    }
    return render(request, 'profile.html', context=context)

def viewcard(request):
    model = Card
    context = {'deck': Deck.objects.all()}

    return render(request,'viewCard.html', context)

def category(request, slug):
    categories = Category.objects.all()
    category = Category.objects.get(slug=slug)
    decks = Deck.objects.filter(category=category)
    decks = Deck.objects.filter()
    if request.user.is_authenticated:
        #if logged in, you see categories in decks owned by you plus categories in decks that are owned by anyone else (public decks)
        decks = Deck.objects.filter(((Q(created_by__user=request.user) & Q(ownership=True)) | Q(ownership=False)) & Q(category=category))
    else:
        #if not logged in, you see categories in decks that aren't owned by anyone (public decks only)
        decks = Deck.objects.filter(ownership=False, category=category)
    paginator = Paginator(decks, 10)
    page = request.GET.get('page', 1)
    decks = paginator.get_page(page)
    context = {
        'decks': decks,
        'category': category,
        'categories': categories,
    }
    return render(request, 'category_view.html', context=context)
