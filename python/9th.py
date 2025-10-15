#write a program to demonsterate the sum of series 

n=int(input("enter the value of n"))
x=int(input("enter the value of x"))

sum=1
for i in range(2,n+1):
    sum=sum+((x**i)/i)
print("sum of series is",sum)
