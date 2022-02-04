import random

class Homeless:
    def __init__(self, name, x=0, y=0):
        self.name = name
        self.x = x
        self.y = y
    
    def position(self):
        return (self.x, self.y)

    def distance_origin(self):
        return (self.x**2 + self.y**2)**0.5

class StandardHomeless(Homeless):
    def __init__(self,name):
        super().__init__(name)

    def walk(self):
        return random.choice([(1,0), (-1,0), (0,1), (0,-1)])