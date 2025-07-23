# Implementaion of a dice gambling game
import random

def throw_dice():
    return random.randint(1, 6)

def draw_dice(face1, face2):
    dice_faces = {
        "empty": [
            "+-------+",
            "|       |",
            "|       |",
            "|       |",
            "+-------+"
        ],
        1: [
            "+-------+",
            "|       |",
            "|   o   |",
            "|       |",
            "+-------+"
        ],
        2: [
            "+-------+",
            "| o     |",
            "|       |",
            "|     o |",
            "+-------+"
        ],
        3: [
            "+-------+",
            "| o     |",
            "|   o   |",
            "|     o |",
            "+-------+"
        ],
        4: [
            "+-------+",
            "| o   o |",
            "|       |",
            "| o   o |",
            "+-------+"
        ],
        5: [
            "+-------+",
            "| o   o |",
            "|   o   |",
            "| o   o |",
            "+-------+"
        ],
        6: [
            "+-------+",
            "| o   o |",
            "| o   o |",
            "| o   o |",
            "+-------+"
        ]
    }

    # Get the lines of each die
    die1 = dice_faces[face1]
    die2 = dice_faces[face2]

    for line1, line2 in zip(die1, die2):
        print(f"{line1}   {line2}")

def set_player_decision(player_config):
    while True:
        user_input = input("Is the sum of the dice (E)ven or (O)dd? > ").lower()
        if user_input.startswith("e"):
            player_config["decision"] = "e"
            break
        elif user_input.startswith("o"):
            player_config["decision"] = "o"
            break
        else:
            print("Invlaid input insert: e or o");


def set_player_bet(player_config):
    print("Your credit is " + str(player_config["credit"]))

    while True:
        user_input = input("How much do you want to bet? > ")
        if user_input.isdigit():
            if player_config["credit"] >= int(user_input):
                player_config["credit"] = player_config["credit"] - int(user_input)
                player_config["bet"] = int(user_input)
                break
            else:
                print("Invalid Input to big bet for current credit!")
        else:
            print("Invlaid input insert a valid number")

def game():
    # show empty dice
    draw_dice("empty", "empty")

    # gen two numbers
    dice1 = throw_dice()
    dice2 = throw_dice()

    # betting

    # show solution
    draw_dice(dice1, dice2)

    # win or lose

def main():
    player_config = {
        "credit" : 100,
        "bet" : 0,
        "decision" : ""
    }

    set_player_bet(player_config)
    set_player_decision(player_config)

    print(player_config)

main()
