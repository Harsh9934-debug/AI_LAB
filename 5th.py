g=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

v,q=set(),[0]
while q:
    n=q.pop(0)
    if  n in v:continue
    print(n , end='')
    v.add(n )
    if n==3:break
    q+= g[n]