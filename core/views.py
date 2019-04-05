from django.shortcuts import get_object_or_404, HttpResponseRedirect, render, redirect
from core.models import Deck, Card, Category, Rate, Profile
from core.forms import DeckForm
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator


# Create your views here.
def home(request):
    decks = Deck.objects.all()
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


def create_Deck(request):
    if request.method == "POST":
        form = DeckForm(request.POST)
        if form.is_valid():
            deck = form.save(commit=False)
            deck.save()
            return redirect('core-home')
    else:
        form = PostForm()
    return render(request, 'core/create_deck.html', {'form': form})

def create_Card(request):
    if request.method == "POST":
        form = NewCardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.save()
            return redirect('core-profile')
    else:
        form = PostForm()
    return render(request, 'core/profile.html', {'form': form})
    