# write a program to solve the graph coloring problem

def color_vertices(graph):
    vertices = sorted(list(graph.keys()))
    color_graph = {}
    for vertex in vertices:
        unused_colours = [True] * len(vertices)
        for neighbour in graph.get(vertex, []):
            if neighbour in color_graph:
                used = color_graph[neighbour]
                if 0 <= used < len(unused_colours):
                    unused_colours[used] = False
        for color in range(len(vertices)):
            if unused_colours[color]:
                color_graph[vertex] = color
                break
    return color_graph
if __name__ == '__main__':
    graph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['A', 'B', 'C', 'E'],
        'E': ['D']
    }
    print("Coloring of graph is", color_vertices(graph))