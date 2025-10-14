from queue import PriorityQueue as PQ
g=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
v,q=set(),PQ();q.put((0,0))
while not q.empty():
 _,n=q.get()
 if n in v:continue
 v.add(n);print(n,end=' ')
 if n==3:break
 [q.put((0,i)) for i in g[n] if i not in v]
