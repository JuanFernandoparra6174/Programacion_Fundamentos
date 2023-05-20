Algoritmo ejercicio20
	//area de descripcion
	// enunciado: Diseñar un programa que lea tres numeros A, B, C y visualice en pantalla el valor del más grande. Se supone que los tres valores son diferentes.
	// diseñador por: Juan Fernando Parra
	// version: 1.0
	// fecha: 3/06/2023
	
	
	
	// area de declaracion de variables
	definir v_numA Como Entero
	Definir  v_numB Como Entero
	definir v_numC Como Entero
	definir v_numMay Como Entero
	
	
	
	//area de inicializacion de variables
	v_numA<-0
	v_numB<-0
	v_numC<-0
	v_numMay<-0
	
	
	
	//area de lectura
	Escribir "el numero A es: "
	leer v_numA
	Escribir "el numero B es: "
	leer v_numB
	Escribir "el numero C es "
	leer v_numC
	
	
	
	//area de procesos
	
	Si v_numA= v_numB y v_numA = v_numC Entonces
		Escribir "los numeros deben ser diferentes"
	SiNo
		si  v_numA>v_numB y v_numA> v_numC Entonces
			v_numMay<-v_numA
			escribir " el numero mayor es ", v_numMay
		sino 
			si  v_numB>v_numA y v_numB> v_numC Entonces
				v_numMay<-v_numB
				Escribir " el numero mayor es ", v_numMay
			SiNo
				si v_numC>v_numB y v_numC> v_numA entonces 
					v_numMay<- v_numC
					escribir "el numero mayor es ", v_numMay
					fin si 
				fin si 
			fin si
		
		
	Fin Si
	
	
	
	
	
FinAlgoritmo
