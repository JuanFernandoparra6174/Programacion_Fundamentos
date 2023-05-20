lista=[]
posicion=0



for x in range (5):
    valor=int(input("ingrese valor: "))
    lista.append(valor);

mayor=lista[0]
for x in range(1,5):
        if lista[x]>mayor:
            mayor=lista[x]

menor=lista[0]
for x in range (1,5):
        if lista[x]<menor:
            menor=lista[x];

#leer un numero por teclado y resonder esto: si esta o no esta, si esta cuantas veces se repite y en que posiciones
numero=int(input("ingresar el numero que quieres ver cuanto se repite: "))
repeticiones=lista.count(numero)
print=("numero mayor es: ",mayor)
print=("numero menor es: ",menor)
print=("las repeticiones del numero fue: ",repeticiones)





