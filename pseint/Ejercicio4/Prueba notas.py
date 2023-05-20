v_canEst=0
c_valExateo=0.40
c_valExaPra=0.60
v_defPriPar=0.0
v_conCic=1
v_SumPriPar=0
v_sumExateo=0.0
v_sumExaPra=0


#leer cantidad de estudiantes
v_canEst=int(input("digite numero de estudiantes: "))
for v_conCic in range(v_canEst):
    v_nomEst = input("Nombre estudiante: ")
    v_genEst=input("genero del estudiante: ")
    v_notExtTeo= float(input("Digite nota examen teorico: "))
    v_notExaPra= float(input("Digite nota examen practico: "))
    #cálculo de la nota del primer parcial por estudiante
    v_notDefPriPar= v_notExtTeo*c_valExateo+v_notExaPra*c_valExaPra
    print("su nota del primer parcial es:" ,v_notDefPriPar)
    #calcular la suma de las notas de los estudiantes 
    v_SumPriPar= v_SumPriPar+v_notDefPriPar
    #calcular la suma de las notas del examen teorico
    v_sumExateo = v_sumExateo + v_notExtTeo
    #calcular la suma de las notas del examen practico
    v_sumExateo=v_sumExateo + v_notExaPra
# calcular el promedio de los estudiantes
v_promNot=v_SumPriPar/v_canEst
print(" El promedio del primer parcial es: ", v_promNot)
# calcular el promedio de las notas del examen teorico2
v_promExateo= v_sumExateo/v_canEst
print("El promedio del examen teorico es: ",v_promExateo)
# calcular el promedio de las notas del examen practico
v_promExaPra= v_sumExaPra/v_canEst
print("El promedio del examen practico es: ",v_promExaPra)
