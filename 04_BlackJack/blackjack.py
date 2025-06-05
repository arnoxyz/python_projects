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
                "value": values[rank],
                "active": False,
                "visible": True
            }
            deck.append(card)

    return deck;


def pick_card(deck):
    choices = deck
    while True:
        pick = random.choice(choices)
        if pick['active'] == False:
            pick['active'] = True;
            return pick

def add_cards(cards):
    sum = 0
    for card in cards: 
        sum = sum + card['value']
    return sum

def display_cards(cards):
    sum = 0

    card_lines = []
    for card in cards: 
        suit_symbols = {
            "Hearts": "♥",
            "Diamonds": "♦",
            "Clubs": "♣",
            "Spades": "♠"
        }
        rank = card["rank"]
        suit = suit_symbols[card["suit"]]
        rank_left = rank.ljust(2)
        rank_right = rank.rjust(2)

        value = card['value']
        sum += value

         # Pad rank for display
        rank_str = rank.ljust(2) if len(rank) == 1 else rank

        # ASCII card template
        card_lines.append([
            "┌─────────┐",
           f"│ {rank_left}      │",
            "│         │",
           f"│    {suit}    │",
            "│         │",
           f"│      {rank_right} │",
            "└─────────┘"
        ])

    # Print Cards side by side
          #"┌─────────┐",          # Line 0
          #"│ A       │",          # Line 1
          #"│         │",          # Line 2
          #"│    ♠    │",          # Line 3
          #"│         │",          # Line 4
          #"│       A │",          # Line 5
          #"└─────────┘"           # Line 6
        
    # glue all cards together line by line
    for i in range(7):
        #["┌─────────┐", "┌─────────┐", "┌─────────┐"]
        print("  ".join(card[i] for card in card_lines))
    
    print(f"Hand value: {sum}")

player_cards = [];
dealer_cards = [];
deck = gen_deck();

# debug stuff
player_cards.append(pick_card(deck))
player_cards.append(pick_card(deck))
print(player_cards)
print(add_cards(player_cards))
display_cards(player_cards)



