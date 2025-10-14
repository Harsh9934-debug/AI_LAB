#write a program to solve latin square problem

def printlatin(n):
    for i in range(n):
        for j in range(n):
            print((i+j)%n+1,end=" ")
        print()
printlatin(4)