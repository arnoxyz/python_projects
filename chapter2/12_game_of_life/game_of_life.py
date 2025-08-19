# Implementation of the game of life
import copy

ALIVE = "1"
DEAD  = "0"

def fill_grid(width, height):
    grid = {}
    for x in range(width):
        for y in range(height):
            grid[(x, y)] = DEAD
            #grid[(x, y)] = ALIVE

    return grid;

def print_grid(grid, width, height):
    for y in range(height):
        for x in range(width):
            print(grid[(x,y)], end="")
        print()

def check_grid(grid, width, height):
    actual_value = 0;
    next_grid = copy.deepcopy(grid)

    for x in range(width):
        for y in range(height):
            current_cell = grid[(x,y)]
            alive_cells = 0

            #get neighbor cells (all cells around the actual_cell)
            left_cell   = grid[(x - 1) % width, y]
            right_cell  = grid[(x + 1) % width, y]
            top_cell    = grid[x, (y - 1) % height]
            bottom_cell = grid[x, (y + 1) % height]

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

    print_grid(next_grid, width, height)

def main():
    width = 10
    height = 10

    grid = fill_grid(width, height)
    #print_grid(grid, width, height)
    check_grid(grid, width, height)

main()
