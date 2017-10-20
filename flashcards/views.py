from django.shortcuts import (
        get_object_or_404,
        HttpResponseRedirect,
        render,
    )
from .forms import CardForm, DeckForm
from .models import Card, Deck

# Create your views here.
def home(request):
    '''
    Renders the FLASHCARD app home template
    '''
    qs = Deck.objects.order_by('-title').filter(is_active=True)
    context = {'decks': qs}
    return render(request, 'flashcards/home.html', context)

def createCard(request, deck_id):
    '''
    Used to create a card for the deck with the given deck_id
    '''
    deck_obj = get_object_or_404(Deck, id=deck_id)
    if request.method == 'POST':
        form = CardForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/flashcards')
    else:
        form = CardForm(initial={'parentDeck':deck_obj})
    context = {'form': form}
    return render(request, 'flashcards/createAndEditCard.html', context)

def createDeck(request):
    '''
    Renders the form to add new decks to the database
    '''
    if request.method == 'POST':
        # create the form isntance, and populate with data from the request
        form = DeckForm(request.POST)
        # check if the form is valid
        if form.is_valid():
            #save the form, this saves the object to the database
            form.save()
            return HttpResponseRedirect('/flashcards')
    else:
        form = DeckForm()
    context = {'form': form}
    return render(request, 'flashcards/createAndEditDeck.html', context)

def deleteCard(request, card_id):
    '''
    Deletes the card whose id == card_id
    '''
    card_obj = get_object_or_404(Card, id=card_id)
    card_obj.delete()
    return HttpResponseRedirect('/flashcards')

def deleteDeck(request, deck_id):
    '''
    Deletes the deck whose id == deck_id
    '''
    deck_obj = get_object_or_404(Deck, id=deck_id)
    deck_obj.delete()
    return HttpResponseRedirect('/flashcards')

def editCard(request, card_id):
    '''
    Renders the form to edit information about a card
    '''
    card_obj = get_object_or_404(Card, id=card_id)
    if request.method == 'POST':
        form = CardForm(request.POST, instance=card_obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/flashcards')
    else:
        form = CardForm(instance=card_obj)
    context = {'form':form, 'edit_mode':True, 'card_obj':card_obj}
    return render(request, 'flashcards/createAndEditCard.html', context)

def editDeck(request, deck_id):
    '''
    Renders the form to edit information about a deck object
    '''
    deck_obj = get_object_or_404(Deck, id=deck_id)
    if request.method == 'POST':
        # create the form isntance, and populate with data from the request
        form = DeckForm(request.POST, instance=deck_obj)
        # check if the form is valid
        if form.is_valid():
            #save the form, this saves the object to the database
            form.save()
            return HttpResponseRedirect('/flashcards')
    else:
        form = DeckForm(instance=deck_obj)
    context = {'form': form, 'edit_mode':True, 'deck_obj':deck_obj}
    return render(request, 'flashcards/createAndEditDeck.html', context)

def viewDeck(request, deck_id):
    '''
    Gets deck from the database.
    Return first card in deck unless card_id is specified in url
    '''
    deck_obj = get_object_or_404(Deck, id=deck_id)
    card_list = deck_obj.card_set.all()
    card_obj = card_list.first()
    print(deck_obj)
    print(card_list)
    print(card_obj)
    context = {'deck_obj': deck_obj, 'card_obj':card_obj}
    return render(request, 'flashcards/viewDeck.html', context)
