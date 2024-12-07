class Direction():

    _LEFT = (-1, 0)
    _UP = (0, -1)
    _RIGHT = (1,0)
    _DOWN = (0, 1)
    symbol_to_cardinal_dict = {"<": _LEFT, "^": _UP, ">": _RIGHT, "v": _DOWN}
 
    def __init__(self, directional_symbol: str):
        self.directional_symbol = directional_symbol
        self.cardinal_direction = self.symbol_to_cardinal_dict[directional_symbol]

    def equals(self, other):
        if not hasattr(other, "directional_symbol"):
            return NotImplemented
        return self.directional_symbol == other.directional_symbol
    
    def __repr__(self):
        return self.directional_symbol
