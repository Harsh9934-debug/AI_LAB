#write a program to perform string handler 

college="Presidency"

print("presidency has",len(college),"letters")
print(college[0])
print(college.upper())
print(college.lower())
print("college has",college.count('e'),"e")
for i in college :
    print(i)
print(college[:3])
print(college[3:])
print(college[2:5])

print(college.replace("Presidency","PES"))
