from copy import deepcopy
import math
import numpy as np
from typing import Dict, List, Set, Tuple

# text_file = "day_8/simple_example.txt"
# text_file = "day_8/example.txt"
# text_file = "day_8/example_2.txt"
text_file = "day_8/puzzle_input.txt"

def node_location_dict(input: List[str]):
    grid: Dict[int, Set] = dict()
    for y, row in enumerate(input):
        for x, element in enumerate(row):
            if element == "\n":
                continue
            if not (element == "." or element == "#"):
                current = grid.get(element, list())
                current.append((x,y))
                grid[element] = current
    return grid

# def find_antinodes(node1, node2, bounds): # part 1
    distance = tuple(np.subtract(node2, node1))
    ahead = tuple(np.add(node2, distance))
    behind = tuple(np.subtract(node1, distance))
    antinodes = set()
    if in_bounds(behind, bounds):
        antinodes.add(behind)
    if in_bounds(ahead, bounds):
        antinodes.add(ahead)
    return antinodes

def find_antinodes(node1, node2, bounds) -> Set[Tuple]: # part 2
    if node1[0] == node2[0]:
        return set((x, node1[0]) for x in range(len(bounds[0])))
    if node1[1] == node2[1]:
        return set((node1[0], y) for y in range(len(bounds)))
    
    if node1 == node2:
        return set()
    
    slope = ((node2[0] - node1[0]), (node2[1] - node1[1]))
    resonance = set()
    resonance.add(node1)
    i = 1
    step = (m * i for m in slope)
    while True:
        step = tuple(m * i for m in slope)
        forward_step = np.add(node1, step)
        forward_node_to_check = (int(forward_step[0]), int(forward_step[1]))
        backward_step = np.subtract(node1, step)
        backward_node_to_check = (int(backward_step[0]), int(backward_step[1]))

        ahead_in_bounds = in_bounds(forward_node_to_check, bounds)
        behind_in_bounds = in_bounds(backward_node_to_check, bounds)
        if ahead_in_bounds:
            resonance.add(forward_node_to_check)
        if behind_in_bounds:
            resonance.add(backward_node_to_check)
        if not ahead_in_bounds and not behind_in_bounds:
            break
        i += 1
    return resonance
    

def in_bounds(point: Tuple, bounds):
    return all(p >= 0 and p < bound for p, bound in zip(tuple(point), bounds))

def find_all_antinodes(node_locations, bounds):
    all_antinodes = set()
    for _, locations in node_locations.items():
        for location_index, node_location in enumerate(locations):
            for other_location_index in range(location_index + 1, len(locations)):
                antinodes = find_antinodes(node_location, locations[other_location_index], bounds)
                all_antinodes.update(antinodes)
    return all_antinodes

def print_nice_grid(frame, antinodes: List[Tuple]):
    size = len(frame)
    print()
    for i in range(size):
        print(i, end="")
    print()
    for y, frame_row in enumerate(frame):
        row = str(y)
        for x, space in enumerate(frame_row):
            if (x,y) in antinodes and space == ".":
                row += "#"
            else:
                row += space
        row +="\n"
        print(row)

def main():
    with open(text_file) as f:
        lines = f.readlines()
        x_bound = len(lines[0]) - 1
        y_bound = len(lines)
        node_locations = node_location_dict(lines)
        antinodes = find_all_antinodes(node_locations, (x_bound, y_bound))
        # print_nice_grid(lines, list(antinodes))
        return antinodes

answer = main()
# print(answer)
print(len(answer))


# def run_test(input, expected):
#     with open(input) as f:
#         lines = f.readlines()
#         x_bound = len(lines[0]) - 1
#         y_bound = len(lines)
#         antinodes = find_all_antinodes(lines, (x_bound, y_bound))
#         return antinodes == expected

# run_test(text_file, 34)

# print(in_bounds((1,1), (40,40)))
# print(in_bounds((1,-1), (40,40)))
# print(in_bounds((-1,1), (40,40)))
# print(in_bounds((-1,-1), (40,40)))
# print(in_bounds((40,1), (40,40)))
# print(in_bounds((1,40), (40,40)))
