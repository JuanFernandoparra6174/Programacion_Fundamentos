Algoritmo ejericicio17
	//area de descripción
	//enunciado: hallar el area de un triangulo conociendo sus lados
	//desarrollado:Juan Fernando Parra
	//version: 1.0
	//fecha: 03/09/2023
	
	
	
	//area de declaracion de variables
	definir v_ladoA Como Real
	definir v_ladoB Como Real
	definir v_ladoC Como Real
	definir v_valPerMtro como real
	definir v_valSemPerMtro como Real
	definir v_valArea como real
	definir v_sumAyB como real
	definir v_valMult Como Real
	definir v_valRai como real
	
	
	//area de inicializacion de variables
	v_ladoA<-0-0
	v_ladoB<-0.0
	v_ladoC<-0.0
	v_sumAyB<-0.0
	v_valPerMtro<-0.0
	v_valSemPerMtro<-0.0
	v_valMult<-0.0
	v_valRai<-0-0
	v_valArea<-0.0
	
	
	
	//area de lectura
	escribir"valor de lado A  "
	leer v_ladoA
	escribir"valor de lado B "
	leer v_ladoB
	escribir"valor de lado C "
	leer v_ladoC
	
	
	
	//area de procesos
	v_sumAyB<- v_ladoA+v_ladoB
	Si v_sumAyB>v_ladoC Entonces
		v_valPerMtro<- v_ladoA+v_ladoB+v_ladoC
		v_valSemPerMtro<-v_valPerMtro/2
		v_valMult<- v_valSemPerMtro*(v_valSemPerMtro-v_ladoA)*(v_valSemPerMtro-v_ladoB)*(v_valSemPerMtro-v_ladoC)
		v_valRai<- raiz(v_valMult)
		v_valArea<-v_valRai
		Escribir "el area del triangulo en m^4 es de :",v_valArea
	SiNo
		Escribir " el triangulo algebraicamente es imposible de construir"
	Fin Si
	

	
	
	
	
	
	
FinAlgoritmo
