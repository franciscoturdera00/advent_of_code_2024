
class Register:

    def __init__(self, val=0):
        self.val = val

    def update_value(self, val):
        self.val = val


REGISTER_A = Register()
REGISTER_B = Register()
REGISTER_C = Register()