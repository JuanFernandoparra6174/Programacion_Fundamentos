import numpy as np
#Ecuacion 1
Valx=int(input("Colocar el valor de x: "))
Valy=int(input("Colocar el valor de y: "))
Const=int(input("Colocar valor de la constante: "))
#Ecuacion 2
Valx2=int(input("Colocar el valor de x: "))
Valy2=int(input("Colocar el valor de y: "))
Const2=int(input("Colocar valor de la constante: "))


A = np.array([[Valx, Valy], [Valx2, Valy2]])
b = np.array([Const, Const2])


sol = np.linalg.solve(A, b)

# Imprimir la solución
print("Solución x, y:")
print(sol)
