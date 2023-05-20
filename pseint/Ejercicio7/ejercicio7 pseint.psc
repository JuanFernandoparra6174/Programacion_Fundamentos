Algoritmo ejercicio7
	// area de descripcion:
	// enunciado: Calcular la media de una serie de numeros positivos, suponiendo que los datos
	// se leen desde un terminal. Un valor de cero como entrada indicara que se ha alcanzado el final de la serie de numeros positivos.
	// desarrolado por: Juan Fernando Parra
	// version:1.0
	// fecha:3/03/2023
	// area de declaracion de variables
	Definir v_valNum Como Real
	Definir v_conTdor Como Real
	Definir v_valSum Como Real
	Definir v_valProm Como Real
	// area de inicializacion de variables
	v_valNum <- 0.0
	v_conTdor <- 0.0
	v_valSum <- 0.0
	v_valProm <- 0.0
	// area de lectura
	Escribir ' Escribir serie de numeros, cuando se escriba 0, el promedio se calcula automaticamente'
	// area de procesos 
	Repetir
		Leer v_valNum
		Si v_valNum>0 Entonces
			v_valSum <- v_valSum+v_valNum
			v_conTdor <- v_conTdor+1
		SiNo
			v_valProm <- v_valSum/v_conTdor
		FinSi
	Hasta Que v_valNum=0
	Escribir 'la suma de los numeros es de: ',v_valSum
	Escribir ' La cantida de numeros es: ',v_conTdor
	Escribir 'el promedio de los numeros es: ',v_valProm
FinAlgoritmo
