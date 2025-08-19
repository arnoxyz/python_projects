# Implementation of the game of life

ALIVE = "1"
DEAD  = "0"

def fill_grid(width, height):
    grid = {}
    for x in range(width):
        for y in range(height):
            #grid[(x, y)] = DEAD
            grid[(x, y)] = ALIVE
    return grid;

def print_grid(grid, width, height):
    for y in range(height):
        for x in range(width):
            print(grid[(x,y)], end="")
        print()

def check_grid(grid, width, height):
    actual_value = 0;

    for x in range(width):
        for y in range(width):
            current_cell = grid[(x,y)]
            alive_cells = 0

            #get cells around the actual_cell
            left_cell   = grid[(x - 1) % width, y]
            right_cell  = grid[(x + 1) % width, y]
            top_cell    = grid[x, (y - 1) % height]
            bottom_cell = grid[x, (y + 1) % height]

            if left_cell == ALIVE:
                alive_cells = alive_cells + 1;
            if right_cell == ALIVE:
                alive_cells = alive_cells + 1;
            if top_cell == ALIVE:
                alive_cells = alive_cells + 1;
            if bottom_cell == ALIVE:
                alive_cells = alive_cells + 1;
            print(alive_cells)
        print()

def main():
    width = 10
    height = 10

    grid = fill_grid(width, height)
    #print_grid(grid, width, height)
    check_grid(grid, width, height)

main()
