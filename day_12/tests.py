
import unittest
from day_12 import build_garden, find_price

class TestDay12(unittest.TestCase):
    def test_example(self):
        example = "day_12/example.txt"
        grid = build_garden(example)
        price = find_price(grid)
        self.assertEqual(price, 1930)
    
    def test_simple_example(self):
        example = "day_12/simple_example.txt"
        grid = build_garden(example)
        price = find_price(grid)
        self.assertEqual(price, 772)
    
    # def test_input(self):
    #     input = "day_12/input.txt"
    #     grid = build_garden(input)
    #     price = find_price(grid)
    #     self.assertEqual(price, 772)

if __name__ == '__main__':
    unittest.main()