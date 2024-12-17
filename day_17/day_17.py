import re

from Register import REGISTER_A, REGISTER_B, REGISTER_C
from Instructions import adv, bst, bdv, bxc, bxl, cdv, jnz, out
from Output import Output

# text_file = "day_17/example.txt"
text_file = "day_17/input.txt"
# text_file = "day_17/example_2.txt"
#148680000

def main():
    output = Output()
    program = read_input(text_file)
    register_a_value = 13560000
    while program != output.val:
        program = read_input(text_file)

        if register_a_value is not None:
            register_a_value += 1
            if register_a_value % 10000 == 0:
                print(register_a_value)
            REGISTER_A.update_value(register_a_value)

        combo_operands = {0: (lambda : 0), 1: (lambda : 1), 2: (lambda : 2), 3: (lambda : 3),
                        4: (lambda : REGISTER_A.val), 5: (lambda : REGISTER_B.val), 6: (lambda : REGISTER_C.val)}

        instruction_pointer = 0

        output = Output()

        while instruction_pointer < len(program):
            if program[instruction_pointer] == 0:
                instruction_pointer = adv(program[instruction_pointer + 1], combo_operands, instruction_pointer)
                continue
            if program[instruction_pointer] == 1:
                instruction_pointer = bxl(program[instruction_pointer + 1], instruction_pointer)
                continue
            if program[instruction_pointer] == 2:
                instruction_pointer = bst(program[instruction_pointer + 1], combo_operands, instruction_pointer)
                continue
            if program[instruction_pointer] == 3:
                instruction_pointer = jnz(program[instruction_pointer + 1], instruction_pointer)
                continue
            if program[instruction_pointer] == 4:
                instruction_pointer = bxc(instruction_pointer)
                continue
            if program[instruction_pointer] == 5:
                instruction_pointer = out(program[instruction_pointer + 1], combo_operands, output, instruction_pointer)
                continue
            if program[instruction_pointer] == 6:
                instruction_pointer = bdv(program[instruction_pointer + 1], combo_operands, instruction_pointer)
                continue
            if program[instruction_pointer] == 7:
                instruction_pointer = cdv(program[instruction_pointer + 1], combo_operands, instruction_pointer)
                continue
    print(register_a_value)
    return register_a_value

def read_input(input_file):
    with open(input_file) as f:
        input = f.readlines()
        num = r"\d+"
        REGISTER_A.update_value(int(re.search(num, input[0]).group()))
        REGISTER_B.update_value(int(re.search(num, input[1]).group()))
        REGISTER_C.update_value(int(re.search(num, input[2]).group()))
        program = [int(x) for x in input[4].split(":")[1:][0][1:].split(",")]
        return program


# result = "".join(str(main())[1: -1].split())
# print(result)
print("A needed: " + str(main()))