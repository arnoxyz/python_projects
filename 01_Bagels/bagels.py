# TODO: generate a random 3 digit variable
win_val = 123; # fixed value for implementing and testing
win_first_digit = 1;
win_second_digit = 2;
win_third_digit = 3;

def game():
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

    #check for pico (position, value correct)
    if win_first_digit == first_digit:
        print("pico ", end="")
        bagels_fg = False
    # check for fermi (value correct, position wrong)
    elif (win_first_digit == second_digit or
          win_first_digit == third_digit):
        print("fermi ", end="")
        bagels_fg = False
    if win_second_digit == second_digit:
        print("pico ", end="")
        bagels_fg = False
    elif (win_second_digit == first_digit or 
          win_second_digit == third_digit):
        print("fermi ", end="")
        bagels_fg = False

    if win_third_digit == third_digit:
        print("pico ", end="")
        bagels_fg = False
    elif (win_third_digit == first_digit or 
          win_third_digit == second_digit):
        print("fermi ", end="")
        bagels_fg = False 

    #check for bagels (all wrong)
    if bagels_fg == True:
        print("bagels")

# Start Program: 
print("Welcome to the bagels game, try to guess a 3 digit number \n")
print("\t Pico  = 1 digit is correct (right position)")
print("\t Fermi = 1 digit is correct (wrong position)")
print("\t Bagels= no digit is correct")

# play 10 rounds
game()



