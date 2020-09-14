

def create_new_vertex(graph, start_edge):
    graph[start_edge] = []


def add_connection(graph, start_edge, end_edge):
    if start_edge not in graph:
        create_new_vertex(graph, start_edge)
    graph[start_edge].append(end_edge)


def create_graph():
    graph = {}
    add_connection(graph, '1', '2')
    add_connection(graph, '1', '3')
    add_connection(graph, '2', '1')
    add_connection(graph, '2', '4')
    add_connection(graph, '2', '5')
    add_connection(graph, '3', '1')
    add_connection(graph, '3', '6')
    add_connection(graph, '3', '7')
    add_connection(graph, '4', '2')
    add_connection(graph, '5', '2')
    add_connection(graph, '6', '3')
    add_connection(graph, '7', '3')
    return graph


def graph_travel(graph, vertex, visited_vertexes):
    if vertex in graph:
        if vertex not in visited_vertexes:
            visited_vertexes.append(vertex)
        else:
            return
        for connected_vertex in graph[vertex]:
            graph_travel(graph, connected_vertex, visited_vertexes)
    else:
        print ("The vertex is not in the graph")
        exit()


if __name__ == '__main__':
    visited_vertexes = []
    graph = create_graph()
    graph_travel(graph, '1', visited_vertexes)
    print("Visited vertexes: ", visited_vertexes)
