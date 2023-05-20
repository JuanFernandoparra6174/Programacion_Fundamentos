import random

equipos_colombianos = ["Nacional", "Junior", "Millonarios", "Santa Fe", "Cali"]

equipos_local = []
equipos_visitante = []
goles_local = []
goles_visitante = []

# Generar todas las posibles combinaciones de equipos
for i in range(len(equipos_colombianos)):
    for j in range(len(equipos_colombianos)):
        if i != j:
            partido_local = (equipos_colombianos[i], equipos_colombianos[j])
            partido_visitante = (equipos_colombianos[j], equipos_colombianos[i])
            if partido_local not in equipos_local and partido_visitante not in equipos_visitante:
                equipos_local.append(partido_local)
                equipos_visitante.append(partido_visitante)
                goles_local.append(0)
                goles_visitante.append(0)

# Simular los resultados de los partidos y actualizar los registros de goles y partidos jugados
num_partidos = 10 # Cantidad de partidos a simular
for i in range(num_partidos):
    for j in range(len(equipos_local)):
        gol_local = random.randint(0, 3)
        gol_visitante = random.randint(0, 3)
        goles_local[j] += gol_local
        goles_visitante[j] += gol_visitante

# Imprimir los resultados
print("Equipos de local: ", equipos_local)
print("Equipos de visitante: ", equipos_visitante)
print("Goles de local: ", goles_local)
print("Goles de visitante: ", goles_visitante)

# Calcular la cantidad de partidos jugados por cada equipo
partidos_local_jugados = {}
partidos_visitante_jugados = {}
for i in range(len(equipos_colombianos)):
    equipo = equipos_colombianos[i]
    partidos_local_jugados[equipo] = 0
    partidos_visitante_jugados[equipo] = 0

for i in range(len(equipos_local)):
    equipo_local = equipos_local[i][0]
    equipo_visitante = equipos_visitante[i][0]
    partidos_local_jugados[equipo_local] += 1
    partidos_visitante_jugados[equipo_visitante] += 1

print("Partidos jugados por equipo de local: ", partidos_local_jugados)
print("Partidos jugados por equipo de visitante: ", partidos_visitante_jugados)

