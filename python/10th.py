#write a program to find the factorial of a number using recursion

def fact(n):
    if n==0:
        return 1
    return n*fact(n-1)
n=5
print(f"The factorial of the number {n} is ",fact(n))