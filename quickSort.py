import time

nombre = "datasetMitadOrdenado.txt"
file = open(nombre,"r")
aux = file.readline()
file.close()

list = [int(num) for num in aux.strip().split()]

start = time.time()



print(str(time.time()-start) + " segundos")

#print(list)

#print(str(time.time()-start) + " segundos")