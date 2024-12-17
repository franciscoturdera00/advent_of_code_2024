

import math
from Register import REGISTER_A, REGISTER_B, REGISTER_C
from Output import Output

# 0
def adv(combo_operand, combo_operands, current_instruction_pointer):
    numerator = REGISTER_A.val
    divisor = 2 ** combo_operands[combo_operand]()
    REGISTER_A.update_value(math.floor(numerator / divisor))
    return current_instruction_pointer + 2

# 1
def bxl(literal_operand, current_instruction_pointer):
    REGISTER_B.update_value(literal_operand ^ REGISTER_B.val)
    return current_instruction_pointer + 2

# 2
def bst(combo_opearand, combo_operands, current_instruction_pointer):
    REGISTER_B.update_value(combo_operands[combo_opearand]() % 8)
    return current_instruction_pointer + 2

# 3
def jnz(literal_operand, current_instruction_pointer):
    if REGISTER_A.val == 0:
        return current_instruction_pointer + 2
    return literal_operand

# 4
def bxc(current_instruction_pointer):
    REGISTER_B.update_value(REGISTER_B.val ^ REGISTER_C.val)
    return current_instruction_pointer + 2

# 5
def out(combo_operand, combo_operands, output_so_far: Output, current_instruction_pointer):
    new_output = combo_operands[combo_operand]() % 8
    output_so_far.add_output(new_output)
    return current_instruction_pointer + 2

# 6
def bdv(combo_operand, combo_operands, current_instruction_pointer):
    numerator = REGISTER_A.val
    divisor = 2 ** combo_operands[combo_operand]()
    REGISTER_B.update_value(math.floor(numerator / divisor))
    return current_instruction_pointer + 2

# 7
def cdv(combo_operand, combo_operands, current_instruction_pointer):
    numerator = REGISTER_A.val
    divisor = 2 ** combo_operands[combo_operand]()
    REGISTER_C.update_value(math.floor(numerator / divisor))
    return current_instruction_pointer + 2
