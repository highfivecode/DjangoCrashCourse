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
        title_input = request.POST.get('form_title', None)
        description_input = request.POST.get('form_description', None)
        if 'form_is_active' in request.POST:
            is_active_input = True
        else:
            is_active_input = False
        new_deck = Deck(
                        title = title_input,
                        description = description_input,
                        is_active = is_active_input)
        new_deck.save()
        print('************* NEW DECK SAVED ****************')
    context = {}
    return render(request, 'flashcards/createDeck.html', context)
