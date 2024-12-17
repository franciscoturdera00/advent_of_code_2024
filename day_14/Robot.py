
class Robot:

    def __init__(self, position, velocity, grid_x, grid_y):
        self.position = position
        self.velocity = velocity
        self.tick = 0
        self.grid = (grid_x, grid_y)

    
    def take_n_steps(self, n):
        big_step = [n * i for i in self.velocity]
        new_position = [(position + step) % size for position, step, size in zip(self.position, big_step, self.grid)]
        self.position = new_position
        self.tick += n
    
    def __repr__(self):
        return "(" + str(self.position) + ", " + str(self.velocity) + ")"