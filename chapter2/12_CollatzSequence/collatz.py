# Generation of the collatz sequence
import math

def get_user_input():
    while True:
        number = input("Insert start integer > ")
        if number.isdigit():
            return int(number)

def generate_collatz_sequence(number, seen=None):
    print(number, end=" ")

    if seen is None:
        seen = set()

    seen.add(number)

    if {4, 2, 1}.issubset(seen):
        return

    if (number % 2) == 0:
        generate_collatz_sequence(number//2, seen)
    else:
        generate_collatz_sequence(3*number+1, seen)

def gen_first_10k():
    for idx in range(1, 10000):
        print()
        generate_collatz_sequence(idx)
        print()

def main():
    number = get_user_input()
    generate_collatz_sequence(number)

    #gen_first_10k()


main()
