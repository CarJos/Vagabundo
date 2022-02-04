class Field:

    def __init__(self):
        self.homeless_coordinates = {}

    def add_homeless(self, homeless, coordinates):
        self.homeless_coordinates[homeless] = coordinates

    def move_homeless(self, homeless):
        delta_x, delta_y = homeless.walk()
        current_coordinates = self.homeless_coordinates[homeless]
        new_coordinate = current_coordinates.move(delta_x, delta_y)
        self.homeless_coordinates[homeless] = new_coordinate
    
    def get_coordinate(self, homeless):
        return self.homeless_coordinates[homeless]