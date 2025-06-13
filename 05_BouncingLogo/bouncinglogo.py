# Implementation of BouncingLogo 

# using module bext by Al Sweigart (https://github.com/asweigart/bext)
import bext, random

def main():
    width, height = bext.size() #return current terminal size 
    bext.fg('black') #text-color
    bext.bg('white') 
    bext.clear()

main()
