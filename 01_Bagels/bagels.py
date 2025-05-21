def help():
    print("\t Pico  = 1 digit is correct (right position)")
    print("\t Fermi = 1 digit is correct (wrong position)")
    print("\t Bagels= no digit is correct")

def game():
    # Prompt user
    print("Insert a 3 digit number: \n")
    # Read input and convert Input from user 
    input_val = input()
    # TODO: Check and output (pico, fermi, bagels)
    # TODO: Check if input is "-h" and print helper
    print(input_val)

# Start Program: 
print("Welcome to the bagels game, try to guess a 3 digit number \n")
print("Here are some helpful informations: (you can always print them by inserting -h)")
help()

# play 10 rounds
game()



