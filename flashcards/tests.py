from django.test import TestCase
from .models import Card, Deck

# Create your tests here.
class CardTestCase(TestCase):
    deck = None
    card1 = None
    card2 = None
    card3 = None

    def setUp(self):
        '''
        Sets up our testing fixture and creates objects
        which we can use in future tests
        '''
        self.deck = Deck.objects.create(title='test_deck_1')
        self.card1 = Card.objects.create(
                                            parentDeck=self.deck,
                                            front='Front of card1',
                                            back='Back of card1'
                                        )
        self.card2 = Card.objects.create(
                                            parentDeck=self.deck,
                                            front='Front of card2',
                                            back='Back of card2'
                                        )
        self.card3 = Card.objects.create(
                                            parentDeck=self.deck,
                                            front='Front of card3',
                                            back='Back of card3'
                                        )

    def test_starting_conditions(self):
        '''
        Check if deck and cards exists
        '''
        self.assertIsInstance(self.deck, Deck)
        self.assertIsInstance(self.card1, Card)
        self.assertIsInstance(self.card2, Card)
        self.assertIsInstance(self.card3, Card)
