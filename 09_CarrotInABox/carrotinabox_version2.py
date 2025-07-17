# Other implementation of the game carrot in a box
import random

def main():
    input("Press Enter to begin...")
    p1_name = input("Name Player1: ")
    p2_name = input("Name Player2: ")
    player_names = p1_name[:11].center(11) + "    " + p2_name[:11].center(11)
    print(player_names)

    print('''HERE ARE TWO BOXES:
          __________   __________
         /        /|  /         /|
        +---------+|  +---------+|
        |         || |          ||
        | BOX1    |/ | BOX2     |/
        +--------+/  +---------+/''')


    print(p2_name + " please close your eyes")
    input("Press Enter to begin...")

    print('\n' * 100)
    print(p1_name + ' here is the inside of your box:')
    if random.randint(1, 2) == 1:
        carrotInFirstBox = True
        print("\n \n You got the carrot :) \n \n")
    else:
        carrotInFirstBox = False
        print("\n \n You don't the carrot :( \n \n")

    input("Press Enter to begin...")
    print('\n' * 100)

    print(p2_name + ', do you want to swap boxes with ' + p1_name + '? y/n')
    while True:
        response = input('> ').upper()
        if not (response.startswith('Y') or response.startswith('N')):
            print("Invalid Input please Insert y or n");
        else:
            break


main()
