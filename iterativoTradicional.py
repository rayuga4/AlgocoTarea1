import time
file = open("matrices 1000 1000.txt","r")
n,m = [int(num) for num in file.readline().strip().split()]
m1 = file.readline().strip().strip(",").split(",")
for row in range(len(m1)):
    m1[row] = [int(num) for num in m1[row].strip().split()]
m2 = file.readline().strip().strip(",").split(",")
for row in range(len(m2)):
    m2[row] = [int(num) for num in m2[row].strip().split()]

start = time.time()

out = [[0 for x in range(n)] for y in range(n)]
for x in range(len(m1)):
    for y in range(len(m2[0])):
        for z in range(len(m2)):
            out[x][y] += m1[x][z]*m2[z][y]

print(str(time.time()-start) + " segundos")

name = "iterativo " + "matrices " + str(n) + " " + str(m) + ".txt"
file = open(name, "w")
file.write(str(n)+" "+str(m)+"\n")
for row in out:
    for value in row:
        file.write(str(value)+" ")
    file.write(", ")
#for row in out:
#    print(row)
