import time
from copy import deepcopy
from typing import Dict, List
from Direction import Direction
from Space import Space


# text_file = "day_6/example.txt"
text_file = "day_6/part_1.txt"
# text_file = 'day_6/temp.txt'


def rotate_90_deg(direction):
    neighbor = {"<": "^", "^":">", ">":"v", "v":"<"}
    return Direction(neighbor[direction.directional_symbol])

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
        tick = 0
        while cont:
            next_grid, cont, guard_position, guard_direction = take_next_step(next_grid, guard_position, guard_direction, tick)
            tick += 1
            
        unsafe = count_unsafe(grid) # part 1
        return unsafe
        return count_loop_possibilities(next_grid, starting_guard_position, starting_guard_direction) # part 2

def get_next_location(cardinal_direction, current_location):
    return tuple(map(lambda i,j: i + j, current_location, cardinal_direction))

def count_loop_possibilities(complete_path_grid: Dict[int,List[Space]], guard_position, guard_direction: Direction):
    loops = 0
    tick = 0
    cont = True
    print_it = False
    complete_path_grid[guard_position[1]][guard_position[0]].become_guard(guard_direction.directional_symbol)
    while cont:
        if tick == 1021:
            print_it = True
        if print_it:
            print_nice_grid(complete_path_grid)
            print(guard_position, tick, loops)

        complete_path_grid, cont, guard_position, guard_direction = take_next_step(complete_path_grid, guard_position, guard_direction)
        # print_nice_grid(complete_path_grid)
        tick += 1
        if is_loop_possibility(complete_path_grid, guard_position, guard_direction, tick):
            loops += 1
    return loops


def is_loop_possibility(complete_path_grid: Dict[int,List[Space]], guard_starting_position, guard_starting_direction: Direction, tick):
    # Work in progress
    forward_step_position = get_next_location(guard_starting_direction.cardinal_direction, guard_starting_position)
    if not point_in_bounds(complete_path_grid, forward_step_position):
        return False
    forward_step_space = complete_path_grid[forward_step_position[1]][forward_step_position[0]]
    if forward_step_space.is_obstruction():
        return False
    
    quarter_turn_direction = rotate_90_deg(guard_starting_direction)
    right_step_position = get_next_location(quarter_turn_direction.cardinal_direction, guard_starting_position)
    right_step_space = complete_path_grid[right_step_position[1]][right_step_position[0]]

    is_loop = False
    if right_step_space.is_seen():
        history = right_step_space.get_history()
        for symbol, seen_tick  in history:
            is_loop = symbol == quarter_turn_direction.directional_symbol and tick > seen_tick
            if is_loop:
                break
        if not is_loop:
            is_loop = test_path_loop(complete_path_grid, forward_step_position, guard_starting_position, guard_starting_direction)
    return is_loop

def test_path_loop(grid: Dict[int, List[Space]], forward_step_position, guard_starting_position, guard_starting_direction):
    test_grid = deepcopy(grid)
    test_grid[guard_starting_position[1]][guard_starting_position[0]].become_guard(rotate_90_deg(guard_starting_direction).directional_symbol)
    test_grid[forward_step_position[1]][forward_step_position[0]].become_obstruction()

    current_position = deepcopy(guard_starting_position)
    current_direction = deepcopy(guard_starting_direction)

    test_grid, cont, current_position, current_direction = take_next_step(test_grid, current_position, current_direction)
    while cont:
        test_grid, cont, current_position, current_direction = take_next_step(test_grid, current_position, current_direction)
        if guard_starting_position == current_position:
            return True
    return False


def count_unsafe(grid: Dict[int, List[Space]]):
    unsafe = 0
    for row in grid:
        for positional_symbol in grid[row]:
            if positional_symbol.is_seen():
                unsafe += 1 
    return unsafe
        

def build_grid_and_find_guard(input):
    grid: Dict[int, List[Space]] = dict()
    guard_direction = None
    guard_location = (0,0)
    for y_index in range(len(input)):
        for x_index, symbol in enumerate(input[y_index]):
            if symbol == "\n":
                continue
            this_space = Space(symbol)
            if is_guard(symbol):
                this_space.become_guard(symbol)
                guard_direction = get_guard_direction(this_space.symbol)
                guard_location = (x_index, y_index)
            grid[y_index] = grid.get(y_index, list()) + [this_space]
    return grid, guard_direction, guard_location


def take_next_step(grid: Dict[int, List[Space]], guard_location: tuple, guard_direction: Direction, tick: int = 0):
    cardinal_dir = guard_direction.cardinal_direction
    next_location = tuple(map(lambda i,j: i + j, guard_location, cardinal_dir))
    current_guard_space = grid[guard_location[1]][guard_location[0]]

    if not point_in_bounds(grid, next_location):
        current_guard_space.become_seen(tick, guard_direction)
        return grid, False, guard_location, guard_direction
    
    forward_grid_space = grid[next_location[1]][next_location[0]]

    if forward_grid_space.is_obstruction():  
        # Rotate 90 degrees and try again
        new_guard_direction = rotate_90_deg(guard_direction)
        current_guard_space.become_guard(new_guard_direction.directional_symbol)
        return take_next_step(grid, guard_location, new_guard_direction, tick)
    
    # Path is clear, move in the new direction
    current_guard_space.become_seen(tick, guard_direction)
    forward_grid_space.become_guard(guard_direction.directional_symbol)
    # print_nice_grid(grid)
    # print()
    return grid, True, next_location, guard_direction
        
def point_in_bounds(grid, point):
    for p in point:
        if p < 0 or p >= len(grid):
            return False
    return True

def is_guard(symbol):
    return symbol in Direction(">").symbol_to_cardinal_dict

def get_guard_direction(symbol):
    return Direction(symbol)


def print_nice_grid(grid, timer=None):
    for y,_ in enumerate(grid):
        for x,_ in enumerate(grid[y]):
            print(grid[y][x], end="")
            # if timer is not None:
            #     time.sleep(timer)
        print()
    print()

print(main())