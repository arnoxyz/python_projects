# Other implementation of the game carrot in a box

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

main()
