# write a program to implement travel salesman problem

from sys import maxsize
from itertools import permutations  
def tsp(g,s=0):
    n=len(g)
    vs=[i for i in range(n) if i!=s]
    return min(sum(g[a][b] for a,b in zip((s,)+p,p+(s,))) for p in permutations(vs))
graph=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
s=0
print('The minimum cost of the travel salesman problem is',tsp(graph,s))