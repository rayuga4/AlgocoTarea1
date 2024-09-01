import time

nombre = "datasetDesordenado.txt"
file = open(nombre,"r")
aux = file.readline()
file.close()

list = [int(num) for num in aux.strip().split()]

start = time.time()

list.sort()

print(str(time.time()-start) + " segundos")

aux = "timSort"+nombre
file = open(aux,"w")
for num in list:
    file.write(str(num)+ " ")