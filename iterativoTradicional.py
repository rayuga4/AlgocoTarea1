file = open("matrices.txt","r")
n,m = [int(num) for num in file.readline().strip().split()]
m1 = file.readline().strip().strip(",").split(",")
for row in range(len(m1)):
    m1[row] = [int(num) for num in m1[row].strip().split()]
m2 = file.readline().strip().strip(",").split(",")
for row in range(len(m2)):
    m2[row] = [int(num) for num in m2[row].strip().split()]
out = [[0 for x in range(n)] for y in range(n)]
for x in range(len(m1)):
    for y in range(len(m2[0])):
        for z in range(len(m2)):
            out[x][y] += m1[x][z]*m2[z][y]
for row in out:
    print(row)
