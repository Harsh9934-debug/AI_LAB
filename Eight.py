m=[[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
n=len(m)
s=[[0]*n for _ in range(n)]
def go(x,y):
 if x<0 or y<0 or x>=n or y>=n or m[x][y]==0 or s[x][y]:
   return 0
 s[x][y]=1
 if (x,y)==(n-1,n-1)or go(x+1,y)or go(x,y+1):
   return 1
 s[x][y]=0
go(0,0)
for r in s:print(*r)
