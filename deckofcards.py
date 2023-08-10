import random
from cardvariables import *

values = list(range(2,15))

class Card:
    def __init__(self, values, suits):
        self.value = values
        self.suits = suits
        

def generate_cards(values, suits):
    cards = []
    for value in values:
        for suit in suits:
            if value in face_cards:
                card_value = face_cards[value]
                cards.append(Card(card_value, suit))
            else:
                cards.append(Card(value, suit))
    return cards

cards = generate_cards(values, suits)

print (random.cards)

    