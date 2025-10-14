g={
    '1': ['2','3','4'],
    '2': ['1','3','4'],
    '3': ['1','2','4'],
    '4': ['1','2','3']
}


c={}
for v in sorted(g):

    c[v]=next(i for i in range(len(g)) if all (c.get(n)!=i for n in g[v]))
print("Coloring of graph is", c)