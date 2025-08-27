import random, sys


def createCave():
    #one line is always 100 symbols

    #one line is [left-part] [middle-part] [right-part]
    middle = 60

    left = (100-middle)//2
    right = left

    line = "*" * left + "-" * middle  +"*"* right;
    print(line)



def main():
    print("Hello World!")
    createCave()


main()
