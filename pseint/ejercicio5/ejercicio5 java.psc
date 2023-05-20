Algoritmo ejercicio5
	// area de descripcion:
	// enunciado : Calcular el salarario de un empleado en base a las horas trabajadas semanalmente, tarifa, horas extras e impustos aplicados
	// desarrollado por: Juan Fernando Parra
	// version:1.0
	// fecha:3/3/2023
	// area de declararacion de variables
	Definir v_nomEmp Como Caracter
	Definir v_horTraSem Como Entero
	Definir v_valHorEmp Como Entero
	Definir v_numHorDiur Como Entero
	Definir v_valHorDiur Como Entero
	Definir v_numHorNoct Como Entero
	Definir v_valHorNoct Como Entero
	Definir v_valPagImp Como Real
	Definir v_valSalBrut Como Real
	Definir v_valSalNet Como Real
	// area de inicializacion de variables
	v_nomEmp <- ''
	v_horTraSem <- 0
	v_valHorEmp <- 0
	v_numHorDiur <- 0
	v_valHorDiur <- 0
	v_numHorNoct <- 0
	v_valHorNoct <- 0
	v_valPagImp <- 0.0
	v_valSalBrut <- 0.0
	v_valSalNet <- 0.0
	// area de lectura
	Escribir 'Nombre del trabajador'
	Leer v_nomEmp
	Escribir 'Horas trabajadas diurnas'
	Leer v_numHorDiur
	Escribir 'Horas trabajadas nocturnas'
	Leer v_numHorNoct
	Escribir 'Valor de la hora del trabajador'
	Leer v_valHorEmp
	// area de procesos
	v_horTraSem <- v_numHorDiur+v_numHorNoct
	v_valHorDiur <- v_numHorDiur*v_valHorEmp
	v_valHorNoct <- v_numHorNoct*((v_valHorEmp*0.40)+v_valHorEmp)
	v_valSalBrut <- v_valHorDiur+v_valHorNoct
	v_valPagImp <- v_valSalBrut*0.19
	v_valSalNet <- v_valSalBrut-v_valPagImp
	Escribir 'Nombre del trabajador ',v_nomEmp
	Escribir 'Horas trabajadas semanalmente ',v_horTraSem
	Escribir 'Salario sin aplicacion de impuestos: ',v_valSalBrut
	Escribir 'Valor total de los impuestos ',v_valPagImp
	Escribir ' Salario neto del trabajador ',v_valSalNet
FinAlgoritmo
