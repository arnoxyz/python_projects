# Other implementation of BouncingLogo
# using module bext by Al Sweigart (https://github.com/asweigart/bext)
import bext, time, sys, random

def gen_logos(number, width, height, colors, directions):
    logos = []
    for i in range(number):
        logos.append({
            "color"     : random.choice(colors),
            "x"         : random.randint(0, width-1),
            "y"         : random.randint(0, height-1),
            "direction" : random.choice(directions)
        })
    return logos

def display_logo(logo):
    bext.goto(logo["x"], logo["y"])
    bext.fg(logo["color"])
    print("DVD", end="")
    bext.goto(0,0)
    sys.stdout.flush()

def move_logos(logos, width, height):
    for logo in logos:
        # Check Corners
        if logo["x"] <= 0 and logo["y"] <= 0:
            logo["direction"] = "dr"
        elif logo["x"] <= 0 and logo["y"] >= height-2:
            logo["direction"] = "ur"
        elif logo["x"] >= width-3 and logo["y"] <= 0:
            logo["direction"] = "dl"
        elif logo["x"] >= width-3 and logo["y"] >= height-2:
            logo["direction"] = "ul"

        # Check Edges before moving
        if logo["x"] <= 0 and logo["direction"] == "ul":
            logo["direction"] = "ur"
        elif logo["x"] <= 0 and logo["direction"] == "dl":
            logo["direction"] = "dr"
        elif logo["x"] >= width-3 and logo["direction"] == "ur":
            logo["direction"] = "ul"
        elif logo["x"] >= width-3 and logo["direction"] == "dr":
            logo["direction"] = "dl"

        elif logo["y"] <= 0 and logo["direction"] == "ul":
            logo["direction"] = "dl"
        elif logo["y"] <= 0 and logo["direction"] == "ur":
            logo["direction"] = "dr"
        elif logo["y"] >= height-1 and logo["direction"] == "dl":
            logo["direction"] = "ul"
        elif logo["y"] >= height-1 and logo["direction"] == "dr":
            logo["direction"] = "ur"

        # Move logos
        if logo["direction"] == "ur":
            logo["x"] += 1
            logo["y"] -= 1
        elif logo["direction"] == "ul":
            logo["x"] -= 1
            logo["y"] -= 1
        elif logo["direction"] == "dr":
            logo["x"] += 1
            logo["y"] += 1
        elif logo["direction"] == "dl":
            logo["x"] -= 1
            logo["y"] += 1
        display_logo(logo)



def main():
    bext.hide_cursor()
    pause = 0.01
    colors  = ['red', 'green', 'blue']
    number_of_logos = 10
    directions = ('ur', 'ul', 'dr', 'dl') #u=up, d=down, r=right, l=left
    width, height = bext.size()

    bext.clear()

    # gen logos
    logos = gen_logos(number_of_logos, width, height, colors, directions);

    # move logos
    while True:
        move_logos(logos, width, height)
        time.sleep(pause)


main()
