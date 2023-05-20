import random

equipos_colombianos = ["Nacional", "Junior", "Millonarios", "Santa Fe", "Cali"]
partidos_local = []
partidos_visitante = []

# Generar todas las posibles combinaciones de equipos
for i in range(len(equipos_colombianos)):
    for j in range(len(equipos_colombianos)):
        if i != j:
            partido_local = (equipos_colombianos[i], equipos_colombianos[j], 0, 0)
            partido_visitante = (equipos_colombianos[j], equipos_colombianos[i], 0, 0)
            if partido_local not in partidos_local and partido_visitante not in partidos_visitante:
                partidos_local.append(partido_local)
                partidos_visitante.append(partido_visitante)

# Simular los goles en cada partido
for i in range(len(partidos_local)):
    goles_local = random.randint(0, 5)
    goles_visitante = random.randint(0, 5)
    partidos_local[i] = (partidos_local[i][0], partidos_local[i][1], partidos_local[i][2] + goles_local, partidos_local[i][3] + 1)
    partidos_visitante[i] = (partidos_visitante[i][0], partidos_visitante[i][1], partidos_visitante[i][2] + goles_visitante, partidos_visitante[i][3] + 1)

# Imprimir la lista de partidos locales y la cantidad de partidos y goles por equipo
print("Partidos locales:")
for equipo in equipos_colombianos:
    partidos_jugados = 0
    goles = 0
    for partido in partidos_local:
        if partido[0] == equipo:
            partidos_jugados += 1
            goles += partido[2]
    print(equipo, "-", partidos_jugados, "partidos jugados,", goles, "goles")

# Imprimir la lista de partidos visitantes y la cantidad de partidos y goles por equipo
print("\nPartidos visitantes:")
for equipo in equipos_colombianos:
    partidos_jugados = 0
    goles = 0
    for partido in partidos_visitante:
        if partido[0] == equipo:
            partidos_jugados += 1
            goles += partido[2]
    print(equipo, "-", partidos_jugados, "partidos jugados,", goles, "goles")
