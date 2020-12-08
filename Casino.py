from deck import Deck
from player import Player

class Casino(Deck):
    def __init__(self):
        self.entrance_fee = 0
        
    def check_age(self, age):
        if age < 18:
            print("Sorry you cannot enter")
        elif age > 18 < 65:
            self.entrance_fee = 30
        elif age > 65:
            self.entrance_fee = 15

    def dealCard(self):
        return self.deck_of_cards.pop(0)

deck = Deck()
deck.cardAmount()