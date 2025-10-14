from itertools import permutations 
g=[
    [1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]
]
print("Min path",min(sum(g[a][b] for a,b in zip((0,)+p,p+(0,)))for p in permutations([1,2,3])))