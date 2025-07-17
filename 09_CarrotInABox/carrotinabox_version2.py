# Other implementation of the game carrot in a box
import random

def get_names(players):
    input("Press Enter to begin...")
    players["player1_name"] = input("Name Player1: ")
    players["player2_name"] = input("Name Player2: ")
    return players

def draw_boxes(draw, players):
    # only draw winning box (that with the item inside)
    box = ""
    box     += "╔══════╗ \n"
    box     += "║--WIN-║ \n"
    box     += "╚══════╝ \n"

    if draw=="init":
        print(box)

    if draw=="player1 won":
        print(box)
        print(players["player1_name"])

    if draw=="player2 won":
        print(box)
        print(players["player2_name"])



def main():

    players = {
            "player1_name" : "Player 1",
            "player2_name" : "Player 2"
    }

    players = get_names(players);
    print(players)

    draw_boxes("init", players);


main()
