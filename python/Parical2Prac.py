import random

equipos = ["Equipo 1", "Equipo 2", "Equipo 3", "Equipo 4", "Equipo 5"]
goles_local = [random.randint(0, 5) for _ in range(len(equipos))]
goles_visitante = [random.randint(0, 3) for _ in range(len(equipos))]
partidos = list(zip(equipos, goles_local, goles_visitante))

print(partidos)
partidos_por_equipo = {}

for partido in partidos:
    equipo_local = partido[0]
    equipo_visitante = partido[1]

    if equipo_local not in partidos_por_equipo:
        partidos_por_equipo[equipo_local] = 1
    else:
        partidos_por_equipo[equipo_local] += 1

    if equipo_visitante not in partidos_por_equipo:
        partidos_por_equipo[equipo_visitante] = 1
    else:
        partidos_por_equipo[equipo_visitante] += 1

print(partidos_por_equipo)
partidos_ganados_por_equipo = {}

for partido in partidos:
    equipo_local = partido[0]
    equipo_visitante = partido[1]
    goles_local = partido[2]
    goles_visitante = partido[3]

    if goles_local > goles_visitante:
        if equipo_local not in partidos_ganados_por_equipo:
            partidos_ganados_por_equipo[equipo_local] = 1
        else:
            partidos_ganados_por_equipo[equipo_local] += 1
    elif goles_visitante > goles_local:
        if equipo_visitante not in partidos_ganados_por_equipo:
            partidos_ganados_por_equipo[equipo_visitante] = 1
        else:
            partidos_ganados_por_equipo[equipo_visitante] += 1

print(partidos_ganados_por_equipo)
goles_por_equipo = {}

for partido in partidos:
    equipo_local = partido[0]
    equipo_visitante = partido[1]
    goles_local = partido[2]
    goles_visitante = partido[3]

    if equipo_local not in goles_por_equipo:
        goles_por_equipo[equipo_local] = goles_local
    else:
        goles_por_equipo[equipo_local] += goles_local

    if equipo_visitante not in goles_por_equipo:
        goles_por_equipo[equipo_visitante] = goles_visitante
    else:
        goles_por_equipo[equipo_visitante] += goles_visitante

print(goles_por_equipo)
equipo_mas_goles = max(goles_por_equipo, key=goles_por_equipo.get)

print(equipo_mas_goles)
equipo_menos_goles_recibidos = min(goles_por_equipo, key=goles_por_equipo.get)

print(equipo_menos_goles_recibidos)
