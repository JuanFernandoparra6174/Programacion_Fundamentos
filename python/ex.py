# leer un numero he imprimir cuantas veces se repite 
#7 gestor de notas que tiene una lista de nombres, de edades, nota final de program, de inasistencias vamo a generar una lista de conceptos con estos parametros, si la nota final de progrom es menor a 30 se pierde academicamente si las asistencia son mayores a 12 perdio si inasistencias es mayor a 12 y la nota es menor a 30 cambie de carrera
import random
lista1=[]
for x in range (20):
    numero=random.randint(1,20)
    lista1.append(numero);
print(lista1)
canTNu=len(lista1)-1
contador=0
numCont=int(input("Escrbir numero que quieres contar cuantas veces se repite: "))
for x in range (canTNu):
    if lista1[x]==numCont:
        contador=contador+1

print("el numero se repite",contador);
print("el numero que se repite",lista1.count(numCont))
