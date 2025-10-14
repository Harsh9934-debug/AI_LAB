# write a program to implement travel salesman problem

from sys import maxsize
from itertools import permutations  
V=4
def tsp(graph,s):
    vertex=[]
    for i in range(V):
        if i!=s:
            vertex.append(i)
    min_path=maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_pathweight=0
        k=s
        for j in i:
            current_pathweight+=graph[k][j]
            k=j
        current_pathweight+=graph[k][s]
        min_path=min(min_path,current_pathweight)
    return min_path
graph=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
    ]
s=0
print("The minimum cost of the travel salesman problem is ",tsp(graph,s))   