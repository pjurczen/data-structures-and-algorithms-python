from src.karger_min_cut.graph import Graph
from src.karger_min_cut.vertex import Vertex, VertexKey


def read_file_into_array(file_name: str) -> []:
    result = []
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file:
            # Split the line into numbers, convert to int, and omit the first number
            numbers = [int(num) for num in line.split()]
            result.append(numbers)
    return result


def create_vertex_from_line(line: []) -> Vertex:
    vertex = Vertex(VertexKey(line[0]))
    for neighbour in line[1:]:
        vertex.add_neighbour(VertexKey(neighbour))
    return vertex


def create_graph_from_array(lines: []) -> Graph:
    graph = Graph()
    for line in lines:
        vertex = create_vertex_from_line(line)
        graph.add_vertex(vertex)
    return graph


def create_graph_from_file(file_name: str) -> Graph:
    lines = read_file_into_array(file_name)
    return create_graph_from_array(lines)
