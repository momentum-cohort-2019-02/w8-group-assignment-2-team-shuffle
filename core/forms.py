from django.forms import ModelForm
from .models import Deck, Card
from django import forms

class DeckForm(ModelForm):
    '''
    Form mapping to the deck model 
    '''
    class Meta:
        model = Deck
        fields = ['title', 'created_by'] 

class NewCardForm(forms.ModelForm):
    deck = forms.CharField(
        label='deck',
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'add deck name'}))

    question = forms.CharField(
        label='question',
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'add question'}))
   
    answer = forms.CharField(
        label='answer',
        max_length=200,
        widget=forms.TextInput(attrs={'placeholder': 'add answer'}))
    
    url = forms.URLField(
        label='url',
        max_length=200,

       )
    
    class Meta:
        model = Card
        fields = ['deck', 'question', 'answer', 'url']