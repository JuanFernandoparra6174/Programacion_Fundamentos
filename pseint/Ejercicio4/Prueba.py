v_canEst=0
c_valExateo=0.40
c_valExaPra=0.60
v_defPriPar=0.0
v_conCic=1
v_SumPriPar=0.0

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
    #calcular la suma de los estudiantes para calcula de los esudiantes
    v_SumPriPar= v_SumPriPar+v_notDefPriPar;
v_promNot=v_SumPriPar/v_canEst
print(" El promedio del primer parcial es: ", v_promNot),v_promNot

