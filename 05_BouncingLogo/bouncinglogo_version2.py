# Other implementation of BouncingLogo 
# using module bext by Al Sweigart (https://github.com/asweigart/bext)
import bext, time, sys, random

def gen_logos(number, width, height, colors, directions): 
    logos = []
    for i in range(number):
        logos.append({
            "color"     : random.choice(colors), 
            "x"         : random.randint(1, width - 4),
            "y"         : random.randint(1, height - 4),
            "direction" : random.choice(directions)
        })
    return logos

def display_logo(logo):
    bext.goto(logo["x"], logo["y"])
    bext.fg(logo["color"])
    print("DVD", end="")
    bext.goto(0,0)
    sys.stdout.flush()

def move_logos(logos):
    for logo in logos:
        display_logo(logo)


def main(): 
    pause = 0.2
    colors  = ['red', 'green', 'blue']
    number_of_logos = 5
    directions = ('ur', 'ul', 'dr', 'dl') #u=up, d=down, r=right, l=left
    width, height = bext.size()

    bext.clear()

    # gen logos
    logos = gen_logos(number_of_logos, width, height, colors, directions);

    # move logos
    move_logos(logos)

main()
