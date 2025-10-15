#write a program to demonstrate the list of operations

a=[1,2,3,4,5]

print(a)
a.append(6)
print(a)
a.insert(0,0)
print(a)
a.remove(3)
print(a)
a.pop()
print(a)    
a[1]=100
print(a)
print(a.index(4))
print(a.count(2))
a.sort()
print(a)
a.reverse()
print(a)
b=[7,8,9]
a.extend(b)
print(a)    