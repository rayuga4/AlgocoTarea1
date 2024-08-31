import time
start = time.time()

nombre = "datasetMitadOrdenado.txt"
file = open(nombre,"r")
aux = file.readline()
file.close()

list = [int(num) for num in aux.strip().split()]

list.sort()

print(str(time.time()-start) + " segundos")

#print(list)

#print(str(time.time()-start) + " segundos")