# write a program to implement the Best First Search Algorithm

from queue import PriorityQueue as PQ
def s(g,S,G):
    v,q=set(),PQ(); q.put((0,S))
    while not q.empty():
        c,n=q.get()
        if n in v: continue
        v.add(n)
        print(n,end=" ")
        if n==G: break
        for nn,w in g[n].items():
            if nn not in v: q.put((c+w,nn))

graph={
    'A':{'B':1,'C':4},
    'B':{'A':1,'D':2,'E':5},
    'C':{'A':4,'F':1},
    'D':{'B':2},
    'E':{'B':5,'F':3},
    'F':{'C':1,'E':3}
}
print("Following is the Best First Search")
s(graph,'A','F')  