import itertools

equipos_colombianos = ["Aguilas Doradas", "Alianza Patrolera", "America de Cali", "Atletico Bucaramanga", "Atletico Junior", "Atletico Nacional", "Deportivo Cortulua", "Deportes Tolima", "Deportivo Cali", "Deportivo Pasto", "Deportivo Pereira", "Envigado FC", "Independientes Medellin", "Independientes Santa Fe", "Jaguares de Cordoba", "La Equidad", "Millonarios", "Once Caldas", "Patriotas FC", "Union Magdalena"]
#punto1
# Crear todas las posibles combinaciones de partidos
partidos = list(itertools.combinations(equipos_colombianos, 2))

# Crear un diccionario para contar los partidos por equipo
partidos_por_equipo = {equipo: 0 for equipo in equipos_colombianos}

# Contar los partidos por equipo
for partido in partidos:
    local, visitante = partido
    partidos_por_equipo[local] += 1
    partidos_por_equipo[visitante] += 1

# Imprimir los resultados
for equipo, partidos in partidos_por_equipo.items():
    print(f"{equipo} jugó {partidos} partidos.")
#punto2
import random

equipos_colombianos = ["Aguilas Doradas", "Alianza Patrolera", "America de Cali", "Atletico Bucaramanga", "Atletico Junior", "Atletico Nacional", "Deportivo Cortulua" ,"Deportes Tolima", "Deportivo Cali" , "Deportivo Pasto" , "Deportivo Pereira" , "Envigado FC" , "Independientes Medellin" , "Independientes Santa Fe", "Jaguares de Cordoba" , "La Equidad", "Millonarios" , "Once Caldas", "Patriotas FC" , "Union Magdalena"]

partidos = []
goles_por_partido = {}
goles_locales = {}
goles_visitantes = {}
ganados_locales = {}
ganados_visitantes = {}

# Generar todas las posibles combinaciones de equipos
for i in range(len(equipos_colombianos)):
    for j in range(len(equipos_colombianos)):
        if i != j:
            partido_local = (equipos_colombianos[i], equipos_colombianos[j])
            partido_visitante = (equipos_colombianos[j], equipos_colombianos[i])
            if partido_local not in partidos and partido_visitante not in partidos:
                partidos.append(partido_local)

# Inicializar los diccionarios con 0 goles y 0 partidos ganados
for partido in partidos:
    goles_por_partido[partido] = (0, 0)
    goles_locales[partido[0]] = 0
    goles_visitantes[partido[1]] = 0
    ganados_locales[partido[0]] = 0
    ganados_visitantes[partido[1]] = 0

# Simular los goles en cada partido y determinar el ganador
for partido in partidos:
    goles_local = random.randint(0, 5)
    goles_visitante = random.randint(0, 5)
    goles_por_partido[partido] = (goles_local, goles_visitante)
    goles_locales[partido[0]] += goles_local
    goles_visitantes[partido[1]] += goles_visitante
    if goles_local > goles_visitante:
        ganados_locales[partido[0]] += 1
    elif goles_visitante > goles_local:
        ganados_visitantes[partido[1]] += 1

# Imprimir la lista de partidos y la cantidad de partidos jugados por cada equipo
for partido in partidos:
    print(partido[0], "vs", partido[1], "-", goles_por_partido[partido][0], ":", goles_por_partido[partido][1])

print("\nPartidos ganados locales:")
for equipo, ganados in ganados_locales.items():
    print(equipo, "-", ganados, "partidos ganados")

print("\nPartidos ganados visitantes:")
for equipo, ganados in ganados_visitantes.items():
    print(equipo, "-", ganados, "partidos ganados")
