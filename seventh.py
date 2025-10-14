# write a program to solve the graph coloring problem

def color_vertices(g):
    vs = sorted(g)
    c = {}
    for v in vs:
        used = {c[n] for n in g.get(v, []) if n in c}
        c[v] = next(i for i in range(len(vs)) if i not in used)
    return c

if __name__ == '__main__':
    g = {
        'A':['B','C','D'],
        'B':['A','D'],
        'C':['A','D'],
        'D':['A','B','C','E'],
        'E':['D']}
    print('Coloring of graph is', color_vertices(g))