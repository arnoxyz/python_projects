# Implementation of BlackJack
import random 


#create a new deck
def gen_deck():
    deck = []

    suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]

    values = {
        "2": 2, "3": 3, "4": 4, "5": 5, "6": 6,
        "7": 7, "8": 8, "9": 9, "10": 10,
        "J": 10, "Q": 10, "K": 10, "A": 11  
    }

    for suit in suits:
        for rank in ranks:
            card = {
                "rank": rank,
                "suit": suit,
                "value": values[rank]
            }
            deck.append(card)

    return deck;


deck = gen_deck();
print(deck)
