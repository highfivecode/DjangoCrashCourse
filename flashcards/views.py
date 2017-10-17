from django.shortcuts import render
from .models import Deck

# Create your views here.
def home(request):
    '''
    Renders the FLASHCARD app home template
    '''
    qs = Deck.objects.order_by('-title').filter(is_active=True)
    context = {'decks': qs}
    return render(request, 'flashcards/home.html', context)

def createDeck(request):
    '''
    Renders the form to add new decks to the database
    '''
    if request.method == 'POST':
        print('****************')
        print(request.POST)
        print('****************')
    context = {}
    return render(request, 'flashcards/createDeck.html', context)
