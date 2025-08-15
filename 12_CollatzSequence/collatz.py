# Generation of the collatz sequence
import math

def get_user_input():
    while True:
        number = input("Insert start integer > ")
        if number.isdigit():
            return int(number)

def generate_collatz_sequence(number):
    if (number % 2) == 0:
        return int(number/2)
    else:
        return 3*number+1

def main():
    #number = get_user_input()
    number = 20
    print(generate_collatz_sequence(number))


main()
