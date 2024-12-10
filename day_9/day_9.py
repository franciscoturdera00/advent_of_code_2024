
from typing import List, Tuple

# text_file = "day_9/simple_example.txt"
# text_file = "day_9/example.txt"
text_file = "day_9/input.txt"

EMPTY = "."

def main():
    with open(text_file) as f:
        input = f.readline()
        individual_blocks = disk_map_to_actual(input)
        optimized_space = get_optimized_space(individual_blocks)
        stream = to_continous_stream(optimized_space)
        checksum = calculate_checksum(stream)

        return checksum

def calculate_checksum(optimized_space):
    total = 0
    for i, val in enumerate(optimized_space):
        if val != EMPTY:
            total += i * int(val)
    return total

# def get_optimized_space(blocks: str): # part 1
    index = len(blocks) - 1
    new_block = list()
    for i, disk_id in enumerate(blocks):
        if i > index:
            break
        if disk_id == EMPTY:
            while blocks[index] == EMPTY:
                index -= 1
                if i > index:
                    break
            new_block.append(blocks[index])
            index -= 1
        else:
            new_block.append(disk_id)
    new_block = new_block[:-1] if new_block[-1] == EMPTY else new_block # Removes possible last None
    return new_block

def get_section_length(starting_index, actual_disk_map):
    current = actual_disk_map[starting_index]
    for i, value in enumerate(actual_disk_map[starting_index:]):
        if value == current:
            continue
        return i
    return len(actual_disk_map) - starting_index

def convert_to_value_length_pairs(individual_blocks):
    value_length_pairs = list()
    index = 0
    while index < len(individual_blocks):
        section_length = get_section_length(index, individual_blocks)
        value_length_pairs.append((individual_blocks[index], section_length))
        index += section_length
    return value_length_pairs


def to_continous_stream(optimized_space):
    ret = list()
    for p, l in optimized_space:
        ret += [str(p)] * l
    return ret

def get_optimized_space(individual_blocks: List[int]):
    value_length_pairs: List[Tuple] = convert_to_value_length_pairs(individual_blocks)
    reversed_value_length_pairs: List[Tuple] = list(reversed(value_length_pairs))
    index = len(reversed_value_length_pairs) - 1
    for i, (value, length) in enumerate(reversed_value_length_pairs):
        index = 0
        if value == EMPTY:
            continue
        while index < len(value_length_pairs):
            value2, length2 = value_length_pairs[index]
            if (value, length) == (value2, length2):
                break
            if value2 == EMPTY and length <= length2:
                value_length_pairs.reverse()
                index_of_found = value_length_pairs.index((value, length))
                value_length_pairs.insert(index_of_found, (EMPTY, length))
                value_length_pairs.remove((value, length))
                value_length_pairs.reverse()

                value_length_pairs.remove((EMPTY, length2))
                value_length_pairs.insert(index, (value, length))
                if length2 > length:
                    value_length_pairs.insert(index + 1, (EMPTY, length2 - length))
                break
            index += 1
    return value_length_pairs 
    
def disk_map_to_actual(disk_map: str):
    disk = True
    id = 0
    result = list()
    for num in disk_map:
        for _ in range(int(num)):
            if disk:
                result.append(id)
            else:
                result.append(EMPTY)
        if disk:
            id += 1
        disk = not disk
    return result
        
print(main())

# Attempted: 
# 141228547136
# 88102131632