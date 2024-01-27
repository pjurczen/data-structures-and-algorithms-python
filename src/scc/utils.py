from src.scc.directed_graph import DirectedGraph


def read_file_into_array(file_name: str) -> []:
    result = []
    with open(file_name, 'r', encoding='UTF-8') as file:
        for line in file:
            # Split the line into numbers, convert to int, and omit the first number
            numbers = [int(num) for num in line.split()]
            result.append(numbers)
    return result


def create_edge_from_line(line: []) -> ():
    return line[0], line[1]


def create_graph_from_array(lines: []) -> DirectedGraph:
    graph = DirectedGraph()
    for line in lines:
        i, j = create_edge_from_line(line)
        graph.add_arc(i, j)
    return graph


def create_reversed_graph_from_array(lines: []) -> DirectedGraph:
    graph = DirectedGraph()
    for line in lines:
        i, j = create_edge_from_line(line)
        graph.add_arc(j, i)
    return graph


def create_graph_from_file(file_name: str) -> DirectedGraph:
    lines = read_file_into_array(file_name)
    return create_graph_from_array(lines)


def create_reversed_graph_from_file(file_name: str) -> DirectedGraph:
    lines = read_file_into_array(file_name)
    return create_reversed_graph_from_array(lines)
