import time
from copy import deepcopy


# text_file = "day_6/example.txt"
text_file = "day_6/part_1.txt"

OBSTRUCTION = "#"
OPEN_SPACE = "."
SEEN = "X"

def symbol_to_cardinal_dict():
        return {"<": (-1, 0), "^":(0,-1), ">":(1,0), "v":(0,1)}

def symbol_to_direction(directional_symbol):
    return {"<": LEFT, "^":UP, ">":RIGHT, "v":DOWN}[directional_symbol]

def rotate_90_deg(direction):
    neighbor = {"<": "^", "^":">", ">":"v", "v":"<"}
    return symbol_to_direction(neighbor[direction.directional_symbol])

class Direction():
 
    def __init__(self, directional_symbol):
        self.directional_symbol = directional_symbol
        self.cardinal_direction = symbol_to_cardinal_dict()[directional_symbol]
    
    def __eq__(self, other):
        if not hasattr(other, "directional_symbol"):
            return NotImplemented
        return self.directional_symbol == (Direction)(other).directional_symbol

    def __lt__(self, other):
        if not hasattr(other, "directional_symbol"):
            return NotImplemented
        return self.directional_symbol == (Direction)(other).directional_symbol
    
    def __repr__(self):
        return self.directional_symbol
        
LEFT = Direction("<")
UP = Direction("^")
RIGHT = Direction(">")
DOWN = Direction("v")

def main():
    with open(text_file) as f:
        lines = f.readlines()
        grid, guard_direction, guard_position = build_grid_and_find_guard(lines)

        starting_guard_position = deepcopy(guard_position)
        starting_guard_direction = deepcopy(guard_direction)

        if not point_in_bounds(grid, guard_position):
            return 0
        
        cont = True
        next_grid = grid
        while cont:
            next_grid, cont, guard_position, guard_direction = take_next_step(next_grid, guard_position, guard_direction)
            # Uncomment for terminal stepping output
            # print_nice_grid(next_grid)
        unsafe = count_unsafe(grid) # part 1
        return unsafe
        # return count_loop_possibilities(next_grid, starting_guard_position, starting_guard_direction) # part 2

def get_next_location(cardinal_direction, current_location):
    return tuple(map(lambda i,j: i + j, current_location, cardinal_direction))

def count_loop_possibilities(complete_path_grid, guard_position, guard_direction: Direction):
    loops = 0
    # Skips first step
    complete_path_grid, cont, guard_position, guard_direction = take_next_step(complete_path_grid, guard_position, guard_direction)
  
    # print_nice_grid(complete_path_grid)
    while cont:
        # print_nice_grid(complete_path_grid)
        if is_loop_possibility(complete_path_grid, guard_position, guard_direction):
            loops += 1
        complete_path_grid, cont, guard_position, guard_direction = take_next_step(complete_path_grid, guard_position, guard_direction)
    return loops
   

def is_loop_possibility(complete_path_grid, guard_starting_position, guard_starting_direction: Direction):
    forward_step_position = get_next_location(guard_starting_direction.cardinal_direction, guard_starting_position)
    if not point_in_bounds(complete_path_grid, forward_step_position):
        return False
    
    forward_step_symbol = complete_path_grid[forward_step_position[1]][forward_step_position[0]]
    if forward_step_symbol == OBSTRUCTION:
        return False

    test_grid = deepcopy(complete_path_grid)
    test_grid[guard_starting_position[1]][guard_starting_position[0]] = rotate_90_deg(guard_starting_direction).directional_symbol
    test_grid[forward_step_position[1]][forward_step_position[0]] = OBSTRUCTION

    current_position = deepcopy(guard_starting_position)
    current_direction = deepcopy(guard_starting_direction)
    return test_path_loop(test_grid, current_position, current_direction, guard_starting_position)

def test_path_loop(test_grid, current_position, current_direction, goal_position):
    test_grid, cont, current_position, current_direction = take_next_step(test_grid, current_position, current_direction)
    while cont:
        test_grid, cont, current_position, current_direction = take_next_step(test_grid, current_position, current_direction)
        if goal_position == current_position:
            return True
    return False


def count_unsafe(grid):
    unsafe = 0
    for row in grid:
        for positional_symbol in grid[row]:
            if not isinstance(positional_symbol, Direction):
                if positional_symbol == SEEN:
                    unsafe += 1 
    return unsafe
        

def build_grid_and_find_guard(input):
    grid = dict()
    guard_direction = None
    guard_location = (0,0)
    for y_index in range(len(input)):
        for x_index, x_symbol in enumerate(input[y_index]):
            if x_symbol == "\n":
                continue
            if is_guard(x_symbol):
                guard_direction = get_guard_direction(x_symbol)
                guard_location = (x_index, y_index)
            grid[y_index] = grid.get(y_index, list()) + [x_symbol]
    return grid, guard_direction, guard_location


def take_next_step(grid, guard_location: tuple, guard_direction: Direction):
    cardinal_dir = guard_direction.cardinal_direction
    next_location = tuple(map(lambda i,j: i + j, guard_location, cardinal_dir))
    if not point_in_bounds(grid, next_location):
        grid[guard_location[1]][guard_location[0]] = SEEN
        return grid, False, guard_location, guard_direction
    
    symbol_ahead = grid[next_location[1]][next_location[0]]

    if symbol_ahead == OBSTRUCTION:  
        # Rotate 90 degrees and try again
        new_guard_direction = rotate_90_deg(guard_direction)
        grid[guard_location[1]][guard_location[0]] = new_guard_direction.directional_symbol
        return take_next_step(grid, guard_location, new_guard_direction)
    
    # Path is clear, move in the new direction
    grid[guard_location[1]][guard_location[0]] = SEEN
    grid[next_location[1]][next_location[0]] = guard_direction
    # print_nice_grid(grid)
    # print()
    return grid, True, next_location, guard_direction
        
def point_in_bounds(grid, point):
    for p in point:
        if p < 0 or p >= len(grid):
            return False
    return True

def is_guard(symbol):
    return symbol in symbol_to_cardinal_dict()

def get_guard_direction(symbol):
    return Direction(symbol)


def print_nice_grid(grid, guard_position=(-1,-1), guard_direction=None, timer=None):
    for y,_ in enumerate(grid):
        for x,_ in enumerate(grid[y]):
            if (x,y) == guard_position:
                print(guard_direction,end="")
            else:
                print(grid[y][x], end="")
            # if timer is not None:
            #     time.sleep(timer)
        print()
    print()

print(main())