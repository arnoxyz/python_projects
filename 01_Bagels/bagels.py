# Implementation of the game bagels:

# Implementation details:
# user input as integer
# divid/modulo operation used to get the digits
# logic with boolean flags used to calculate the game logic

import random

def game(win_first_digit, win_second_digit, win_third_digit):
    # Prompt user
    print("Insert a 3 digit number: \n")
    # Read input and convert Input from user 
    input_val = int(input())
    #Check and output (pico, fermi, bagels)
        # get the 3 values
    first_digit = input_val//100;
    second_digit = (input_val//10)%10;
    third_digit = input_val%10;
        #flag for bagels
    bagels_fg = True
    pico1_fg = False
    pico2_fg = False
    pico3_fg = False

    #check for pico (position, value correct)
    if win_first_digit == first_digit:
        print("pico (correct value, correct position)", end="")
        pico1_fg = True
        bagels_fg = False
    # check for fermi (value correct, position wrong)
    elif (win_first_digit == second_digit or
          win_first_digit == third_digit):
        print("fermi (correct value, wrong position)", end="")
        bagels_fg = False
    if win_second_digit == second_digit:
        print("pico (correct value, correct position)", end="")
        bagels_fg = False
        pico2_fg = True
    elif (win_second_digit == first_digit or 
          win_second_digit == third_digit):
        print("fermi (correct value, wrong position)", end="")
        bagels_fg = False

    if win_third_digit == third_digit:
        print("pico (correct value, correct position)", end="")
        bagels_fg = False
        pico3_fg = True
    elif (win_third_digit == first_digit or 
          win_third_digit == second_digit):
        print("fermi (correct value, wrong position)", end="")
        bagels_fg = False 
    print("")

    #check for bagels (all wrong)
    if bagels_fg == True:
        print("bagels (nothing right here)")

    #return if the player has guessed the right value
    if (pico1_fg == True and 
        pico2_fg == True and 
        pico3_fg == True):
        return True
    else: 
        return False
        

# Start Program: 
print("Welcome to the bagels game, try to guess a 3 digit number \n")
print("\t Pico  = 1 digit is correct (right position)")
print("\t Fermi = 1 digit is correct (wrong position)")
print("\t Bagels= no digit is correct")

# play 10 rounds
user_score = 1000

# Gen Solution
number = random.randint(100, 999)
win_val = number
win_first_digit = number//100
win_second_digit = (number//10)%10
win_third_digit = number%10

while user_score != 0: 
    game_result = game(win_first_digit, win_second_digit, win_third_digit)
    if game_result == True:
        print("Win, your score is = " + str(user_score))
        break;
    else:
        user_score = user_score - 100;

print("You lost")
