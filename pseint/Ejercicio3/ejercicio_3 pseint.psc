Algoritmo ejercicio_3
	// area de descripcion
	// enunciado://Una locomotora necesita 10 s. para alcanzar su velocidad normal que es 25m/s.
	// Suponiendo que su movimiento es uniformemente acelerado, Que aceleracion se le ha comunicado y que espacio 
	// ha recorrido antes de alcanzar la velocidad regular?//
	// desarrollado por: Juan Fernando Parra
	// version: 1.0
	// fecha: 2/22/2023
	// area de delcaracion de variables
	Definir v_valVelIni Como Entero
	Definir v_valVelFin Como Entero
	Definir v_valTiem Como Entero
	Definir v_valAcel Como Real
	Definir v_valRec Como Entero
	// area de inicializacion de variables
	v_valVelIni <- 0
	v_valVelFin <- 0
	v_valTiem <- 0
	v_valAcel <- 0.0
	v_valRec <- 0
	// area de lectura
	Escribir 'escribir la velocidad inicial'
	Leer v_valVelIni
	Escribir 'escribir la velocidad final'
	Leer v_valVelFin
	Escribir 'escribir el tiempo transcurrido entre el cambio de velocidad inicial y velocidad final'
	Leer v_valTiem
	// area de procesos
	v_valAcel <- (v_valVelFin-v_valVelIni)/(v_valTiem)
	Escribir 'La aceleracion en m/s^2 fue de : ',v_valAcel
	v_valRec <- (v_valVelIni*v_valTiem)+((1/2*v_valAcel)*(v_valTiem^2))
	Escribir 'El recorrorrido en metros antes de alcanzar la velocidad regular fue de: ',v_valRec
FinAlgoritmo
