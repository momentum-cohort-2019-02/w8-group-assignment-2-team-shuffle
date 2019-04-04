from django.shortcuts import (
        get_object_or_404,
        HttpResponseRedirect,
        render,
    )
from .models import Deck
from .forms import DeckForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    context = {'deck': Deck.objects.all()}
    return render(request, 'index.html', context)


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
