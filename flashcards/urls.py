#FLASHCARDS URL CONF
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'decks/create/', views.createDeck, name='createDeck'),
    url(r'decks/edit/(?P<deck_id>[\d]+)', views.editDeck, name='editDeck')
]
