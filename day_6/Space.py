from typing import List
from Direction import Direction

class Space:

    _OBSTRUCTION_SYMBOL = "#"
    _SEEN_SYMBOL = "X"

    def __init__(self, symbol):
        self.symbol = symbol
        # Can't do set bc unhasable type
        self._history: List[str] = list()

    def get_history(self):
        return self._history
    
    def add_to_direction_history(self, direction: Direction, tick: int):
        self._history.append((direction.directional_symbol, tick))
    
    def become_seen(self, tick, direction):
        self.symbol = self._SEEN_SYMBOL
        if direction:
            self.add_to_direction_history(direction, tick)
    
    def become_obstruction(self):
        self.symbol = self._OBSTRUCTION_SYMBOL

    def is_seen(self):
        return self._is_symbol(self._SEEN_SYMBOL)

    def is_obstruction(self):
        return self._is_symbol(self._OBSTRUCTION_SYMBOL)
    
    def _is_symbol(self, other):
        return self.symbol == other

    def become_guard(self, sym):
        self.symbol = sym

    def equals(self, other):
        if not hasattr(other, "symbol"):
            return NotImplemented
        return self.symbol == other.symbol
    
    def __repr__(self):
        return self.symbol
    