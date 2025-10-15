# write a program to implement the arithematic operation in python 

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b

print("Select operation.")
print("1.add")
print("2.sub")
print("3.mul")
print("4.div")


choice=input("Enter choice(1/2/3/4): ")

a=int(input("Enter a: "))
b=int(input("Enter b: "))   


if choice in ('1','2','3','4'):
    if choice=='1':
        print(a,"+",b,"=",add(a,b))
    elif choice=='2':
        print(a,"-",b,"=",sub(a,b))
    elif choice=='3':
        print(a,"*",b,"=",mul(a,b))
    elif choice=='4':
        print(a,"/",b,"=",div(a,b))
else:
    print("Invalid Input")
