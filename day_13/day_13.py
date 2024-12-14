from typing import List
from VectorCombination import VectorCombination

text_file = "day_13/example.txt"
# text_file = "day_13/input.txt"

COST_A = 3
COST_B = 1

def main():
    vector_combinations = read_button_behavior(text_file)
    cheapest_scalars = [vector.calculate_cheapest_linear_combination(COST_A, COST_B) for vector in vector_combinations]
    cheapest_scalars = list(filter(lambda c: c[1] != -1, cheapest_scalars))
    cheapest_scalars = [sc[1] for sc in cheapest_scalars]
    return sum(cheapest_scalars)

def read_button_behavior(file):
    vectors: List[VectorCombination] = list()
    f = open(file)
    input = f.readlines()
    for i in range(0, len(input), 4):
        sub = input[i:i + 4]
        vectors.append(VectorCombination(sub, 10000000000000))
    f.close()
    return vectors


print(main())