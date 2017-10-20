from django.db import models

# Create your models here.
class Deck(models.Model):
    title = models.CharField(max_length=64, null=False, blank=False)
    description = models.CharField(max_length=255, null=False, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_number_of_cards(self):
        '''
        Returns the number of cards in the decks related
        card_set
        '''
        return self.card_set.count()
    get_number_of_cards.short_description = 'Card Count'

class Card(models.Model):
    parentDeck = models.ForeignKey(Deck, on_delete=models.CASCADE)
    front = models.TextField()
    back = models.TextField()

    def __str__(self):
        return self.front

    def has_prev_card(self):
        '''
        Returns true if the card is not the first card
        in the deck.
        '''
        first_card_in_deck = self.parentDeck.card_set.first()
        if self == first_card_in_deck:
            return False
        return True

    def get_prev_card(self):
        '''
        Returns previous card in deck
        '''
        return self.parentDeck.card_set.filter(id__lt=self.id).last()


    def has_next_card(self):
        '''
        Returns true if the card is not the last card
        in the deck
        '''
        last_card_in_deck = self.parentDeck.card_set.last()
        if self == last_card_in_deck:
            return False
        return True

    def get_next_card(self):
        '''
        Returns next card in deck
        '''
        return self.parentDeck.card_set.filter(id__gt=self.id).first()
