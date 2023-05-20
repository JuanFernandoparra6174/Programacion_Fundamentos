import random
Equipos =["Águilas Doradas", "Alianza Petrolera", "América de Cali", "Atlético Bucaramanga",
         "Atlético Junior", "Atlético Nacional", "Deportivo Cortuluá" ,"Deportes Tolima",
         "Deportivo Cali" , "Deportivo Pasto" , "Deportivo Pereira" , "Envigado FC" ,
        "Independientes Medellin" , "Independientes Santa Fé", "Jaguares de Cordoba" ,
                  "La Equidad", "Millonarios" , "Once Caldas", "Patriotas FC" , "Unión Magdalena"]
def menu():
    print("===================// Menú //===================")
    print("1 | Tabla de Jornadas de la liga")
    print("2 | Tabla de resultados de la liga")
    print("3 | Todos los resultados de un equipo de la liga")
    print("4 | Tabla de puntaje")
    print("5 | Salir del menú.")
    print("=================================================")
    Opcion = int(input("| 1 | 2 | 3 | 4 | 5 ----> "))
    return Opcion
while True:
    Opcion = menu()
    if Opcion == 1:
        partidos = []
        equiposLocal = Equipos[:len(Equipos)//2]
        equiposVisit = Equipos[len(Equipos)//2:]
        for i in range(len(equiposLocal)):
            for j in range(len(equiposVisit)):
                if i % 2 == 0:
                    partido = [equiposLocal[i], equiposVisit[j]]
                else:
                    partido = [equiposVisit[j], equiposLocal[i]]
                partidos.append(partido)
        resultados = []
        for partido in partidos:
            goles_local = random.randint(0, 5)
            goles_visitante = random.randint(0, 3)
            resultado = [partido[0], partido[1], goles_local, goles_visitante]
            resultados.append(resultado)
        print("=============================================== Jornadas de la liga ===============================================")
        print("===================================================================================================================")
        print("       Equipo local      |         Equipo visitante        |         Goles local         |     Goles visitante    |")
        print("===================================================================================================================")
        for resultado in resultados:
            print("{:<24} | {:<31} | {:<27} | {:<30}".format(resultado[0], resultado[1], resultado[2], resultado[3]))
        print("===================================================================================================================")    
    elif Opcion == 2:
        partidos = []
        for i in range((len(Equipos))):
            for j in range(i+1, len(Equipos)):
                partido = [Equipos[i], Equipos[j]]
                partidos.append(partido)      
        resultados = []
        for partido in partidos:
            goles_local = random.randint(0, 5)
            goles_visitante = random.randint(0, 3)
            resultado = [partido[0], partido[1], goles_local, goles_visitante]
            resultados.append(resultado)
        goles = {}
        partidos_ganados = {}
        partidos_empatados = {}
        partidos_perdidos = {}
        GolesContra = {}
        for equipo in Equipos:
            goles[equipo] = 0
            partidos_ganados[equipo] = 0
            partidos_empatados[equipo] = 0
            partidos_perdidos[equipo] = 0
            GolesContra[equipo] = sum([resultado[3] for resultado in resultados if resultado[1] == equipo])
        for resultado in resultados:
            goles[resultado[0]] += resultado[2]
            goles[resultado[1]] += resultado[3]
            GolesContra[resultado[0]] += resultado[3]
            GolesContra[resultado[1]] += resultado[2]
            if resultado[2] > resultado[3]:
                partidos_ganados[resultado[0]] += 1
                partidos_perdidos[resultado[1]] += 1
            elif resultado[2] == resultado[3]:
                partidos_empatados[resultado[0]] += 1
                partidos_empatados[resultado[1]] += 1
            else:
                partidos_ganados[resultado[1]] += 1
                partidos_perdidos[resultado[0]] += 1
        print("============================================== Tabla de Resultados ============================================")
        print("===============================================================================================================")
        print("           Equipo              |     Goles     |   Goles En Contra   |    Ganados    |   Empatados   | Perdidos")
        print("===============================================================================================================")
        for equipo in Equipos:
            print("{:<30} | {:<13} | {:<19} | {:<13} | {:<13} | {:<12}".format(equipo, goles[equipo], GolesContra[equipo], partidos_ganados[equipo],
                                                                  partidos_empatados[equipo], partidos_perdidos[equipo]))
        print("===============================================================================================================")
        MaxG = max(goles, key = lambda k: goles[k])
        print("El equipo más goleador fue:", MaxG)
        print("=========================================================")
        EquipoMenosGoles = min(GolesContra, key = GolesContra.get)
        print("El equipo que menos goles recibió fue:", EquipoMenosGoles)
        print("=========================================================")
    elif Opcion == 3:
        partidos = []
        Equipo = input("Ingrese un equipo: ")
        while Equipo not in Equipos:
            print("")
            Equipo = input("Equipo no encontrado, ingrese un equipo nuevamente: ")
            if Equipo in Equipos:
                break
        Pos = Equipos.index(Equipo)
        Equipos.pop(Pos)
        for i in range((len(Equipos))):
            partido = [Equipo, Equipos[i]]
            partidos.append(partido)
            partidoVis = [Equipos[i], Equipo]
            partidos.append(partidoVis)
        resultados = []
        for partido in partidos:
            goles_local = random.randint(0, 5)
            goles_visitante = random.randint(0, 3)
            resultado = [partido[0], partido[1], goles_local, goles_visitante]
            resultados.append(resultado)  
        print("=============================================== Jornadas de la liga ===============================================")
        print("===================================================================================================================")
        print("      Equipo Local     |         Equipo visitante        |         Goles local         |     Goles visitante    |  ")
        print("===================================================================================================================")
        for resultado in resultados:
            print("{:<24} | {:<32} | {:<22} | {:<28}".format(resultado[0], resultado[1], resultado[2], resultado[3]))
        print("===================================================================================================================")
    elif Opcion == 4:
        partidos = []
        for i in range((len(Equipos))):
            for j in range(i+1, len(Equipos)):
                partido = [Equipos[i], Equipos[j]]
                partidos.append(partido)      
        resultados = []
        for partido in partidos:
            goles_local = random.randint(0, 5)
            goles_visitante = random.randint(0, 3)
            resultado = [partido[0], partido[1], goles_local, goles_visitante]
            resultados.append(resultado)
        goles = {}
        partidos_ganados = {}
        partidos_empatados = {}
        partidos_perdidos = {}
        Puntos = {}
        GolesContra = {}
        for equipo in Equipos:
            goles[equipo] = 0
            partidos_ganados[equipo] = 0
            partidos_empatados[equipo] = 0
            partidos_perdidos[equipo] = 0
            Puntos[equipo] = 0
            GolesContra[equipo] = sum([resultado[3] for resultado in resultados if resultado[1] == equipo])
        for resultado in resultados:
            goles[resultado[0]] += resultado[2]
            goles[resultado[1]] += resultado[3]
            GolesContra[resultado[0]] += resultado[3]
            GolesContra[resultado[1]] += resultado[2]
            if resultado[2] > resultado[3]:
                partidos_ganados[resultado[0]] += 1
                Puntos[resultado[0]] += 3 
                partidos_perdidos[resultado[1]] += 1
            elif resultado[2] == resultado[3]:
                partidos_empatados[resultado[0]] += 1
                Puntos[resultado[0]] += 1
                partidos_empatados[resultado[1]] += 1
                Puntos[resultado[1]] += 1
            else:
                partidos_ganados[resultado[1]] += 1
                Puntos[resultado[1]] += 3 
                partidos_perdidos[resultado[0]] += 1
        def OrdPunt(equipo):
            return Puntos[equipo]
        EqOrd = sorted(Equipos, key = OrdPunt, reverse = True)
        print("=========================================================== Tabla de Resultados =====================================================")
        print("=====================================================================================================================================")
        print("             Equipo             |     Puntos    |     Goles     |       Goles en Contra      |  Ganados    |   Empatados   | Perdidos")
        print("=====================================================================================================================================")
        for equipo in EqOrd:
            print("{:<30} | {:<13} | {:<13} | {:<25} | {:<13} | {:<13} | {:<13}".format(equipo, Puntos[equipo], goles[equipo], GolesContra[equipo], partidos_ganados[equipo],
                                                                              partidos_empatados[equipo], partidos_perdidos[equipo]))
        print("=====================================================================================================================================")
        suma = 0
        for valores in goles.values():
            suma += valores
        print("El total de los goles fue:", suma)
        print("==========================================================================================================")
        MaxG = max(goles, key = lambda k: goles[k]) 
        print("El equipo más goleador fue:", MaxG)
        print("==========================================================================================================")
        EquipoMenosGoles = min(GolesContra, key = GolesContra.get)
        print("El equipo que menos goles recibió fue:", EquipoMenosGoles)
        print("==========================================================================================================")
    elif Opcion == 5:
        print("==================================================")
        print("Gracias por utilizar el programa | Fin del proceso")
        print("==================================================")
        break
    if Opcion in [1, 2, 3, 4]:
        respuesta = input("¿Desea continuar en el menú? | S | N | ----> ") 
        if respuesta.upper() != "S":
            print("==================================================")
            print("Gracias por utilizar el programa | Fin del proceso")
            print("==================================================")
            break