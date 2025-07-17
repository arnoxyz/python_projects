# Other implementation of the game carrot in a box
import random

def get_names(players):
    input("Press Enter to begin...")
    players["player1_name"] = input("Name Player1: ")
    players["player2_name"] = input("Name Player2: ")
    return players;


    return players



def main():
    players = {
            "player1_name" : "Player 1",
            "player2_name" : "Player 2"
    }

    players = get_names(players);
    print(players)



main()
