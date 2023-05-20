Algoritmo ejercicio_4
	// area de descripcion
	// enunciado: Un cuerpo posee una velocidad inicial de 12 m/s y una aceleracion de 2 m/s2 
	// Cuanto tiempo tardara en adquirir una velocidad de 144 Km/h
	// desarrollado por: Juan Fernando Parra
	// version: 1.0
	// fecha: 2/22/2023
	// area de delcaracion de variables
	Definir v_valVelIni Como Entero
	Definir v_valVelFin Como Entero
	Definir v_valVelFinMet Como Entero
	Definir v_valAcel Como Entero
	Definir v_valTiem Como Entero
	// area de inicializacion de variables
	v_valVelIni <- 0
	v_valVelFin <- 0
	v_valVelFinMet <- 0
	v_valAcel <- 0
	v_valTiem <- 0
	// area de lectura
	Escribir 'escribir la velocidad inicial'
	Leer v_valVelIni
	Escribir 'escribir la velocidad final'
	Leer v_valVelFin
	Escribir 'escribir la aceleracion'
	Leer v_valAcel
	// area de procesos
	v_valVelFinMet <- (v_valVelFin*1000)/(3600)
	v_valTiem <- (v_valVelFinMet-v_valVelIni)/(v_valAcel)
	Escribir 'el tiempo en segundos que tardara en alcanzar la velocidad final es de  : ',v_valTiem
FinAlgoritmo
