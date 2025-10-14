maze = [[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]

def solve(m):
    n = len(m)
    sol = [[0]*n for _ in range(n)]

    def go(x,y):
        if x<0 or y<0 or x>=n or y>=n or m[x][y]==0 or sol[x][y]:
            return False
        sol[x][y]=1
        if (x,y)==(n-1,n-1) or go(x+1,y) or go(x,y+1):
            return True
        sol[x][y]=0
        return False

    if not go(0,0):
        print("Solution doesn't exist")
    else:
        for r in sol:
            print(' '.join(map(str,r)))

if __name__=='__main__':
    solve(maze)
    