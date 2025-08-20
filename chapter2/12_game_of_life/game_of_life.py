# Implementation of the game of life
import copy, random

# Always generated a SIZE times SIZE Grid
SIZE = 10

# Symbol to use to display alive and dead cells
ALIVE = "1"
DEAD  = "0"

def fill_grid_random():
    grid = {}
    for x in range(SIZE):
        for y in range(SIZE):
            if random.randint(0, 1) == 0:
                grid[(x, y)] = ALIVE
            else:
                grid[(x, y)] = DEAD

    return grid

def fill_grid():
    grid = {}
    for x in range(SIZE):
        for y in range(SIZE):
            grid[(x, y)] = DEAD

    # check the two rules
    #(x,y)
    grid[1,1] = ALIVE
    grid[2,2] = ALIVE
    grid[0,2] = ALIVE

    grid[3,5] = ALIVE
    grid[4,4] = ALIVE
    grid[4,5] = ALIVE
    return grid

def print_grid(grid):
    for y in range(SIZE):
        for x in range(SIZE):
            print(grid[(x,y)], end="")
        print()

def check_grid(grid):
    actual_value = 0;
    next_grid = copy.deepcopy(grid)

    for x in range(SIZE):
        for y in range(SIZE):
            current_cell = grid[(x,y)]
            alive_cells = 0

            #get neighbor cells (all cells around the actual_cell)
            left_cell   = grid[(x - 1) % SIZE, y]
            right_cell  = grid[(x + 1) % SIZE, y]
            top_cell    = grid[x, (y - 1) % SIZE]
            bottom_cell = grid[x, (y + 1) % SIZE]

            #count all neighbors that are alive
            if left_cell == ALIVE:
                alive_cells = alive_cells + 1;
            if right_cell == ALIVE:
                alive_cells = alive_cells + 1;
            if top_cell == ALIVE:
                alive_cells = alive_cells + 1;
            if bottom_cell == ALIVE:
                alive_cells = alive_cells + 1;

            #apply rule
            if current_cell == ALIVE and (alive_cells == 2 or alive_cells == 3):
                #current Cell stays Alive
                next_grid[(x,y)] = ALIVE
            elif current_cell == DEAD and (alive_cells == 3):
                #current Cell becomes Alive
                next_grid[(x,y)] = ALIVE
            else:
                next_grid[(x,y)] = DEAD

    return next_grid

def main():
    grid = fill_grid_random()
    print_grid(grid)

    while True:
        grid = check_grid(grid)

        input_str =  input("Press enter to display the next generation or (q)uit > ").lower()
        if "quit" in input_str or "q" in input_str:
            break

        print("\n"*10)
        print_grid(grid)

main()
