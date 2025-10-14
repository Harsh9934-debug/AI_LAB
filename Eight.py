m=[[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
n=len(m)
s=[[0]*n for _ in m]
def f(x,y):
    if not(0<=x<n and 0<=y<n and m[x][y]and not s[x][y]):
        return 0
    s[x][y]=1
    if (x,y)==(n-1,n-1)or f(x+1,y)or f(x,y+1):
        return 1
    s[x][y]=0
f(0,0)
for r in s:print(*r)

