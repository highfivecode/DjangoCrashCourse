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

    def test_card_has_prev(self):
        '''
        The first card does not have a prev card.
        All other cards do.
        '''
        self.assertFalse(self.card1.has_prev_card())
        self.assertTrue(self.card2.has_prev_card())
        self.assertTrue(self.card3.has_prev_card())

    def test_card_has_next(self):
        '''
        The last card does not have a next card.
        All other cards do.
        '''
        self.assertTrue(self.card1.has_next_card())
        self.assertTrue(self.card2.has_next_card())
        self.assertFalse(self.card3.has_next_card())
