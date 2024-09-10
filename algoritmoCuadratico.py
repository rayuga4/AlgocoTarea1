#Bubble sort
import time

nombre = "datasetDesordenado.txt"
file = open(nombre,"r")
aux = file.readline()
file.close()

list = [int(num) for num in aux.strip().split()]

start = time.time()

for x in range(len(list)):
    flag=False
    for y in range(len(list)-x-1):
# si el elemento actual es mayor al siguiente, se intercambian
        if list[y]>list[y+1]:
            aux = list[y+1]
            list[y+1] = list[y]
            list[y] = aux
            flag = True
# si no se realiza ningun swap en una iteracion, la lista esta ordenada y se sale del ciclo
    if not flag:
        break

print(str(time.time()-start) + " segundos")

aux = "bubbleSort"+nombre
file = open(aux,"w")
for num in list:
    file.write(str(num)+ " ")
