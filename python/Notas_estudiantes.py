#inicializar variables
nomEst=""
canEst=0
genEst=0
notExaPra=0.0
notExaTeo=0.0
sumExam=0.0
promEst=0.0
v_sumTotalProm=0.0
v_promTotal=0.0
v_sumExaPra=0.0
v_sumExaTeo=0.0
v_conMuj=0
v_conHom=0
v_sumMuj=0.0
v_sumHom=0.0
v_promHom=0.0
v_promMuj=0.0
v_sumTotalProMj=0.0
v_sumTotalProHm=0.0
notMaxEs=0.0
notMinEs=0.0
listNotMax = []
listNotMin= []
listExaTeoMax=[]
listExaTeoMin=[]
listExaPra=[]
notMaxMj=0.0
notMaxHom=0.0
listNotMaxMj=0.0

#Pedir numero de estudiantes
canEst=int(input("Cantidad de estudiantes: "))
#Hacer ciclo
for x in range (canEst):
    #Pedir nombre del estudiante
    nomEst=input("Nombre del estudiante: ")
    #Pedir el genero
    genEst=int(input("Sí el genero del estudiantes es hombre teclear 1 y sí es mujer teclear 0: "))
    #Pedir nota del examen practico
    notExaPra=float(input("valor del examen practico: "))
    #Pedir nota del examen teorico
    notExaTeo=float(input("valor del examen teorico: "))
    #Valor del examen practico
    v_valExaPra=notExaPra*0.40
    #valor del examen teorico
    v_valExaTeo=notExaTeo*0.60
    #Hallar promedio de cada estudiante
    v_promEst=(v_valExaPra+v_valExaTeo)/(0.40+0.60)
    print ("El promedio del estudiante es ",v_promEst)
    #Contador suma promedio total de estudiantes
    v_sumTotalProm=v_sumTotalProm+v_promEst
    #Contador suma examenes practicos
    v_sumExaPra=notExaPra+v_sumExaPra
    #Contador suma examenes teoricos
    v_sumExaTeo=notExaTeo+v_sumExaTeo
    #hallar nota máxima por estudiante
    if notExaPra>notExaTeo:
       notMaxEs=notExaPra
       print ("La nota maxima del estudiante fue: ",notMaxEs)
    else:
       notMaxEs=notExaTeo
       print("La nota maxima del estudiante fue: ",notMaxEs);
    #Hacer una lista de datos que guarde las notas máximas de todos los estudiantes
    listNotMax.append(notMaxEs)
    #hallar nota minima de todos los estudiantes
    if notExaPra<notExaTeo:
        notMinEs=notExaPra
        print ("La nota minima del estudiante fue: ",notMinEs)
    else:
        notMinEs=notExaTeo
        print ("La nota minima del estudiante fue: ",notMinEs);
    #Lista de datos que guarde las notas minimas de los estudiantes
    listNotMin.append(notMinEs)
    #hallar nota Maxima examen teorico
    listExaTeoMax.append(notExaTeo)
    #hallar nota minima examen teorico
    listExaTeoMin.append(notExaTeo)
    #Hallar nota maxima y minima del examen practico}
    listExaPra.append(notExaPra)

        
        

    #Contador cantidad de mujeres
    if genEst==0:
        v_conMuj=v_conMuj+1
        #Promedio de mujeres
        v_sumTotalProMj=v_sumTotalProMj+v_promEst
        v_promMuj=v_sumTotalProMj/v_conMuj
        #hallar nota maxima mujeres
    elif notExaPra>notExaTeo:
       notMaxMj=notExaPra
       #hacer lista de todas las notas maximas de las mujeres
       listNotMaxMj.append(notMaxMj)
    elif notExaTeo>notExaPra:
        notMaxMj=notExaTeo
        #hacer lista de todas las notas maximas de las mujeres
        listNotMaxMj.append(notMaxMj)

    
        


        
    else:
       #Contador cantidad de hombres
        v_conHom=v_conHom+1
        #Promedio de hombres
        v_sumTotalProHm=v_sumTotalProHm+v_promEst
        v_promHom=v_sumTotalProHm/v_conHom
    if notExaPra<notExaTeo:
        notMinEs=notExaPra
   
        
        





    
    
#hallar promedio total de estudiantes
v_promTotal=v_sumTotalProm/canEst
print ("El promedio total de los estudiantes: ",v_promTotal)
#hallar promedio de examenes practicos
v_promPra=v_sumExaPra/canEst
print ("El promedio del examen practico es: ",v_promPra)
#hallar promedio de examenes teoricos
v_promTeo=v_sumExaTeo/canEst
print ("El promedio del examen teorico es: ",v_promTeo)
#numero de mujeres y hombres
print ("El numero de mujeres son: ",v_conMuj)
print ("El numero de hombres son: ",v_conHom)
#promedio de mujeres y hombres
print ("El promedio de los examenes de las mujeres es: ",v_promMuj)
print ("El promedio de los examenes de los hombres es: ",v_promHom)
#Nota maxima de todos los estudiantes
print("La nota Maxima de todos los estudiantes fue: ",max(listNotMax))
#Nota minima de todos los estudiantes
print("La nota minima de todos los estudiantes fue: ",min(listNotMin))
#Nota maxima de examen teorico de todos los estudiantes
print("La nota maxima del examen teorico de todos los estudiantes fue: ",max(listExaTeoMax))
#Nota minima de examen teorico de todos los estudiantes 
print("La nota minima del examen teorico de todos los estudiantes fue: ",min(listExaTeoMin))
#Nota maxima del examen practico de todos los estudiantes
print("La nota maxima del examen practico de todos los estudiantes fue: ",max(listExaPra))
#Nota minima del examen practico de todos los estudiantes
print("La nota minima del examen practico de todos los estudiantes fue: ",min(listExaPra))
#Nota maxima de las mujeres
print("La nota maxima de las mujeres fue de: ",max(listNotMaxMj) )
