from Card import Card

import random


class Deck:
    def __init__(self):
        self.deck_of_cards = []
        self.build_deck()


# deck method that creates an individual card for each suit up to 14
    def build_deck(self):
        suits = ["Spades","Hearts", "Clubs","Diamonds"]
        for suit in suits:
            for value in range(1,14):
                # adding an instance of class Card into cards list
                self.deck_of_cards.append(Card(suit,value))

    def shuffle(self):
        random.shuffle(self.deck_of_cards)

    def show(self):
        for card in self.deck_of_cards:
            card.show()

deck = Deck()
# deck.show()
deck.shuffle()
deck.show()