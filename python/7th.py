#write a program the list of operation in the dictionery 

d={'name':'harsh','age':20,'course':'btech'}
for k,v in d.items():
    print("The key is ",k,"the value is ",v)

for k in d.keys():
    print("The key is ",k)

for v in d.values():
    print("The value is",v)

print(d.get('name'))
print(d.items())
print(d.keys())
print(d.values())