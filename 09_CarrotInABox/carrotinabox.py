# Implementaion of a two player game called: Apple In a Box

def draw_boxes():
    box = ""
    top    =     "+--------+  +--------+"
    empty_line = "|        |  |        |"
    middle =     "|  BOX1  |  |  BOX2  |"
    bottom =     "+--------+  +--------+"

    box += top + "\n"
    box += empty_line + "\n"
    box += middle + "\n"
    box += empty_line + "\n"
    box += bottom + "\n"

    print(box)

def draw_open_box1():
    box = ""
    top    =     "+        +  +--------+"
    empty_line = "|        |  |        |"
    middle =     "|  BOX1  |  |  BOX2  |"
    bottom =     "+--------+  +--------+"

    box += top + "\n"
    box += empty_line + "\n"
    box += middle + "\n"
    box += empty_line + "\n"
    box += bottom + "\n"
    print(box)

def draw_open_boxes1():
    box = ""
    top    =     "+ (---)  +  +        +"
    empty_line = "|        |  |        |"
    middle =     "|  BOX1  |  |  BOX2  |"
    bottom =     "+--------+  +--------+"

    box += top + "\n"
    box += empty_line + "\n"
    box += middle + "\n"
    box += empty_line + "\n"
    box += bottom + "\n"
    print(box)

def draw_open_boxes2():
    box = ""
    top    =     "+        +  +  (---) +"
    empty_line = "|        |  |        |"
    middle =     "|  BOX1  |  |  BOX2  |"
    bottom =     "+--------+  +--------+"

    box += top + "\n"
    box += empty_line + "\n"
    box += middle + "\n"
    box += empty_line + "\n"
    box += bottom + "\n"
    print(box)


def main():
    print("Welcome to Apple in a Box!")
    draw_boxes()

    draw_open_boxes1()
    draw_open_boxes2()

main()
