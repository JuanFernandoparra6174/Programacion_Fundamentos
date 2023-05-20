import random
lista1=[]
lista2=[]
for x in range (20):
    numero=random.randint(1,20)
    lista1.append(numero);
print("lista de numeros random",lista1)
canTNu=len(lista1)-1
contador=0
for k in range (canTNu):
    for x in range (canTNu):
        if lista1[x]>lista1[x + 1]:
            auxil=lista1[x]
            lista1[x]=lista1[x + 1]
            lista1[x + 1]=auxil
print("lista de numeros random ordenada",lista1);
print("Lista sin repetir ordenada",set(lista1))
canTNu2=len(lista1)
for x in range (canTNu2):
        if lista1[x]==lista1[x]:
            lista2.append(lista1.count(lista1[x]))
print("los numeros de la lista se repiten:",lista2)



