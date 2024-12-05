import re

text_file = "day_3/part_1.txt"
# text_file = "Day 3\\test_input.txt"
# text_file = "Day 3\\test_2.txt"
 

def find_all_operations(input):
    # Reg exp: Takes any "don't(), do(), mult(number(max 3 digits), number(max 3 digits))"
    regular_exp=r"don't\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\)"
    return re.findall(regular_exp, input)

def perform_multiplication(mult_instance):
    regular_exp = r"\d{1,3}" # number of 1 - 3 digits
    numbers = re.findall(regular_exp, mult_instance)
    total = 1
    for n in numbers:
        total *= int(n)
    return total

def add_all_mults(mult_instances):
    total = 0
    for mult in mult_instances:
        total += perform_multiplication(mult)
    return total

#removes mults invalidated by 'don't's
def validate_input(operations):
    do = True
    new_mults = []
    for operation in operations:
        if operation == "don't()":
            do = False
            continue
        if operation == "do()":
            do = True
            continue
        if do:
            new_mults.append(operation)
    return new_mults

with open(text_file) as f:
    program = str(f.readlines())
    all_mults = find_all_operations(program)
    cleaned_mults = validate_input(all_mults)
    print(add_all_mults(cleaned_mults))
