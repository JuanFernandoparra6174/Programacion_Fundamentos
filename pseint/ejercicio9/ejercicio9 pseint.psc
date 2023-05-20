Algoritmo ejercicio9
	// descripcion: 
	// enunciado: Programa que calcula el salario de los empleados
	// desarrollado por: Juan Fernando Parra
	// version:1,0
	// fecha:/5/2023
	// area de declaracion de variables
	Definir v_nomEmp Como Caracter
	Definir v_horSemTra Como Entero
	Definir v_valHor Como Real
	Definir v_horTraExt Como Entero
	Definir v_horTraSinExt Como Entero
	Definir v_valHorSinExt Como Real
	Definir v_valHorExt Como Real
	Definir v_valSal Como Real
	// area de inicializacion de variables
	v_nomEmp <- ''
	v_horSemTra <- 0
	v_valHor <- 0.0
	v_horTraExt <- 0
	v_horTraSinExt <- 0
	v_valHorSinExt <- 0.0
	v_valHorExt <- 0.0
	v_valSal <- 0.0
	// area de lectura
	Escribir 'Nombre del empleado'
	Leer v_nomEmp
	Escribir 'Escriba las horas trabajadas semanalmente'
	Leer v_horSemTra
	Escribir 'Valor de la hora del trabajador'
	Leer v_valHor
	// area de procesos
	Si v_horSemTra>40 Entonces
		v_horTraExt <- v_horSemTra-40
		v_valHorExt <- (v_valHor+(v_valHor*1.5))*v_horTraExt
		v_horTraSinExt <- v_horSemTra-v_horTraExt
		v_valHorSinExt <- v_valHor*v_horTraSinExt
		v_valSal <- (v_valHorSinExt+v_valHorExt)*4
		Escribir 'El nombre del empleado es ',v_nomEmp
		Escribir 'El numero de horas extras es de: ',v_horTraExt
		Escribir ' El salario del empleado es de: ',v_valSal
	SiNo
		v_valSal <- v_horSemTra*v_valHor*4
		Escribir 'El nombre del empleado es',v_nomEmp
		Escribir ' El salario del empleado es de: ',v_valSal
	FinSi
FinAlgoritmo
