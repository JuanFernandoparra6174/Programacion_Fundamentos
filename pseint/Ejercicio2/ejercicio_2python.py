# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


if __name__ == '__main__':
	# area de descripcion
	# enunciado: Un formula 1 que parte del reposo alcanza una velocidad de 216 km/h en 10 s. Calcula su aceleracion.
	# desarrollado por: Juan Fernando Parra
	# version: 1.0
	# fecha: 2/22/2023
	# area de delcaracion de variables
	v_valvelini = int()
	v_valvelfin = int()
	v_valvelfinmet = int()
	v_valtiem = int()
	v_valacel = int()
	# area de inicializacion de variables
	v_valvelini = 0
	v_valvelfin = 0
	v_valvelfinmet = 0
	v_valtiem = 0
	v_valacel = 0
	# area de lectura
	print("escribir la velocidad inicial")
	v_valvelini = int(input())
	print("escribir la velocidad final")
	v_valvelfin = int(input())
	print("escribir el tiempo transcurrido entre el cambio de velocidad inicial y velocidad final")
	v_valtiem = int(input())
	# area de procesos
	v_valvelfinmet = (v_valvelfin*1000)/(3600)
	v_valacel = (v_valvelfinmet-v_valvelini)/(v_valtiem)
	print("La aceleracion en m/s^2 fue de : ",v_valacel)

