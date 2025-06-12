# Implementation of BouncingLogo 

# using module bext by Al Sweigart (https://github.com/asweigart/bext)
import bext, random

# demo of bext
def demo():
    width, height = bext.size()

    try:
        while True:
            bext.fg('random')
            bext.bg('random')
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)

            if x == width -1 and y == height - 1:
                continue 
            bext.goto(x, y)
            print('*', end='')
    except KeyboardInterrupt:
        pass

demo()
