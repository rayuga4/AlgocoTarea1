#Bubble sort
import time
start = time.time()

nombre = "datasetOrdenado.txt"
file = open(nombre,"r")
aux = file.readline()
file.close()

list = [int(num) for num in aux.strip().split()]

for x in range(len(list)):
    flag=False
    for y in range(len(list)-x-1):
        if list[y]>list[y+1]:
            aux = list[y+1]
            list[y+1] = list[y]
            list[y] = aux
            flag = True
    if not flag:
        break

print(str(time.time()-start) + " segundos")

print(list)

print(str(time.time()-start) + " segundos")