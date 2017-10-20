#FLASHCARDS URL CONF
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'decks/create/', views.createDeck, name='createDeck'),
    url(r'decks/edit/(?P<deck_id>[\d]+)', views.editDeck, name='editDeck'),
    url(r'decks/delete/(?P<deck_id>[\d]+)', views.deleteDeck, name='deleteDeck'),
    url(r'decks/view/(?P<deck_id>[\d]+)', views.viewDeck, name='viewDeck'),
    url(r'cards/create/(?P<deck_id>[\d]+)', views.createCard, name='createCard'),
    url(r'cards/edit/(?P<card_id>[\d]+)', views.editCard, name='editCard'),
    url(r'cards/delete/(?P<card_id>[\d]+)', views.deleteCard, name='deleteCard')
]
