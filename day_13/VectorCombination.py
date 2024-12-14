
import math


class VectorCombination:

    def __init__(self, A, B, wish_result, prefix=0):
        self.A = A
        self.B = B
        self.wish_result = [int(str(prefix) + str(res)) for res in wish_result]

    def __init__(self, raw, prefix=0):
        self.A = self._read_button_input(raw[0])
        self.B = self._read_button_input(raw[1])
        self.wish_result = [int(str(prefix) + str(res)) for res in self._read_button_input(raw[2], "=")]

    def calculate_cheapest_linear_combination(self, cost_a, cost_b):
        cheapest = -1
        cheapest_pushes = (-1, -1)
        lowest = [min(a, b) for a,b in zip(self.A, self.B)]
        extremes = [math.ceil(wish / min) for wish, min in zip(self.wish_result, lowest)]
        for push_b in range(1, extremes[1] + 1):
            for push_a in range(1, extremes[0] + 1):
                aA = [push_a * a for a in self.A]
                bB = [push_b * b for b in self.B]
                sum = [a + b for a, b in zip(aA, bB)]
                if sum == self.wish_result:
                    cost = cost_a * push_a + cost_b * push_b 
                    if cheapest == -1 or cost < cheapest:
                        cheapest_pushes = (push_a, push_b)
                        cheapest = cost
        return cheapest_pushes, cheapest

    
    def _read_button_input(self, line, sp = "+"):
        button = line.split(":")
        nums = button[1].split(",")
        x = nums[0].split(sp)[1]
        y = nums[1].split(sp)[1]
        return [int(x), int(y)]
    
    def __repr__(self):
        return "(" + str(self.A) + ", " + str(self.B) + ", " + str(self.wish_result) + ")"