# class to create cards with a suit and value
class Card:
    def __init__(self, card_suit, card_value):
        self.suit = card_suit
        self.value = card_value

    def show_card(self):
        print(f"{self.value} of {self.suit}")
        
    

# card1 = Card("Spades", "7")
# card1.show_card()





