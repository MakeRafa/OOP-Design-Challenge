import random
from Card import Card
from Deck import Deck

class Player:
    def __init__(self, name, starting_amt):
        self.name = name
        self.starting_amt = starting_amt
        self.player_cards = []

    def getHand(self):
        print(len(self.player_cards))


rafa = Player("rafa", 50)

rafa.getHand()