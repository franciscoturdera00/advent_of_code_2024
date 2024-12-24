
# text_file = "day_24/example.txt"
text_file = "day_24/input.txt"

def read_input(file):
    logic_gates = dict()
    with open(file) as f:
        for line in f: # Initial values
            if line.strip() == "":
                break
            var, val = line.split()
            var = var[:-1]
            logic_gates[var] = (lambda val=int(val): val)
            # print(var, logic_gates[var]())
        for line in f: # gates
            input_a, gate, input_b, _, var = line.split()
            # print(input_a, input_b, gate, var)
            if gate == "AND":
                logic_gates[var] = (lambda input_a=input_a, input_b=input_b: AND(input_a, input_b))
            if gate == "OR":
                logic_gates[var] = (lambda input_a=input_a, input_b=input_b: OR(input_a, input_b))
            if gate=="XOR":
                logic_gates[var] = (lambda input_a=input_a, input_b=input_b: XOR(input_a, input_b))
        return logic_gates

logic_gates = read_input(text_file)

def XOR(input_a, input_b):
    return 1 if logic_gates[input_a]() != logic_gates[input_b]() else 0

def OR(input_a, input_b):
    return 1 if logic_gates[input_a]() or logic_gates[input_b]() else 0

def AND(input_a, input_b):
    return 1 if logic_gates[input_a]() and logic_gates[input_b]() else 0

def main():
    new_values = dict()
    for gate in logic_gates:
        new_values[gate] = logic_gates[gate]()
    zs = [(var, val) for var, val in new_values.items() if var.startswith("z")]
    zs.sort(key=lambda z: int(z[0][1:]), reverse=True)
    binaries = [str(z[1]) for z in zs]
    final_decimal_value = int("".join(binaries), 2)
    return final_decimal_value

print(main())