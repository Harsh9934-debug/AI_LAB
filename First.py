#write a program for the toh 

def toh(n,a='A',b='B',c='C'):
    if n==0:
        return
    toh(n - 1, a, c, b)
    print(f"move disk {n} from {a} to {c}")
    toh(n - 1, b, a, c)

toh(3)
