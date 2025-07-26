# Another Implementaion of cho/han
import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN', 4: 'SHI', 5: 'GO', 6: 'ROKU'}

def place_bet(money):
    print("You have ", money, " money. How much do you bet? (or stop)")
    while True:
        pot = input("> ")
        if pot.upper() == 'STOP':
            print("Thanks for playing!")
            sys.exit()
        elif not pot.isdecimal():
            print("Please enter a number.")
        elif int(pot) > money:
            print("You do not have enough to make that bet.")
        else:
            pot = int(pot)
            return pot

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    return dice1+dice2;


def main():
    money = 5000
    pot = 0
    dice_sum = 0

    pot = place_bet(money)

    print("The dealer takes the dice and puts them into a cup. Then he swirls the cup and you hear the rattle of dice.  The dealer slams the cup on the floor, still covering the dice and asks for your bet. Insert CHO (for even) or HAN (for odd) dice sum?")
    dice_sum = roll_dice()


main()
