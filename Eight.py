#write a program to solve the rat in the maze program 

def is_safe(maze,x,y):
    if x>=0 and x<len(maze) and y>=0 and y<len(maze) and maze[x][y]==1:
        return True
    return False
def solve_maze(maze):
    sol=[[0 for j in range(len(maze))]for i in range(len(maze))]
    if solve_util(maze,0,0,sol)==False:
        print("Solution doesn't exist")
        return False
    print_solution(sol)
    return True
def solve_util(maze,x,y,sol):   
    if x==len(maze)-1 and y==len(maze)-1:
        sol[x][y]=1
        return True
    if is_safe(maze,x,y)==True:
        sol[x][y]=1
        if solve_util(maze,x+1,y,sol)==True:
            return True
        if solve_util(maze,x,y+1,sol)==True:
            return True
        sol[x][y]=0
        return False
    return False
def print_solution(sol):
    for i in sol:
        for j in i:
            print(j,end=" ")
        print()
maze=[[1,0,0,0],[1,1,0,1],[0,1,0,0],[1,1,1,1]]
solve_maze(maze)    