from django.forms import ModelForm
from .models import Deck

class DeckForm(ModelForm):
    '''
    Form mapping to the deck model
    '''
    class Meta:
        model = Deck
        fields = ['title', 'description', 'is_active']
