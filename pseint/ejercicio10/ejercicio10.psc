Algoritmo ejercicio10
	// area de descripcion:
	// enunciado: Programa que calcula la cantidad a pagar de una llamda telefonica
	// desarrollado por: Juan Fernando Parra
	// version:1.0
	// fecha:3/03/2023
	// area de declaracion de variables
	Definir v_cantMin Como Entero
	Definir v_cantMinExt Como Entero
	Definir v_valMinSinCarg Como Entero
	Definir v_valMinConCarg Como Entero
	Definir v_precLlam Como Entero
	// area de inicializacion de variables
	v_cantMin <- 0
	v_cantMinExt <- 0
	v_valMinSinCarg <- 0
	v_valMinConCarg <- 0
	v_precLlam <- 0
	// area de lectura
	Escribir 'escribir cantidad de minutos'
	Leer v_cantMin
	// area de procesos
	Si v_cantMin<3 Entonces
		v_valMinSinCarg <- 10
		v_precLlam <- v_valMinSinCarg
		Escribir 'el coste de la llamada fue de :',v_precLlam
	SiNo
		v_cantMinExt <- v_cantMin-3
		v_valMinSinCarg <- 10
		v_valMinConCarg <- v_cantMinExt*5
		v_precLlam <- v_valMinSinCarg+v_valMinConCarg
		Escribir 'Los minutos extras fueron de : ',v_cantMinExt
		Escribir 'el coste de la llamada fue de: ',v_precLlam
	FinSi
FinAlgoritmo
