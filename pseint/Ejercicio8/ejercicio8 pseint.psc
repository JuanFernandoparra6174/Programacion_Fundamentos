Algoritmo sin_titulo
	// area de descripcion
	// enunciado:Programa que calcula la suma de los numero pares comprendidos entre 2 y 100
	// desarrollado por: Juan Fernando Parra
	// version: 1.0
	// fecha: 2/24/2023
	// area de declaracion de variables
	Definir v_numIni Como Entero
	Definir v_numFin Como Entero
	Definir v_i Como Entero
	Definir v_valSum Como Entero
	// area de inicializacion de variables
	v_numIni <- 0
	v_numFin <- 0
	v_i <- 0
	v_valSum <- 0
	// Area de lectura
	Escribir ' Escribir desde que numero se iniciara la suma'
	Leer v_numIni
	Escribir ' Escrbir hasta que numero se sumara'
	Leer v_numFin
	// area procesos
	Para v_i<-v_numIni Hasta v_numFin Con Paso 2 Hacer
		v_valSum <- v_valSum+v_i
	FinPara
	Escribir 'La suma total de los numeros es: ',v_valSum
FinAlgoritmo
