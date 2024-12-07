
from typing import List
from OperationFamily import OperationFamily

# text_file = "day_7/example.txt"
text_file = "day_7/part_1.txt"

def main():
    total = 0
    with open(text_file) as f:
        lines = f.readlines()
        operation_families: List[OperationFamily] = build_operand_family(lines)
        for operation_family in operation_families:
            if operation_family.is_true_equation():
                total += operation_family.result
        return total

        
def build_operand_family(input):
    operation_families = list()
    for line in input:
        result, operands_str = line.split(":")
        result = int(result)
        operands = list(map(int, operands_str.split(" ")[1:]))
        operation_families.append(OperationFamily(result, operands))
    return operation_families

print(main())

        