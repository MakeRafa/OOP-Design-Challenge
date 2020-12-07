from Card import Card

import random

class Deck():
    def __init__(self):
        self.deck_of_cards = []
        self.build_deck()

# deck method that creates an individual card for each suit up to 14
    def build_deck(self):
        suits = ["Spades","Hearts", "Clubs","Diamonds"]
        for suit in suits:
            for value in range(1,11):
                # adding an instance of class Card into cards list
                self.deck_of_cards.append(Card(suit,value))

    def cardAmount(self):
        print(f"Cards in Deck: {len(self.deck_of_cards)}")

    def cards(self):
        for card in self.deck_of_cards:
            card.show_card()
        print(f"Cards in Deck: {len(self.deck_of_cards)}")

    def shuffle(self):
        random.shuffle(self.deck_of_cards)
        print("Deck is Shuffled")

    def dealCard(self):
        return self.deck_of_cards.pop(0)
        
    

# deck = Deck()
# deck.dealCard()
# card1 = deck.dealCard()
# print(card1.show_card())

# card2 = deck.dealCard()
# print(card2.show_card())

# card3 = deck.dealCard()
# print(card3.show_card())

# deck.cardAmount()
