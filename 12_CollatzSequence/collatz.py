# Generation of the collatz sequence
import math

def get_user_input():
    while True:
        number = input("Insert start integer > ")
        if number.isdigit():
            return int(number)

def generate_collatz_sequence(number, idx):
    print(number, end=" ")

    if idx != 1:
        if (number % 2) == 0:
            generate_collatz_sequence(int(number/2), idx-1)
        else:
            generate_collatz_sequence(3*number+1, idx-1)

def main():
    #number = get_user_input()
    number = 20
    generate_collatz_sequence(number, 100)


main()
