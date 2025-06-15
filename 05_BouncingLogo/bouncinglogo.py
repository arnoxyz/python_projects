# Implementation of BouncingLogo 
# using module bext by Al Sweigart (https://github.com/asweigart/bext)
import bext, time, sys


def main():
    bext.clear()
    bext.fg('black') 
    bext.bg('white') 
    text = "A" 
    width, height = bext.size() #return current terminal size 

    # Coordinate: (x,y) 
    x = 0;
    y = 0;

    # Window: 
    # (0,0) --------------------------------- (Width-1, 0)
    # (0,1) --------------------------------- (Width-1, 1)
    # (0,2) --------------------------------- (Width-1, 2)
    # ...
    # ...
    # (0,Height-3) -------------------------- (Width-1, Height-3)
    # (0,Height-2) -------------------------- (Width-1, Height-2)
    # (0,Height-1) -------------------------- (Width-1, Height-1)
    
    # Corners:
    left_up = (0,0)
    right_up = (width-1,0)
    right_down = (width-1,height-1)
    left_down = (0,height-1)

    while True: 
        bext.clear();
        bext.goto(x,y)

        if x < width-1: 
            x = x+1
        print(text, end="")
        sys.stdout.flush()
        time.sleep(0.5)

main()
