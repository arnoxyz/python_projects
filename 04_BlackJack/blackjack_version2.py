# Other implementation of Blackjack
import random, sys

HEARTS   = chr(9829) #'♥'
DIAMONDS = chr(9830) #'♦'
SPADES   = chr(9824) #'♠'
CLUBS    = chr(9827) #'♣'
BACKSIDE = 'backside'

def main():
    print("hello world")
    money = 5000
    while True: 
        if money <= 0:
            print("game over = no money left")
            sys.exit()

        print("Money:", money)
        bet = get_bet(money)

        deck = get_deck()
        dealer_hand = [deck.pop(), deck.pop()]
        player_hand = [deck.pop(), deck.pop()]

        # Player Actions:
        print("Bet:", bet)
        while True:
            display_hands(player_hand, dealer_hand, False)
            print()
            
            if get_hand_value(player_hand) > 21:
                break

            # get players move (H,S,D)
            move = get_move(player_hand, money - bet)
            
            # handle action
            if move == 'D':
                additional_bet = get_bet(min(bet, (money - bet)))
                bet += additional_bet
                print("Bet increased to {}.".format(bet))

            if move in ('H', 'D'):
                new_card = deck.pop()
                rank, suit = new_card
                print("You drew a {} of {}.".format(rank, suit))
                player_hand.append(new_card)

                if get_hand_value(player_hand) > 21:
                    continue

            if move in ('S', 'D'):
                break

        # Dealer Actions:
        if get_hand_value(player_hand) <= 21:
            while get_hand_value(dealer_hand) < 17: 
                print("Dealer hit")
                dealer_hand.append(deck.pop())
                display_hands(player_hand, dealer_hand, False)

                if get_hand_value(dealer_hand) > 21:
                      break
                input("Press Enter to continue")

        # Final Results:
        display_hands(player_hand, dealer_hand, True)
        player_value = get_hand_value(player_hand)
        dealer_value = get_hand_value(dealer_hand)

        if dealer_value > 21:
            print("You win")
            money += bet
        elif ((player_value > 21) or (player_value < dealer_value)):
            print("You lost")
            money -= bet
        elif (player_value > dealer_value):
            print("You win")
            money += bet
        elif player_value == dealer_value:
            print("Tie")

        input("Press Enter to continue");
        print("\n\n")

def get_bet(max_bet):
    while True:  
        print('How much do you bet? (1-{}, or (q)uit)'.format(max_bet))
        bet = input('> ').lower().strip()
        if bet == 'q':
            print('Thanks for playing!')
            sys.exit()

        if not bet.isdecimal():
            continue  # If the player didn't enter a number, ask again.

        bet = int(bet)
        if 1 <= bet <= max_bet:
            return bet  # Player entered a valid bet.


def get_deck():
    deck = []
    for suit in (HEARTS, DIAMONDS, SPADES, CLUBS):
        for rank in range(2, 11):
            deck.append((str(rank), suit))  
        for rank in ('J', 'Q', 'K', 'A'):
            deck.append((rank, suit))  
    random.shuffle(deck)
    return deck


def display_hands(player_hand, dealer_hand, show_dealer_hand):
    print()
    if show_dealer_hand:
        print('DEALER:', get_hand_value(dealer_hand))
        display_cards(dealer_hand)
    else:
        print('DEALER: ???')
        # Hide the dealer's first card:
        display_cards([BACKSIDE] + dealer_hand[1:])

    print('PLAYER:', get_hand_value(player_hand))
    display_cards(player_hand)

def get_hand_value(cards):
    value = 0
    number_of_aces = 0

    for card in cards:
        rank = card[0]  # card is a tuple like (rank, suit)
        if rank == 'A':
            number_of_aces += 1
        elif rank in ('K', 'Q', 'J'):  # Face cards are worth 10 points.
            value += 10
        else:
            value += int(rank)  # Numbered cards are worth their number.

    value += number_of_aces  # Add 1 per ace.
    for i in range(number_of_aces):
        if value + 10 <= 21:
            value += 10
    return value


def display_cards(cards):
    rows = ['', '', '', '', '']  # The text to display on each row.
    for i, card in enumerate(cards):
        rows[0] += ' ___  '  # Print the top line of the card.
        if card == BACKSIDE:
            rows[1] += '|## | '
            rows[2] += '|###| '
            rows[3] += '|_##| '
        else:
            rank, suit = card  # The card is a tuple data structure.
            rows[1] += '|{} | '.format(rank.ljust(2))
            rows[2] += '| {} | '.format(suit)
            rows[3] += '|_{}| '.format(rank.rjust(2, '_'))

    # Print each row on the screen:
    for row in rows:
        print(row)


def get_move(player_hand, money):
    while True:  
        moves = ['(H)it', '(S)tand']

        if len(player_hand) == 2 and money > 0:
            moves.append('(D)ouble down')

        # Get the player's move:
        move_prompt = ', '.join(moves) + '> '
        move = input(move_prompt).upper()
        if move in ('H', 'S'):
            return move  # Player has entered a valid move.
        if move == 'D' and '(D)ouble down' in moves:
            return move  # Player has entered a valid move.

main()
