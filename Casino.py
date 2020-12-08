from deck import Deck
from player import Player

class Casino():
    def __init__(self):
        self.__entrance_fee = 0
        self.tables = []
    
    def check_age(self, age):
        if age < 18:
            print("Sorry you cannot enter")
        elif age > 18 < 65:
            self.entrance_fee = 30
        elif age > 65:
            self.entrance_fee = 15

    def welcome(self):
        print("Welcome to the casino!")

# lasVegas = Casino()
# lasVegas.welcome()
# create_deck = Deck()
# create_deck.shuffle()
# player = Player("rafa", 100, 18)
# dealer = Player("Afar", 1000, 70)
# create_deck.cardAmount()
# player.drawCard(create_deck)
# rafa.drawCard(create_deck)
# dealer.drawCard(create_deck)
# dealer.drawCard(create_deck)
# create_deck.cardAmount()
# rafa.play(dealer)

