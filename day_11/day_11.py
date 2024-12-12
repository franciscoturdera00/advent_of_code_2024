import math
from typing import List

# text_file = "day_11/example.txt"
text_file = "day_11/input.txt"

BLINKS = 75
MULTIPLIER = 2024

def main():
     with open(text_file) as f:
        line = f.readline()
        stones = list(int(i) for i in line.split())
        return perform_blink(BLINKS, stones)

# This is too slow. Next start: memoization
def perform_blink(n, stones: List[int]):
    if len(stones) > 1:
        answer = list()
        half = math.floor(len(stones) / 2)
        answer = perform_blink(n, stones[:half]) + perform_blink(n, stones[half:])
        return answer
    
    stone = stones[0]
    answer = None
    if stone == 0:
        answer = [1]
    elif is_even_number_digit(stone):
        answer = split_even_stone(stone)
    else:
        answer =  [stone * MULTIPLIER]
    if n > 1:
        return perform_blink(n - 1, answer)
    return len(answer)
    
def is_even_number_digit(stone):
        return len(str(stone)) % 2 == 0

def split_even_stone(stone):
    str_val = str(stone)
    midpoint = int(len(str_val) / 2)
    first, second = int(str_val[:midpoint]), int(str_val[midpoint:])
    return [first, second]


print(main())
