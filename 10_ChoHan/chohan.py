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

def main():
    # show empty dice
    draw_dice("empty", "empty")

    # gen two numbers
    dice1 = throw_dice()
    dice2 = throw_dice()

    # show solution
    draw_dice(dice1, dice2)

main()
