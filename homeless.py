import random

class Homeless:
    def __init__(self, name):
        self.name = name

class StandardHomeless(Homeless):
    def __init__(self,name):
        super().__init__(name)

    def walk(self):
        return random.choice([(1,0), (-1,0), (0,1), (0,-1)])