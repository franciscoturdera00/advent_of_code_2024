from typing import Dict, List, Tuple

# text_file = "day_12/example.txt"
text_file = "day_12/simple_example.txt"
# text_file = "day_12/input.txt"

AREA = "area"
PERIMETER = "perimeter"
LOCKED_IN_VALUE = 4

def main():
    garden = build_garden(text_file)
    price = find_price(garden)
    return price

def build_garden(file: str):
    with open(file) as f:
        lines = f.readlines()
        garden = [[x for x in line if x != "\n"] for line in lines]
        return garden


def find_price(garden):
    regions: Dict[str, List[Tuple[int, int]]] = dict()
    unique = 0
    for y, _ in enumerate(garden):
        for x, flower in enumerate(garden[y]):
            # Check if current flower has already been spotted in another area
            spotted = flower in regions
            if spotted:
                flower = flower + str(unique)
                unique += 1
            # find area of current flower
            area = find_region_of(flower, (x,y), garden)
            
            for position in area:

                current_flower_attributes = regions.get(flower, {PERIMETER: 0, AREA: list()})
                perimeter = get_current_perimiter((x,y), garden)
                current_flower_attributes[PERIMETER] += perimeter
                current_flower_attributes[AREA].append((x,y))
                regions[flower] = current_flower_attributes
    price = 0
    for region in regions:
        area = len(regions[region][AREA])
        perimeter = regions[region][PERIMETER]
        price += area * perimeter
    for f, val in regions.items():
        print(f, val)
    return price

def find_region_of(starting_flower, current_flower_location, garden, visited = list()):
    if current_flower_location in visited:
        return None
    if not in_bounds(garden, current_flower_location):
        return None
    flower = garden[current_flower_location[1]][current_flower_location[0]]
    if starting_flower == flower:
        directions = get_sorrounding_positions(current_flower_location, garden)
        ret = [current_flower_location]
        for d in directions:
            region = find_region_of(starting_flower, d, garden, visited + [current_flower_location])
            if region is not None:
                ret += region
        return ret
    return None





def get_current_perimiter(current_position, garden):
    perimiter = 0
    flower = garden[current_position[1]][current_position[0]]
    directions = get_sorrounding_positions(current_position, garden)

    for d in directions:
        if not in_bounds(garden, d):
            perimiter += 1
        else:
            other_flower = garden[d[1]][d[0]]
            if not other_flower == flower:
                perimiter += 1
    return perimiter

def in_bounds(grid, position):
    size = len(grid)
    return all(0 <= index < size for index in position)
    

def get_sorrounding_positions(location, grid):
    left = (location[0] - 1, location[1])
    right = (location[0] + 1, location[1])
    up = (location[0], location[1] - 1)
    down = (location[0], location[1] + 1)
    directions = (left, right, up, down)
    return directions

print(main())