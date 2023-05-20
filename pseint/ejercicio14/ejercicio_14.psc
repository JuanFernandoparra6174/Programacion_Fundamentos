Algoritmo ejercicio_14
	// Programa: Fundamentos de programacion
	// Nombre del archivo: ejercicio 14
	// Descripcion : Programa que calcula la sumatoria de los primeros 50 numeros enteros
	// Autor: Juan Fernando Parra Rincon
	// Fecha: 1/5/2023
	// Version: 1.0
	//  Escribir un algoritmo que acepte tres números enteros e imprima el mayor de ellos.
	definir number1, number2, number3 Como entero
	number1<-0
	number2<-0
	number3<-0
	Escribir "numero1"
	leer number1
	escribir "numero2"
	leer number2
	escribir "numero3"
	leer number3
	
	Si number1=number2 y number1=number3 y number2=number1 y number2=number3 y number3= number1 y number3 = number2 Entonces
		Escribir "no hay igual"
	SiNo
		Si number1>number2 y number1>number3 Entonces
			Escribir "el numero mayor es : " number1
		SiNo
			Si number2>number1 y number2>number3 Entonces
				Escribir "el numero mayor es: " number2
			SiNo
				Si number3>number1 y number3>number2 Entonces
				 escribir "el numero mayor es: " number3
				Fin Si
			Fin Si
		Fin Si
	Fin Si
FinAlgoritmo
