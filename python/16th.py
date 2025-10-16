#user defined exceptiion 

class FiveDivisionError(Exception): 
    pass

try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    if b == 5: 
        raise FiveDivisionError("cannot divide by five")
    print("division is:", a / b)
except (FiveDivisionError, ZeroDivisionError) as e:
    print(e)
