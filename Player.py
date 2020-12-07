import random
from card import Card
from deck import Deck

class Player:
    def __init__(self, name, starting_amt):
        self.name = name
        self.starting_amt = starting_amt

        self.player_cards = []

        self.deck = Deck()
        # self.card = Card()

    def drawCard(self):
        new_card = self.deck.dealCard()
        self.player_cards.append(new_card)
        # self.player_cards[].show_card()
        for cards in self.player_cards:
            cards.show_card()


    def play(self, dealer):
        if self.player_cards < dealer.player_cards:
            self.starting_amt -= 10
            print("Player wins")
        elif dealer.player_cards < self.player_cards:
            self.starting_amt -= 10
            print("Dealer wins")
        else:
            print("You got the same cards")

if __name__ == "__main__":
    rafa = Player("rafa", 50)
    alex = Player("alex", 50)
    rafa.drawCard()
    alex.drawCard()

    rafa.play(alex)



