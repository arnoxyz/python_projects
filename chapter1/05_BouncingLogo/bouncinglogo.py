# Implementation of BouncingLogo 
# using module bext by Al Sweigart (https://github.com/asweigart/bext)
import bext, time, sys, random

def draw(text):
    print("BALL", end="")
    sys.stdout.flush()
    time.sleep(0.1)

def main():
    bext.clear()
    bext.hide_cursor()
    bext.fg('black') 
    bext.bg('white') 
    text = "A" 
    width, height = bext.size() #return current terminal size 

    # Init Move:
    move_right = False
    move_left = False
    move_down = False
    move_up = False

    # Coordinate: (x,y) 
    x = 0
    y = 0

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

    x = random.randint(0, 10000) % width-1;
    y = random.randint(0, 10000) % height-1;

    choice = random.randint(0, 10000) % 4
    if choice == 0:
        move_right = True
        move_down = True
    elif choice == 1:
        move_right = True
        move_up = True
    elif choice == 2:
        move_left = True
        move_up = True
    elif choice == 3:
        move_left = True
        move_down = True

    while True: 
        bext.clear();
        bext.goto(x,y)


        # Movements
        if move_right:
            if x < width-1:
                x = x+1
            else:
                move_right = False
                move_left = True
        if move_left:
            if x > 0:
                x = x-1
            else:
                move_right = True
                move_left = False
        if move_down:
            if y < height-1:
                y = y+1
            else:
                move_down = False
                move_up = True
        if move_up:
            if y > 0:
                y = y-1
            else:
                move_down = True
                move_up = False

        draw(text)


main()
