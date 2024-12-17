import unittest

from Robot import Robot

class TestDay14(unittest.TestCase):
    def test_example(self):
        robot = Robot([1,1], [3,5], 7, 11)
        robot.take_n_steps(1)
        self.assertEqual(robot.position, [4, 6])
        robot.take_n_steps(1)
        self.assertEqual(robot.position, [0, 0])
    
    def test_step_over(self):
        robot = Robot([1,1], [3,5], 7, 11)
        robot.take_n_steps(2)
        self.assertEqual(robot.position, [0, 0])

if __name__ == '__main__':
    unittest.main()