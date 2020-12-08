import random
from deck import Deck

class Player:
    def __init__(self, name, money_amt, age):
        self.name = name
        self.starting_amt = money_amt
        self.age = age

        self.player_cards = []

        # self.deck = Deck()
        # self.card = Card()

    def drawCard(self, deck):
        new_card = deck.dealCard()
        self.player_cards.append(new_card)
        new_card.show_card()


    def play(self, dealer):
        player_sum = 0
        dealer_sum = 0
        for card in self.player_cards:
            player_sum += card.value
        # print(player_sum)
        for card in dealer.player_cards:
            dealer_sum += card.value
        # print(dealer_sum)
        if player_sum > dealer_sum:
            print(f"Player wins: {player_sum} to {dealer_sum}")
        elif dealer_sum > player_sum:
            print(f"Dealer Wins: {dealer_sum} to {player_sum}")
        else:
            print("You got the same cards")


        

# if __name__ == "__main__":
#     rafa = Player("rafa", 50, 30)
#     alex = Player("alex", 100, 10)
#     deck = Deck()
#     deck.cardAmount()
#     deck.shuffle()

#     rafa.drawCard(deck)
#     rafa.drawCard(deck)
#     rafa.drawCard(deck)
#     deck.cardAmount()
#     alex.drawCard(deck)
#     alex.drawCard(deck)
#     rafa.play(alex)

# print(rafa.starting_amt)

