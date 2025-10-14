# write a program to solve the graph coloring problem

def color_vertices(graph):
    vertices=sorted((list(graph.keys())))
    color_graph={}
    for vertex in vertices:
        unused_colours=len(vertices)*True
        for neighbour in graph[vertex]:
            if neighbour in color_graph:
                unused_colours[color_graph[neighbour]]=False
        for color in range(len(vertices)):
            if unused_colours(color):
                color_graph[vertex]=color
                break
    return color_graph  
graph={
    'A':['B','C','D'],
    'B':['A','D'],
    'C':['A','D'],
    'D':['A','B','C','E'],
    'E':['D']
}   
print("Coloring of graph is ",color_vertices(graph))