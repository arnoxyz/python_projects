# Implementation of BouncingLogo 
# using module bext by Al Sweigart (https://github.com/asweigart/bext)
#import bext

# move x-pos
def move_x_pos(pos):
    pos["x"] += 1
    #bext.goto(pos["x"],pos["y"])

# move y-pos
def move_y_pos(pos):
    pos["y"] += 1
    #bext.goto(pos["x"],pos["y"])

def display(text):
    #bext.clear()
    print(text)

def main():
    text = "TEXT"
    pos = {"x" : 0, "y" : 0}
    print(pos)
    move_x_pos(pos)
    print(pos)
    move_y_pos(pos)
    print(pos)


def bext_stuff():
    width, height = bext.size() #return current terminal size 
    bext.fg('black') #text-color
    bext.bg('white') 
    bext.clear()
    move_x_pos(pos)
    move_y_pos(pos)
    print(pos, end="")
    display(text)

main()
