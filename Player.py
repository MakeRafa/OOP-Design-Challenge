import random
from card import Card
from deck import Deck

class Player:
    def __init__(self, name, starting_amt, age):
        self.name = name
        self.starting_amt = starting_amt
        self.age = age

        self.player_cards = []

        # self.deck = Deck()
        # self.card = Card()

    def drawCard(self, deck):
        new_card = deck.dealCard()
        self.player_cards.append(new_card)
        # self.player_cards[].show_card()
        # for card in self.player_cards:
        #     card.show_card()
        new_card.show_card()


    def play(self, dealer):
        player_sum = 0
        for card in self.player_cards:
            player_sum += card.value
        print(player_sum)

        # if len(self.player_cards) > len(dealer.player_cards):
        #     self.starting_amt -= 10
        #     print("Player wins")
        # elif len(dealer.player_cards) > len(self.player_cards):
        #     dealer.starting_amt -= 10
        #     print("Dealer wins")
        # else:
        #     print("You got the same cards")

if __name__ == "__main__":
    rafa = Player("rafa", 50, 30)
    alex = Player("alex", 100, 10)
    deck = Deck()

    rafa.drawCard(deck)
    rafa.drawCard(deck)
    rafa.drawCard(deck)

    alex.drawCard(deck)
    alex.drawCard(deck)
    rafa.play(alex)

# print(rafa.starting_amt)

