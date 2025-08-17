# Other implementation of the game carrot in a box
import random

def get_names(players):
    players["player1_name"] = input("Insert Player1 Name > ")
    players["player2_name"] = input("Insert Player2 Name > ")
    players["player1_has_carrot"] = True if random.randint(1, 2) == 1 else False
    return players

def draw_boxes(players, draw):
    # only draw winning box (that with the item inside)
    box = ""
    box     += "╔══════╗ \n"
    box     += "║--WIN-║ \n"
    box     += "╚══════╝ \n"

    if draw=="init":
        print("this is the box with the present inside \n")
        print(box)
    else:
        if players["player1_has_carrot"]:
            print(box)
            print(players["player1_name"])
        else:
            print(box)
            print(players["player2_name"])

def start_game(players):
    print(players["player2_name"] + " please close your eyes")
    input("Press Enter to begin...")

    print('\n' * 100)
    print(players["player1_name"] + ' here is the inside of your box:')

    if players["player1_has_carrot"]:
        print("\n \n You got the carrot :) \n \n")
    else:
        print("\n \n You don't got the carrot :( \n \n")

    input("Press Enter to cont...")
    print('\n' * 100)

    #player 2 swap input
    print(players["player2_name"] + ', do you want to swap boxes with ' + players["player2_name"] + '? y/n')
    while True:
        response = input('> ').upper()
        if not (response.startswith('Y') or response.startswith('N')):
            print("Invalid Input please Insert y or n");
        else:
            if response.startswith('Y'):
                players["player1_has_carrot"] = not players["player1_has_carrot"]; #toggle box
            break

    print('\n' * 100)

    #show winner
    draw_boxes(players, "")

def main():

    players = {
            "player1_name" : "Player 1",
            "player2_name" : "Player 2",
            "player1_has_carrot" : True
    }

    players = get_names(players)
    draw_boxes(players, "init")
    start_game(players)


main()
