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

def draw_open_boxes1():
    box = ""
    names  =     "-PLAYER 1-  -PLAYER 2-"
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

def draw_open_boxes2():
    box = ""
    names  =     "-PLAYER 1-  -PLAYER 2-"
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
                "player1 got apple" : True if random_bit() == 1 else False
    }

    if (config["player1 got apple"]):
        draw_open_boxes1()
    else:
        draw_open_boxes2()

main()
