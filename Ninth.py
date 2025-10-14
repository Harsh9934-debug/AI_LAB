#write a program to solve latin square problem

def printlatin(n):
    for i in range(n):
        print(*list(range(i+1,n+1))
              +list(range(1,i+1)))
printlatin(5)