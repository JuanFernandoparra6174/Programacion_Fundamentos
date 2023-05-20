Algoritmo ejercicio18
	//area de descripcion
	//enunciado: leida una fecha decir el dia de la semana
	//desarrolado: Juan Fernando Parra
	//version: 1.0
	//fecha:3/0462023
	
	
	
	//area de declaracion de variables
	definir v_dia como entero
	
	
	
	
	//area de inicialización de variables
	v_dia<-0
	
	
	
	
	//area de lectura
	escribir" Digitar el día en numero "
	leer v_dia
	
	
	
	
	//area de procesos
	Si v_dia<=30 y v_dia>1 Entonces
		Si v_dia=1 o v_dia=8 o v_dia=15 o v_dia=22 o v_dia= 29 Entonces
			Escribir  "el dia de la semana es lunes "
		SiNo
			Si v_dia=2 o v_dia=9 o v_dia=16 o v_dia=23 o v_dia=30  Entonces
				Escribir "el dia de la semana es martes"
			SiNo
				Si v_dia=3 o v_dia=10 o v_dia=17 o v_dia=24 Entonces
					Escribir "el dia de la semana es miercoles"
				SiNo
					Si v_dia=4 o v_dia=11 o v_dia=18 o v_dia=25 Entonces
						Escribir "el dia de la semana es jueves"
					SiNo
						Si v_dia=5 o v_dia=12 o v_dia=19 o v_dia=26 Entonces
							Escribir "el dia de la semana es viernes"
						SiNo
							Si v_dia=6 o v_dia=13 o v_dia=20 o v_dia=27 Entonces
								Escribir "el dia de la semana es sabado"
							SiNo
								Si v_dia=7 o v_dia=14 o v_dia=21 o v_dia=28 Entonces
									Escribir "el dia de la semana fue domingo"
								
								Fin Si
							Fin Si
						Fin Si
					Fin Si
				Fin Si
			Fin Si
		Fin Si
	SiNo
		escribir " el dia debe estar entre 1 y 30 "
	Fin Si
	
FinAlgoritmo
