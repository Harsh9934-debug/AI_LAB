#write a program to implement the water jug problem 

print("Water jug problem ")
x=int(input("Enter X: "))
y=int(input("Enter Y: "))
while True:
    sno=int(input("Enter the step number : "))
    if sno==1:
        if x<4:
            x=4
    if sno==2:  
        if y<3:
            y=3
    if sno==5:
        if x>0:
            x=0
    if sno==6:
        if y>0:
            y=0
    if sno==7:
        if x+y>=4 and y>0:
            x,y=4,y-(4-x)
    if sno==8:
        if x+y>=3 and x>0:
            x,y=x-(3-y),3
    if sno==9:
        if x+y<4 and y>0:
            x,y=x+y,0

    if sno==10:
        if x+y<3 and x>0:
            x,y=0,x+y

    print("X=",x)
    print("Y=",y)   
    if x==2:
        print("Goal State Reached")
        break

# To run this give it like 
# 2 9 2 7 5 9 