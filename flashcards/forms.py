from django.forms import ModelForm
from .models import Deck, Card

class DeckForm(ModelForm):
    '''
    Form mapping to the deck model
    '''
    class Meta:
        model = Deck
        fields = ['title', 'description', 'is_active']

class CardForm(ModelForm):
    '''
    Form mapping to the card model
    '''
    class Meta:
        model = Card
        fields = ['parentDeck', 'front', 'back']
