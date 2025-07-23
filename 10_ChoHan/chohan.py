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
    house_betting_cost = 5

    while True:
        user_input = input("How much do you want to bet? > ")
        if user_input.isdigit():
            if player_config["credit"] >= int(user_input):
                player_config["credit"] = player_config["credit"] - (int(user_input) + house_betting_cost)
                player_config["bet"] = int(user_input)
                break
            else:
                print("Invalid Input to big bet for current credit!")
        else:
            print("Invlaid input insert a valid number")

def game(player_config):
    while player_config["credit"] > 0:
        user_input = input("play another round of cho/han? (y)es/(n)o > ").lower()
        if not (user_input.startswith("y")):
            break

        # show empty dice
        draw_dice("empty", "empty")

        # gen two numbers
        dice1 = throw_dice()
        dice2 = throw_dice()
        dice_sum = dice1+dice2

        # betting
        set_player_bet(player_config)
        set_player_decision(player_config)

        # show solution
        draw_dice(dice1, dice2)

        # win or lose
        if (dice_sum % 2) == 0:
            print("sum is even")
            if(player_config["decision"] == "e"):
                player_config["credit"] = player_config["credit"] + player_config["bet"]*2
                print("You won! Your credit is now: " + str(player_config["credit"]))
        else:
            print("sum is odd")
            if(player_config["decision"] == "o"):
                player_config["credit"] = player_config["credit"] + player_config["bet"]*2
                print("You won! Your credit is now: " + str(player_config["credit"]))

def main():
    player_config = {
        "credit" : 100,
        "bet" : 0,
        "decision" : ""
    }

    game(player_config)
    print("Thanks for playing your final score is: " + str(player_config["credit"]))

main()
