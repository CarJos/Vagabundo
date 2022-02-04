from homeless import StandardHomeless
from field import Field
from coordinate import Coordinate

from bokeh.plotting import figure, output_file, show

def hike(homeless, field, step):
    begin = field.get_coordinate(homeless)
    for _ in range(step):
        field.move_homeless(homeless)

    return begin.distance(field.get_coordinate(homeless))

def simulate_hike(step, attemps, homeless_type):
    homeless = homeless_type(name='Ivan')
    begin = Coordinate(0,0)
    distance = []

    for _ in range(attemps):
        field = Field()
        field.add_homeless(homeless, begin)
        simulation_hike = hike(homeless, field, step)
        distance.append(round(simulation_hike,1))
    
    return distance

def graph(x,y):
    paint = figure(title="Camino Aleatorio", x_axis_label="Pasos", y_axis_label="Distancia")
    paint.line(x, y, legend_label="Distancia")
    show(paint)

def main(walk_distance, attemps, homeless_type):
    average_walking_distance = []
    for steps in walk_distance:
        distance = simulate_hike(steps, attemps, homeless_type)
        distance_average = round(sum(distance)/len(distance), 4)
        distance_max = max(distance)
        distance_min = min(distance)
        average_walking_distance.append(distance_average)
        print(f"{homeless_type.__name__}caminata aleatoria{steps} pasos")
        print(f"Media = {distance_average}")
        print(f"Max = {distance_max}")
        print(f"Min = {distance_min}")

        graph(walk_distance, average_walking_distance)

if __name__ == "__main__":
    walk_distance = [10, 100, 1000, 10000]
    attemps = 100

    main(walk_distance, attemps, StandardHomeless)