import math
import re
from typing import List

from Robot import Robot

# text_file = "day_14/example.txt"
text_file = "day_14/input.txt"

GRID_X = 101
GRID_Y = 103
GRID = [GRID_X, GRID_Y]
TICKS = 10000

def main():
    robots: List[Robot] = build_robots(text_file)
    # print_grid(robots)
    (robot.take_n_steps(TICKS) for robot in robots)
    
    # for i in range(TICKS): # part 2 attempt :/
    #     (robot.take_n_steps(1) for robot in robots)
    #     if [0, math.floor(GRID_Y / 2)] in [robot.position for robot in robots]:
    #         print_grid(robots)
    #         print(i)
    robs_per_quad = robots_per_quadrant(robots)
    print(robs_per_quad)
    return math.prod(robs_per_quad)

def robots_per_quadrant(robots: List[Robot]):
    half_x = math.floor(GRID_X / 2)
    half_y = math.floor(GRID_Y / 2)

    # half = [half_x, half_y]
    
    robot_count = [0] * 4 # upleft, upright, downleft, downright

    for robot in robots:
        if robot.position[0] == half_x or robot.position[1] == half_y:
            continue
        left, up = [False] * 2
        if robot.position[0] < half_x:
            left = True
        if robot.position[1] < half_y:
            up = True
        if left and up:
            robot_count[0] += 1
        if not left and up:
            robot_count[1] += 1
        if left and not up:
            robot_count[2] += 1
        if not left and not up:
            robot_count[3] += 1
    return robot_count

def build_robots(input_file):
    with open(input_file) as f:
        robots_build = f.readlines()
        robots = list()
        for r in robots_build:
            exp=r"\-?\d+,\-?\d+"
            pos, vel = re.findall(exp, r)
            pos = [int(p) for p in pos.split(",")]
            vel = [int(v) for v in vel.split(",")]
            robot = Robot(pos, vel, GRID_X, GRID_Y)
            robots.append(robot)
        return robots


def print_grid(robots):
    positions = [robot.position for robot in robots]
    num_per_pos = dict()
    for pos in positions:
        row = num_per_pos.get(pos[1], dict())
        val = row.get(pos[0], 0)
        val += 1
        row[pos[0]] = val
        num_per_pos[pos[1]] = row
    print("------------")
    for y in range(GRID_Y):
        # if y == math.floor(GRID_Y / 2):
        #     print()
        #     continue
        for x in range(GRID_X):
            # if x == math.floor(GRID_X / 2):
            #     print(" ", end="")
            #     continue
            if [x,y] in positions:
                print(num_per_pos[y][x], end="")
            else:
                print(".", end="")
        print()
    print("------------")
    print()

print(main())