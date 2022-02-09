from homeless import Homeless, StandardHomeless, ModerateHomeless, LeftHomeless
from field import Field
from coordinate import Coordinate

from bokeh.plotting import figure, output_file, show

def know_type_homeless(homeless_type):
    if homeless_type.__name__ == StandardHomeless:
        return "Vagabundo Estandar"
    elif homeless_type.__name__ == ModerateHomeless:
        return "Vagabundo Moderado"
    else:
        return "Vagabundo Izquierdo"

def hike(homeless_type, field, step):
    begin = [homeless.position()]
    x_graph = [0]
    y_graph = [0]
    for _ in range(step-1):
        homeless.walk()
        x, y = homeless.position()
        x_graph.append(x)
        y_graph.append(y)
    know_homeless = know_type_homeless(homeless_type)
    graph(x_graph,y_graph,know_homeless,step)
    return homeless.distance_origin()

def simulate_hike(step, attemps, homeless_type):
    homeless = []
    distance = []

    for i in range(attemps):
        homeless.append(homeless_type(name=f"Rasta Cuando {i}"))
        emulate_walk = hike(homeless[i],step,homeless_type)
        distance.append(round(emulate_walk,1))
        
    return distance

def graph(x_graph,y_graph, know, step):
    paint = figure(title=know, x_axis_label="Pasos", y_axis_label="Distancia")
    paint.line(x_graph, y_graph, legend_label=str(step)+"pasos")
    final_x = x_graph[-1]
    final_y = y_graph[-1]
    paint.diamond_cross(0,0, fill_color="green", line_color="green",size=18)
    paint.diamond_cross(final_x,final_y, fill_color="red", line_color="red",size=18)
    final_stretch_x = [0, final_x]
    final_stretch_y = [0, final_y]
    graph.line(final_stretch_x,final_stretch_y, line_width=2, color="blue")
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