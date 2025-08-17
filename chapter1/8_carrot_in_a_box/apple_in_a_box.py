# Implementaion of a two player game called: Apple In a Box
import random

def random_bit():
    return random.randint(0, 1)

def draw_boxes():
    box = ""
    names  =     "-PLAYER 1-  -PLAYER 2-"
    top    =     "+--------+  +--------+"
    empty_line = "|        |  |        |"
    middle =     "|  BOX1  |  |  BOX2  |"
    bottom =     "+--------+  +--------+"

    box += names+ "\n"
    box += top + "\n"
    box += empty_line + "\n"
    box += middle + "\n"
    box += empty_line + "\n"
    box += bottom + "\n"

    print(box)

def draw_open_boxes1(config):
    box = ""
    if (config["default"]):
        names  =     "-PLAYER 1-  -PLAYER 2-"
    else:
        names  =     "-PLAYER 2-  -PLAYER 1-"
    empty =      "                      "
    top    =     "  (---)               "
    empty_line = "|        |  |        |"
    middle =     "|  BOX1  |  |  BOX2  |"
    bottom =     "+--------+  +--------+"

    box += names + "\n"
    box += empty + "\n"
    box += top + "\n"
    box += empty_line + "\n"
    box += middle + "\n"
    box += empty_line + "\n"
    box += bottom + "\n"
    print(box)

def draw_open_boxes2(config):
    box = ""
    if (config["default"]):
        names  =     "-PLAYER 1-  -PLAYER 2-"
    else:
        names  =     "-PLAYER 2-  -PLAYER 1-"

    empty =      "                      "
    top    =     "               (---)  "
    empty_line = "|        |  |        |"
    middle =     "|  BOX1  |  |  BOX2  |"
    bottom =     "+--------+  +--------+"

    box += names + "\n"
    box += empty + "\n"
    box += top + "\n"
    box += empty_line + "\n"
    box += middle + "\n"
    box += empty_line + "\n"
    box += bottom + "\n"
    print(box)


def main():
    print("Welcome to Apple in a Box!")
    draw_boxes()

    config = {
                "player1 got apple" : True if random_bit() == 1 else False,
                "default" : True
    }

    input("Player 2 please close your eyes... (Press Enter to Continue)")

    if (config["player1 got apple"]):
        draw_open_boxes1(config)
        print("Player 1 at the moment you got the apple with box1")
    else:
        draw_open_boxes2(config)
        print("Player 1 at the moment you got the box with no apple")


    input("Player 1 if you are done ... (Press Enter to Continue)")
    print("\n" * 100);

    draw_boxes()
    player2_choice = input("Player 2 can decide now to switch the boxes or not -> Switch Boxes? (y/n): ")
    if 'y' in player2_choice.lower():
        config["default"] = False
        config["player1 got apple"] = not config["player1 got apple"]

    if (config["player1 got apple"]):
        draw_open_boxes1(config)
        print("Player 1 Won")
    else:
        draw_open_boxes2(config)
        print("Player 2 Won")

main()
