#write a program to find the area of the geometric figures

def circle(r):
    area= 3.14*r*r
    print("area of the circle is :",area)
def square(a):
    area=a*a
    print("area of the square is :",area)
def rectangle(l,b):
    area= l*b
    print("area of the rectangle is :",area)
def triangle(b,h):
    area = (0.5*b*h)
    print("area of the triangle is :",area)
radius=int(input("enter the radius of the circle :"))
circle(radius)
side=int(input("Enter the side of the square :"))
square(side)
length=int(input("Enter the length of the rectangle :"))
breadth=int(input("Enter the breadth of the rectangle :"))
rectangle(length,breadth)
base=int(input("Enter the base of the triangle :"))
height=int(input("Enter the height of the triangle :"))
triangle(base,height)