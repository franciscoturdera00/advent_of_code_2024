from enum import Enum

# text_file = "Day 4\\example_1.txt"
text_file = "day_4/part_1.txt"
TARGET = "MAS"

def main():
    with open(text_file) as f:
        lines = f.readlines()
        print(check_grid(lines))
    return

def is_out_of_bounds(x, y, grid, wiggle_room=1):
    return not (y >= 0 + wiggle_room and y < len(grid) - wiggle_room 
                and x >= 0 + wiggle_room and x < len(grid[y]) - wiggle_room)

def is_mas(word):
    return word == TARGET or word == TARGET[::-1]

def is_x_mas(grid, current_location):
    x, y = current_location
    if is_out_of_bounds(x,y, grid):
        return 0
    letter = grid[y][x]

    top_left = grid[y - 1][x - 1]
    bottom_right = grid[y + 1][x + 1]

    bottom_left = grid[y + 1][x - 1]
    top_right = grid[y - 1][x + 1]

    if is_mas(top_left + letter + bottom_right) and is_mas(bottom_left + letter + top_right):
        return 1
    return 0

def check_grid(grid):
    total = 0
    for y,_ in enumerate(grid):
        for x,_ in enumerate(grid[y]):
            if grid[y][x] == 'A':
                total += is_x_mas(grid, (x,y))
    return total

main()