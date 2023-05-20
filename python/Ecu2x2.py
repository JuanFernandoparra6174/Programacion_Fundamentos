#Solucíon de una ecuación 2x2 con 3 incognitas
print("Valores de la ecucacion 1")
Valx=int(input("Colocar el valor de x: "))
Valy=int(input("Colocar el valor de y: "))
Valz=int(input("Colocar el valor de z: "))
Const=int(input("Colocar valor de la constante: "))
print("Valores de la ecucacion 2")
Valx2=int(input("Colocar el valor de x: "))
Valy2=int(input("Colocar el valor de y: "))
Valz2=int(input("Colocar el valor de z: "))
Const2=int(input("Colocar valor de la constante: "))
print("Valores de la ecuacion3 ")
Valx3=int(input("Colocar el valor de x: "))
Valy3=int(input("Colocar el valor de y: "))
Valz3=int(input("Colocar el valor de z: "))
Const3=int(input("Colocar valor de la constante: "))
import numpy as np
lista1=[]
lista1.append
A=np.array([[Valx,Valy,Valz],[Valx2,Valy2,Valz2],[Valx3,Valy3,Valz3]])
B=np.array([Const,Const2,Const3])
Solve=np.linalg.solve[A,B]
print(Solve)