from enum import Enum

# text_file = "Day 4\\example_1.txt"
text_file = "day_4/part_1.txt"
TARGET = "XMAS"

def main():
    with open(text_file) as f:
        lines = f.readlines()
        print(sum_target_appearances(lines))
    return

def is_target(word, target=TARGET):
    return word == target

def target_correct_so_far(word, target=TARGET):
    return target.startswith(word)

def is_out_of_bounds(x, y, grid):
    return not (y >= 0 and y < len(grid) and x >= 0 and x < len(grid[y]))

def omnidirectional_target_count(current_location, grid):
    letter = grid[current_location[1]][current_location[0]]
    if not target_correct_so_far(letter):
        return 0
    total = 0
    for dir in Direction:
        total += check_current_direction(current_location, grid, dir)
    return total
    
def sum_target_appearances(grid):
    total = 0
    for y,_ in enumerate(grid):
        for x,_ in enumerate(grid[y]):
            total += omnidirectional_target_count((x,y), grid)
    return total

class Direction(Enum):
    LEFT=1
    UPLEFT=2
    DOWNLEFT=3
    UP=4
    DOWN=5
    RIGHT=6
    UPRIGHT=7
    DOWNRIGHT=8

    
def check_current_direction(current_location, grid, direction, word_so_far=""):
    x, y = current_location
    if is_out_of_bounds(x, y, grid):
        return 0
    word = word_so_far + grid[y][x]
    if is_target(word):
        return 1
    if not target_correct_so_far(word):
        return 0
    if direction == Direction.LEFT:
        return check_current_direction((x - 1, y), grid, direction, word)
    if direction == Direction.UPLEFT:
        return check_current_direction((x - 1, y - 1), grid, direction, word)
    if direction == Direction.DOWNLEFT:
        return check_current_direction((x - 1, y + 1), grid, direction, word)
    if direction == Direction.UP:
        return check_current_direction((x, y - 1), grid, direction, word)
    if direction == Direction.DOWN:
        return check_current_direction((x, y + 1), grid, direction, word)
    if direction == Direction.UPRIGHT:
        return check_current_direction((x + 1, y - 1), grid, direction, word)
    if direction == Direction.RIGHT:
        return check_current_direction((x + 1, y), grid, direction, word)
    if direction == Direction.DOWNRIGHT:
        return check_current_direction((x + 1, y + 1), grid, direction, word)
    

main()