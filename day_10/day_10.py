
from typing import Tuple


# text_file = "day_10/two_paths_to_same_answer.txt"
# text_file = "day_10/large_example.txt"
# text_file = "day_10/2_trails.txt"
text_file = "day_10/input.txt"

def main():
    with open(text_file) as f:
        input = f.readlines()
        grid = make_grid(input)
        # print_grid(grid)
        trailheads = find_all_trailheads(grid)
        return sum(trailheads)

def find_all_trailheads(grid, start=0, g=9):
    goals = find_all_goals(grid, g)
    trailhead_counts = list()
    for y, row in enumerate(grid):
        for x, num in enumerate(row):
            if num == start:
                trailhead_count = 0
                for g in goals:
                    trails = count_trailhead(grid, (x,y), start - 1, g)
                    trailhead_count += trails
                    
                trailhead_counts.append(trailhead_count)
    return trailhead_counts

def find_all_goals(grid, goal):
    goals = list()
    for y, _ in enumerate(grid):
        for x, val in enumerate(grid[y]):
            if val == goal:
                goals.append((x,y))
    return goals



# def has_trailhead(grid, current_location, last_seen, goal, step = 1): # part 1
    if not in_bounds(grid, current_location):
        return False
    value = grid[current_location[1]][current_location[0]]
    if value != last_seen + step:
        return False
    if current_location == goal:
        return True
    
    left = (current_location[0] - 1, current_location[1])
    right = (current_location[0] + 1, current_location[1])
    up = (current_location[0], current_location[1] - 1)
    down = (current_location[0], current_location[1] + 1)
    directions = (left, right, up, down)

    paths = any(list(has_trailhead(grid, d, value, goal) for d in directions))
    return paths

def count_trailhead(grid, current_location, last_seen, goal, step = 1): # part 2
    if not in_bounds(grid, current_location):
        return 0
    value = grid[current_location[1]][current_location[0]]
    if value != last_seen + step:
        return 0
    if current_location == goal:
        return 1
    
    left = (current_location[0] - 1, current_location[1])
    right = (current_location[0] + 1, current_location[1])
    up = (current_location[0], current_location[1] - 1)
    down = (current_location[0], current_location[1] + 1)
    directions = (left, right, up, down)

    paths = sum(list(count_trailhead(grid, d, value, goal) for d in directions))
    return paths


def in_bounds(grid, position):
    size = len(grid)
    return all(0 <= index < size for index in position)

def make_grid(input):
    grid = list()
    for i, line in enumerate(input):
        grid.append(list())
        for num in line:
            if num == "\n":
                continue
            grid[i].append(int(num))
    return grid

def print_grid(grid, start=None, end=None):
    for y, line in enumerate(grid):
        for x, num in enumerate(line):
            if start and (x,y) == start:
                print("S ", end="")
            elif end and (x,y) == end:
                print("X ", end="")
            else:
                print(str(num) + " ", end="")
        print()
    print()

print(main())