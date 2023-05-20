Algoritmo ejercicio_2
	// area de descripcion
	// enunciado: Un formula 1 que parte del reposo alcanza una velocidad de 216 km/h en 10 s. Calcula su aceleracion.
	// desarrollado por: Juan Fernando Parra
	// version: 1.0
	// fecha: 2/22/2023
	// area de delcaracion de variables
	Definir v_valVelIni Como Entero
	Definir v_valVelfin Como Entero
	Definir v_valVelfinMet Como Entero
	Definir v_valTiem Como Entero
	Definir v_valAcel Como Entero
	// area de inicializacion de variables
	v_valVelIni <- 0
	v_valVelfin <- 0
	v_ValVelfinMet <- 0
	v_valTiem <- 0
	v_valAcel <- 0
	// area de lectura
	Escribir 'escribir la velocidad inicial'
	Leer v_valVelIni
	Escribir 'escribir la velocidad final'
	Leer v_valVelfin
	Escribir 'escribir el tiempo transcurrido entre el cambio de velocidad inicial y velocidad final'
	Leer v_valTiem
	// area de procesos
	v_ValVelfinMet <- (v_valVelfin*1000)/(3600)
	v_valAcel <- (v_ValVelfinMet-v_valVelIni)/(v_valTiem)
	Escribir 'La aceleracion en m/s^2 fue de : ',v_valAcel
FinAlgoritmo
