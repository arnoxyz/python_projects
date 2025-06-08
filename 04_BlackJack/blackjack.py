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


def pick_card(current_deck, visible=True):
    choices = current_deck
    while True:
        pick = random.choice(choices)
        if pick['active'] == False:
            pick['active'] = True

            if visible == False:
                pick['visible'] = False
            return pick

def card_value(cards):
    sum = 0
    for card in cards: 
        if card['visible'] == True:
            sum = sum + card['value']
    return sum

def display_cards(cards):
    sum = 0

    card_lines = []
    for card in cards: 
        if card['visible'] == False:
            face_down_card = [
            "┌─────────┐",
            "│         │",
            "│         │",
            "│         │",
            "│         │",
            "│         │",
            "└─────────┘"
            ]
            card_lines.append(face_down_card);


        if card['visible'] == True:
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
    
    #print(f"Hand value: {sum}")

def player_turn(dealer_cards, player_cards, deck):
    game_status = ""
    if card_value(player_cards) == 21: 
        return "Black Jack!"

    while True:
        player_input = (input("Stay (S), Hit (H) -> ")).upper()
        if player_input == "H":
            player_cards.append(pick_card(deck))
            display_game(dealer_cards, player_cards)
        if card_value(player_cards) > 21: 
            game_status = "Player_lost"
            break
        if player_input == "S":
            game_status = "Player_stays"
            break
    return game_status;

def dealer_turn(dealer_cards, player_cards, deck):
    dealer_count_rule = 16 #until this value the dealer must take another card
    game_status = ""

    #reveal the dealer card and display it
    dealer_cards[0]['visible'] = True



    while card_value(dealer_cards) < dealer_count_rule :
        dealer_cards.append(pick_card(deck))
        display_game(dealer_cards, player_cards)


    if card_value(dealer_cards) > 21: 
        return "Dealer_lost"
    if card_value(dealer_cards) > dealer_count_rule :
        display_game(dealer_cards, player_cards)
        return "Dealer_stays"

def display_game(dealer_cards, player_cards):
    print("\n");
    print("Dealer Cards: Value =", card_value(dealer_cards))
    display_cards(dealer_cards)
    print("Your Cards: Value =", card_value(player_cards))
    display_cards(player_cards)


def main():
    # GAME-START:

    # INIT-GAME
    game_status = ""
    player_score_start = 100
    player_score = 100
    player_bet = 50
    player_cards = []
    dealer_cards = []
    # gen new deck
    deck = gen_deck()
    # give dealer two cards
    dealer_cards.append(pick_card(deck, visible=False))
    dealer_cards.append(pick_card(deck))
    # give the player two cards 
    player_cards.append(pick_card(deck))
    player_cards.append(pick_card(deck))

    # USER-TURN
    display_game(dealer_cards, player_cards)
    game_status = player_turn(dealer_cards, player_cards, deck)

    if game_status == "Black Jack!":
        player_score = player_score + 2*player_bet;
    if game_status == "Player_lost":
        player_score = player_score - player_bet;

    # DEALER-TURN
    if game_status == "Player_stays":
        game_status = dealer_turn(dealer_cards, player_cards, deck)
        if game_status == "Dealer_lost":
            player_score = player_score + player_bet;
        if game_status == "Dealer_stays":
            dealer_val = card_value(dealer_cards)
            player_val = card_value(player_cards)

            if dealer_val == player_val:
                player_score = player_score + player_bet
                game_status = "Tie"
            if dealer_val > player_val: 
                player_score = player_score - player_bet
                game_status = "Player_lost"
            if dealer_val < player_val:
                player_score = player_score + player_bet
                game_status = "Player_win"

    print(game_status)
    print("Player Score before \t= "+str(player_score_start))
    print("Player Score now \t= "+str(player_score))
    print("Diff \t\t\t= "+str(player_score-player_score_start))

main()
