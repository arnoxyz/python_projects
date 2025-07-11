# Implementaion of a two player game called: Carrot In a Box

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

def main():
    print("Welcome to Carrot in a Box!")
    draw_boxes()

main()
