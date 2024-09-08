import time
import numpy as np

file = open("matrices 200 200.txt","r")
nOriginal,mOriginal = [int(num) for num in file.readline().strip().split()]
m1 = file.readline().strip().strip(",").split(",")
for row in range(len(m1)):
    m1[row] = [int(num) for num in m1[row].strip().split()]
m2 = file.readline().strip().strip(",").split(",")
for row in range(len(m2)):
    m2[row] = [int(num) for num in m2[row].strip().split()]

#Implementacion obtenida de https://www.geeksforgeeks.org/strassens-matrix-multiplication-algorithm-implementation/ 
def strassen(A, B):
    n = A.shape[0]
 
    # base case: 1x1 matrix
    if n == 1:
        return A * B
    else:
        # split input matrices into quarters
        mid = n // 2
        A11, A12, A21, A22 = A[:mid, :mid], A[:mid, mid:], A[mid:, :mid], A[mid:, mid:]
        B11, B12, B21, B22 = B[:mid, :mid], B[:mid, mid:], B[mid:, :mid], B[mid:, mid:]
 
        # calculate p1 to p7
        P1 = strassen(A11 + A22, B11 + B22)
        P2 = strassen(A21 + A22, B11)
        P3 = strassen(A11, B12 - B22)
        P4 = strassen(A22, B21 - B11)
        P5 = strassen(A11 + A12, B22)
        P6 = strassen(A21 - A11, B11 + B12)
        P7 = strassen(A12 - A22, B21 + B22)
 
        # calculate the 4 quarters of the resulting matrix
        C11 = P1 + P4 - P5 + P7
        C12 = P3 + P5
        C21 = P2 + P4
        C22 = P1 + P3 - P2 + P6
 
        # combine the 4 quarters into a single result matrix
        C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
 
        return C
    
start = time.time()

A = np.array(m1)
B = np.array(m2)

n = max(A.shape[0], A.shape[1], B.shape[0], B.shape[1])
m = 1
while m < n:
    m *= 2
A = np.pad(A, ((0, m - A.shape[0]), (0, m - A.shape[1])), mode='constant')
B = np.pad(B, ((0, m - B.shape[0]), (0, m - B.shape[1])), mode='constant')

C = strassen(A, B)

print(str(time.time()-start) + " segundos")

print(C)
out = C.tolist()

name = "strassen " + "matrices " + str(nOriginal) + " " + str(mOriginal) + ".txt"
file = open(name, "w")
file.write(str(nOriginal)+" "+str(mOriginal)+"\n")
for row in out:
    for value in row:
        file.write(str(value)+" ")
    file.write(", ")