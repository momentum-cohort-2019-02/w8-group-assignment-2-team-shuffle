
from django.shortcuts import get_object_or_404, HttpResponseRedirect, render, redirect
from core.models import Deck, Card, Category, Rate, Profile
from core.forms import DeckForm, NewCardForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.urls import reverse
from django.db.models import Q



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
            created_by = request.user
            deck.save()

            return HttpResponseRedirect(reverse('home'))
    else:
        form = DeckForm()
    return render(request, 'create_deck.html', {'form': form})
    

def createCard(request):
    if request.method == "POST":
        form = NewCardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            return redirect('core-profile')
    else:
        form = PostForm()
    return render(request, 'core/profile.html', {'form': form})

@login_required
def profile(request):
    decks = Deck.objects.all()
    profiles = Profile.objects.all()
    paginator = Paginator(decks, 10)
    page = request.GET.get('page', 1)
    decks = paginator.get_page(page)


    context = {
        'decks': decks,
        'profiles': profiles,
    }
    return render(request, 'profile.html', context=context)
