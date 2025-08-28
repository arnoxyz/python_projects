import random, sys, time

def createCave(start):
    #one line is always 100 symbols
    middle = start
    left = (100-middle)//2
    right = left

    #one line is [left-part] [middle-part] [right-part]
    line = "*" * left + "-" * middle  +"*"* right;
    print(line, flush=True)


def main():
    start = random.randint(0, 100)
    while True:
        choice = random.randint(0,2)
        if choice == 0:
            start = start+5
        elif choice == 1:
            start = start-5

        if start <= 0:
            start = 10
        if start >= 100:
            start = 90

        createCave(start)
        time.sleep(0.05)


main()
