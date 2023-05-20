Algoritmo ejercicio_12
	// Programa: Fundamentos de programacion
	// Nombre del archivo: ejercicio 13
	// Descripcion : Programa que calcula el producto  de los n primeros numeros naturales
	// Autor: Juan Fernando Parra Rincon
	// Fecha: 1/5/2023
	// Version: 1.0
	//  Escribir un algoritmo que calcule el producto de los n primeros números naturales.
	number=0
	producto=1
	escribir " numero que quieres sabes su producto"
	leer number
	Si number>=0 Entonces
		Para i<-1 Hasta number Hacer
			producto<-producto*i
		
		Fin Para
		Escribir "numero: ", number
		Escribir "el producto es ", producto
	SiNo
	 Escribir "el numero dado es incorrecto"
 Fin Si
 
FinAlgoritmo
