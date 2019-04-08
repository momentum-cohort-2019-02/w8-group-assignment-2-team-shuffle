from django.forms import ModelForm
from .models import Deck, Card
from django import forms

class DeckForm(ModelForm):
    '''
    Form mapping to the deck model 
    '''
    class Meta:
        model = Deck
        fields = ['title','category', 'ownership']
        



class NewCardForm(forms.ModelForm):
    
    class Meta:
        model = Card
        fields = ['question', 'answer', 'url', 'deck']
        