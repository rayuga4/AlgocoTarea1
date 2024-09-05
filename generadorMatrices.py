import random
n = 15
m = random.randint(5,10)
m1 = []
for x in range(n):
    m1.append([])
    for y in range(m):
        m1[x].append(random.randint(0,100))
m2 = []
for x in range(m):
    m2.append([])
    for y in range(n):
        m2[x].append(random.randint(0,100))
print(m1)
print(m2)
name = "matrices.txt"
file = open(name, "w")
file.write(str(n)+" "+str(m)+"\n")
for row in m1:
    for value in row:
        file.write(str(value)+" ")
    file.write(", ")
file.write("\n")
for row in m2:
    for value in row:
        file.write(str(value)+" ")
    file.write(", ")