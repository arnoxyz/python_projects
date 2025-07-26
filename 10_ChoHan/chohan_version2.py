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

def main():
    money = 5000
    pot = 0

    pot = place_bet(money)

    print("Hello World!")



main()
