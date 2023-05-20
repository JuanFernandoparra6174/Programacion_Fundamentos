Algoritmo ejercicio19
	//area de descripcio:
	//enunciado:Preguntar que dia de la semana fue el dia 1 del mes actual y calcular que dia de la semana es hoy.
	//desarrolado: Juan Fernando Parra
	//version:1.0
	//fecha:3/5/2023
	
	
	
	//area de declalaracion de variavles
	definir v_dia Como Entero
	definir v_diaLun Como Caracter
	definir v_diaMar Como Caracter
	Definir v_diaMie Como Caracter
	definir v_diaJue Como Caracter
	definir v_diaSab Como Caracter
	definir v_diaDom Como Caracter
	definir v_dia1 como caracter
	
	
	
	//area de inicializacion de variables
	v_dia<-0
	v_diaLun<-""
	v_diaMar<-""
	v_diaMie<- ""
	v_diaVie<-""
	v_diaSab<-""
	v_diaDom<-""
	v_dia1<-""
	
	
	//area de lectura
	Escribir " escribir el dia en numeros"
	leer v_dia
	
	
	
	//area de procesos
	
	Si v_dia<=31 y v_dia>0 Entonces
		Si v_dia=6 o v_dia=13 o v_dia=20 o v_dia=27 Entonces
			v_diaLun<- "Lunes"
			escribir " el dia de la semana es ", v_diaLun
		SiNo
			Si v_dia=7 o v_dia=14 o v_dia=21 o v_dia=28 Entonces
				v_diaMart<- "Martes" 
				escribir "el dia de la semana es ", v_diaMart
			SiNo
				Si v_dia=1 o v_dia=8 o v_dia=15 o v_dia=22 o v_dia=29 Entonces
					v_diaMie<- "Miercoles"
					escribir " el dia de la semana es ", v_diaMie
				SiNo
					Si v_dia=2 o v_dia=9 o v_dia=16 o v_dia=23 o v_dia=30 Entonces
						v_diaJue<- "Jueves"
						Escribir "el dia de la semana es ", v_diaJue
					SiNo
						Si v_dia=3 o v_dia=10 o v_dia=17 o v_dia=24 o v_dia=31 Entonces
							v_diaVie<- "Viernes" 
							Escribir "el dia de la semana es ", v_diaVie
						SiNo
							Si v_dia=4 o v_dia=11 o v_dia=18 o v_dia=25 Entonces
								v_diaSab<- "Sabado"
								Escribir "el dia de la semana es ", v_diaSab
							SiNo
								Si v_dia=5 o v_dia=12 o v_dia=19 o v_dia=26 Entonces
									v_diaDom<- "Domingo"
									Escribir "el dia de la semana es ", v_diaDom
									Si v_dia<=31 y v_dia>0 Entonces
										
									Fin Si
								
								Fin Si
							Fin Si
						Fin Si
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	SiNo
		escribir " el dia en numeros debe estar entre 1 y 31"
	Fin Si
	v_dia1<- "Miercoles"
	Si v_dia<=31 y v_dia>0 Entonces
		Escribir " el primer dia de la semana del mes fue " v_dia1
		fin si
	
	
FinAlgoritmo
