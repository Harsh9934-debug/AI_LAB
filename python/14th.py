#write a pogram to filer even number from the even list 

def even(n):
    if n%2==0:
        return True
    return False    
n=[1,2,3,4,5,6,7,8,9,10]
out=list(filter(even,n))
print(out)