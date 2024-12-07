
import itertools


class OperationFamily:

    _MULTIPLY = "*"
    _ADD = "+"
    _CONCAT = "||"

    def __init__(self, result, operands):
        self.result = result
        self.operands = operands
        self.operations = [self._ADD, self._MULTIPLY, self._CONCAT]
        self.combination_of_operations = list(itertools.product(self.operations, repeat=len(self.operands) - 1))

    def is_true_equation(self):
        for combination in self.combination_of_operations:
            total = self.operands[0]
            for i, operation in enumerate(combination):
                total = self._apply_operation(operation, total, self.operands[i + 1])
            if total == self.result:
                return True
        return False

    def _apply_operation(self, operation, so_far, new_value):
        if operation == self._ADD:
            return so_far + new_value
        if operation == self._MULTIPLY:
            return so_far * new_value
        if operation == self._CONCAT:
            return int(str(so_far) + str(new_value))
        raise Exception("Invalid operation: " + operation)