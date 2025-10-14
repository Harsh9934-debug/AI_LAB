# Graph Coloring problem

g=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
c=[-1]*len(g)
for v in range(len(g)):
    used={c[i]for i in range(len(g))if g[v][i]and c[i]!=-1}
    c[v]=next(x for x in range(len(g))if x not in used)
print("Represents the different Colors addigned to each vertices:",c)