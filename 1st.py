#Write a program for the tower of hanoi 

def toh(n,a='A',b='B',c='C'):
    if n==0:
        return 
    toh(n-1,a,c,b)    
    print(f"movr the disk {n} form {a} to {c}")
    toh(n-1,b,a,c)
toh(3)