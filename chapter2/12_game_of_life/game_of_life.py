# Implementation of the game of life

def fill_grid(width, height):
    grid = {}
    ALIVE = "1"
    DEAD  = "0"
    for x in range(width):
        for y in range(height):
            grid[(x, y)] = DEAD
    return grid;

def print_grid(grid, width, height):
    for y in range(height):
        for x in range(width):
            print(grid[(x,y)], end="")
        print()

def main():
    width = 10
    height = 10

    print("Hello World!")
    grid = fill_grid(width, height)
    print_grid(grid,width, height)


main()
